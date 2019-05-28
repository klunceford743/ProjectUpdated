"""
Katie Lunceford and Jon Li

This file contains the SKPCA class that uses PCA to analyze author
attribution. The class has attributes self.pca_h which starts off as 
None, self.ncomp which starts off as 0 but will always be set to 2 when 
used in our GUI, self.labels which starts off as None (column labels), 
and self.X which starts off as None (values created by PCA training). 

This class contains the methods train and eval.
"""

import pandas as pd
import numpy as np
from sklearn import decomposition
import math as math
import matplotlib.pyplot as plt

class SKPCA:

    def __init__(self):
        self.pca_h = None
        self.ncomp = 0
        self.labels = None
        self.X = None

    def train(self, data, labels, ncomp):
        """Data is a 2d data list.
           Each row in the 2dlist is sample (all samples probably of a word)
           The first column is the label idenity the sample ("A")
           labels are where the sample came frome, such as from JamesJoyce sisters
        """
        self.ncomp = ncomp
        self.labels = labels
        # print(labels)
        #Strip the first column
        x = [None]*len(data)
        y = [None]*len(data)
        
        for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t

        
        self.pca_h = decomposition.PCA(ncomp)
        self.pca_h.fit(x)
        self.X = self.pca_h.transform(x)
        


    def eval(self, data):
        """
        used to predict the author of a new document once
        the pca is trained and built
        pre: data is a 2d list with one row, the first value 
        should be None and the other values should be the ratio
        that a word with the corresponding label index appears in 
        the document, pca must already be trained so self.pca_h is
        not None and self.X is not None
        post: scatter plot of the pca values assigned to each trained 
        document as well as the predicted document pops up, trained documents'
        values are in blue and the predicted document's values are in red
        once scatter plot is closed, returns the index of the trained document
        that is closest to the predicted document
        """

        #Strip the first column
        x = [None]*len(data)
        y = [None]*len(data)
        
        for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t


         #2 by number of test authors
        
        test = self.pca_h.transform(x)
        x = []
        y = []
        for i in range(len(self.X)):
            x.append(self.X[i,0])
            y.append(self.X[i,1])
        x.append(test[0,0])
        y.append(test[0,1])
        colors = [0]*len(self.X) + [0.7]
        plt.scatter(x,y, c = colors, s = 100)
        plt.show()
         
         #find distance btween all of test and self.X
         #Select one with smallest distance
        ind = 0
        x1 = float(test[0,0])
        x2 = float(test[0,1])
        y1 = float(self.X[0,0])
        y2 = float(self.X[0,1])
        m = math.sqrt((x1-y1)**2 + (x2-y2)**2)
        for i in range(1, len(self.X)):
            y1 = float(self.X[i,0])
            y2 = float(self.X[i,1])
            d = math.sqrt((x1-y1)**2 + (x2 - y2)**2)
            if d < m:
                m = d
                ind = i
        return ind

        
        
