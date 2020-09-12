# vehicle-park

We have installed a number-plate detection system in our parking lot. The parking lot can be used only for cars and bikes. The detection system can tell the central system what time a vehicle entered or exited the parking lot, the number of the vehicle, whether it was entry or exit and the type of vehicle. These 4 values come as comma-separated values and are entered in a log file. Write a Python program to analyze this log file and then store the average time a car was parked in the parking lot per day.

Sample log file:

2011-06-26 21:27:41.867801,KA03JI908,Bike,Entry
2011-06-26 21:27:42.863209,KA02JK1029,Car,Exit
2011-06-26 21:28:43.165316,KA05K987,Bike,Entry

Then, build a REST service in Java to query this data based on vehicle number and return the average time.
