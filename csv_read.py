import csv
import numpy as np

with open('../Medical_data.csv','r') as csv_file:
    csv_reader = list(csv.reader(csv_file,delimiter=","))
    csv_dicReader = csv.DictReader(csv_file)
    my_data = np.array(csv_reader)
    # print(my_data)

    ##following the data for Medical_data.csv for kMeans
    new_data = np.array(my_data[1:,1:],dtype=np.float)
    #next() <- makes the line skip
    # my_data = np.genfromtxt('../Medical_data.csv',delimiter=',',skipheader=1)
    # print(my_data[0])

    # for line in csv_reader:
    #     print(line)
    # for line in csv_dicReader:
    #     print(line)
