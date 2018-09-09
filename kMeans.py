
# coding: utf-8

# In[1]:


import numpy as np
import scipy
from scipy.stats import norm
import math
import random


# In[12]:


class kMeans:

    def __init__(self,k,n,d):
        # k is the number of clusters to form
        self.k = k
        # centroid points
        self.centroid = np.zeros(k*d).reshape(k,d)
        # weights are the how much each feature matters
        self.weights = np.ones(k)
        # d is the dimension of the feature vector
        self.d = d
        # n is the number of the samples we have
        self.n = n
        #cluster is the stored value of the data
        self.cluster = np.zeros(n)

    def showValues(self):
        print("k:",self.k)
        print("n:",self.n)
        print("d:",self.d)

    def setWeights(self,data):
        for i in range (0,self.k):
            # for now the weights are set as 1
            self.weights[i]=1

    def dis(self,data,centroidIndex):
        distance =0
        #using euclidean distance with weights in this case
        for i in range (0,self.d):
            distance = distance + (self.weights[i]*((data[i]-self.centroid[centroidIndex][i])**2))
        return distance

    def updateClass(self,data):
        # print('n in update class: ',self.n)
        for i in range (0,self.n):
            minDistance = math.inf
            # print("i in updateClass: ",i)
            for j in range (0,self.k):
                tempDist = self.dis(data[i],j)
                if(tempDist<minDistance):
                    self.cluster[i] = j
                    minDistance = tempDist
                    # print('cluster: ',j)
        # self.printAllClasses()

    def updateCentroids(self,data):
        converged = True
        tempCentroid = np.zeros(self.k*self.d).reshape(self.k,self.d)
        tempCnumbers = np.zeros(self.k)
        for i in range(0,self.n):
            clusIndex = (int)(self.cluster[i])
            # print('clusindex for i:',i,clusIndex)
            tempCnumbers[clusIndex]+=1
            tempCentroid[clusIndex]+=data[i]
        for i in range(0,self.k):
            t = (tempCentroid[i]/tempCnumbers[i])==self.centroid[i]
            for j in range(0,self.d):
                if(t[j]==False):
                    converged = False
                    break
            self.centroid[i] = tempCentroid[i]/tempCnumbers[i]
        return converged

    def initializeCentroids(self,data):
        #right now it takes only the first k elements
        for i in range(0,self.k):
            self.centroid[i] = data[random.randint(0,self.n-1)]

    def classify(self,data):
        convergence = False
        self.initializeCentroids(data)
        p=0
        while((convergence==False) and (p!=100)):
            print(p)
            p+=1
            self.updateClass(data)
            convergence = self.updateCentroids(data)
        print("Classification Done")
        print("Now printing cluster values:")
        self.printAllClasses()

    def getClass(self,data):
        minDistance = math.inf
        clusterNumber = -1
        for j in range (0,self.k):
            tempDist = self.dis(data,j)
            if(tempDist<minDistance):
                clusterNumber = j
                minDistance = tempDist
        return clusterNumber

    def printAllClasses(self):
        for i in range(0,self.n):
            print(self.cluster[i])

            

