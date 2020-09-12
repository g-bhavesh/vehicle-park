import sys
import getopt
import pandas as pd
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
    cols = ['date', 'hours', 'vehicle_no', 'vehicle_type', 'log_type']
    e_df = pd.DataFrame(columns = cols)
    if inputfile:
        out_data = []
        with open(inputfile, 'r') as vehicle_log:
            for line in vehicle_log:
                cols_data = line.split(",")
                log_date = cols_data[0]
                date = datetime.datetime.strptime(log_date, "%Y-%m-%d %H:%M:%S.%f").date()
                hours = datetime.datetime.strptime(log_date, "%Y-%m-%d %H:%M:%S.%f").hour
                #minutes = datetime.datetime.strptime(log_date, "%Y-%m-%d %H:%M:%S.%f").minute
                v_no = cols_data[1]
                v_type = cols_data[2]
                log_type = cols_data[3].rstrip("\n")
                out_data.append([date,hours,v_no,v_type,log_type])
        v_df = pd.DataFrame(out_data, columns=cols)
        return v_df
    return e_df

def prepareData(v_df):

    r_df = v_df.groupby(['date','vehicle_no','vehicle_type']).agg({'hours': ['min','max']})
    r_df.columns = ['entry', 'exit']
    r_df = r_df.reset_index()
    r_df['total_hours'] = r_df['exit']-r_df['entry']

    f_df = r_df.groupby(['vehicle_no','vehicle_type']).agg({'total_hours':'mean'})
    f_df.columns = ['avg_hours_per_day']
    f_df = f_df.reset_index()

    return f_df

def main(argv):
    # parse the input file from the argument
    inputfile = parseArgs(argv)

    # prepare raw dataframe from the input dataframe
    v_df = prepareRawData(inputfile)

    # prepare final data from raw data
    f_df = prepareData(v_df)

    # dump findal data into csv file
    f_df.to_csv('../data/final_sample.csv', index=False)



if __name__ == "__main__":
    main(sys.argv[1:])
