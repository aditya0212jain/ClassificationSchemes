import csv
import numpy as np
import kMeans as kMeans

with open('../Medical_data.csv','r') as csv_file:
    csv_reader = list(csv.reader(csv_file,delimiter=","))
    csv_dicReader = csv.DictReader(csv_file)
    my_data = np.array(csv_reader)
    ##following the data for Medical_data.csv for kMeans
    new_data = np.array(my_data[1:,1:],dtype=np.float)
    kMeansClassfier = kMeans.kMeans(3,new_data.shape[0],new_data.shape[1]) ##k,n,d 3000,3
    kMeansClassfier.showValues()
    kMeansClassfier.classify(new_data)
