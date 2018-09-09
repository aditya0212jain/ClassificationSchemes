
# coding: utf-8

# In[5]:


import numpy as np
import scipy
from scipy.stats import norm
import math
import random


# In[6]:


class knn:
    """kNearest Neighbour classification implementation"""
    
    def __init__(self,k):
        self.k = k
        
    def euclideanDistance(self,data1,data2,n):
        distance = 0
        for i in range(0,n):
            distance+=np.square(data1[i]-data2[i])
        return np.sqrt(distance)
    
    def manhattanDistance(self,data1,data2,n):
        distance = 0
        for i in range(n):
            distance+=abs(data1[i]-data2[i])
        return distance
    
    def hammingDistance(self,data1,data2,n):
        distance = 0
        for i in range(n):
            if data1[i]==data2[i]:
                distance+=1
        return distance
    
    ##using euclidean distance for now
    def getNeighbours(self,dataset,data):
        distances = []
        length = len(data)
        for i in range(0,len(dataset)):
            ##change the below line for different distances
            dist = self.euclideanDistance(data,dataset[i],length)
            distances.append((dataset[i],dist))
        distances.sort(k=operator.itemgetter(1))
        neighbours = []
        for i in range(self.k):
            neigbours.append(distances[i][0])
        return neighbours
    
    def getClass(self,neighbours):
        classOccurrence = {}
        for i in range(len(neighbours)):
            t = neighbours[i][-1]
            if t in classOccurrence:
                classOccurrence[t]+=1
            else:
                classOccurrence[t] = 1
        sortedOccurrence = sorted(classOccurrence.items(),key=operator.itemgetter(1),reverse=True)
        return sortedOccurrence[0][0]

