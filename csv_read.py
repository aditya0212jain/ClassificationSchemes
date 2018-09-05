import csv
import numpy as np

with open('../Medical_data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_dicReader = csv.DictReader(csv_file)
    #next() <- makes the line skip
    my_data = np.genfromtxt('../Medical_data.csv',delimiter=',')
    print(my_data[0])

    # for line in csv_reader:
    #     print(line)
    # for line in csv_dicReader:
    #     print(line)
