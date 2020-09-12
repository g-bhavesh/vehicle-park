import sys
import getopt
import pandas as pd
import sqlite3
import datetime

def parseArgs(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError as error:
        print("main.py -i <inputfile>")

    for opt, arg in opts:
        if opt=='-h':
            print("main.py -i <inputfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    return inputfile

def prepareRawData(inputfile):
    cols = ['log_date', 'date', 'vehicle_no', 'vehicle_type', 'log_type']
    e_df = pd.DataFrame(columns = cols)
    if inputfile:
        out_data = []
        with open(inputfile, 'r') as vehicle_log:
            for line in vehicle_log:
                cols_data = line.split(",")
                log_date = cols_data[0]
                date = datetime.datetime.strptime(log_date, "%Y-%m-%d %H:%M:%S.%f").date()
                v_no = cols_data[1]
                v_type = cols_data[2]
                log_type = cols_data[3].rstrip("\n")
                out_data.append([log_date,date,v_no,v_type,log_type])
        v_df = pd.DataFrame(out_data, columns=cols)
        return v_df
    return e_df

def prepareData(v_df):
    v_df['entry'] = pd.to_datetime(v_df[v_df['log_type']=='Entry']['log_date']).dt.strftime('%H:%M')
    v_df['entry'].fillna(value='00:00', inplace=True)
    v_df['exit'] = pd.to_datetime(v_df[v_df['log_type']=='Exit']['log_date']).dt.strftime('%H:%M')
    v_df['exit'].fillna(value='23:59', inplace=True)
    r_df = v_df.groupby(['date','vehicle_no','vehicle_type']).agg({'entry':'first', 'exit':'first'})
    r_df.columns = ['entry', 'exit']
    r_df = r_df.reset_index()
    r_df['total_hours'] = (pd.to_datetime(r_df['exit'])-pd.to_datetime(r_df['entry'])).astype('timedelta64[h]')

    f_df = r_df.groupby(['vehicle_no','vehicle_type']).agg({'total_hours':'mean'})
    f_df.columns = ['avg_hours_per_day']
    f_df = f_df.reset_index()
    return f_df

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main(argv):
    db = r"../data/vehicles.db"

    vehicles_table = """ CREATE TABLE IF NOT EXISTS vehicles (
                                        id integer PRIMARY KEY,
                                        vehicle_no text NOT NULL,
                                        vehicle_type text NOT NULL,
                                        avg_hours_per_day DECIMAL(10,5)
                                    ); """
    # create a database connection
    conn = create_connection(db)

    # create tables
    if conn is not None:
        # create vehicles table
        create_table(conn, vehicles_table)
    else:
        print("Error! cannot create the database connection.")

    # parse the input file from the argument
    inputfile = parseArgs(argv)

    # prepare raw dataframe from the input dataframe
    v_df = prepareRawData(inputfile)

    # prepare final data from raw data
    f_df = prepareData(v_df)
    # dump findal data into csv file
    #f_df.to_csv('../data/final_sample.csv', index=False)
    f_df.to_sql('vehicles', conn, if_exists='replace')

if __name__ == "__main__":
    main(sys.argv[1:])
