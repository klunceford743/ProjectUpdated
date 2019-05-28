"""
Katie Lunceford and Jon Li

This file contains the class for a scikit decision
tree. The class as the attributes self.tree, self.labels, 
and self.depth which all start off as None.

The class has the methods train, eval, and toDot.
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz


class SKTree:

    def __init__(self):
        self.tree = None
        self.labels = None
        self.depth = None

    def train(self, data, labels, depth):
        """
        Training method that trains a decision tree based off of the
        given data.
        We assume that data is a 2D python list, the target in colum 0
        """
        self.labels = labels
        self.depth = depth
        
        x = [None]*len(data)
        y = [None]*len(data)

        for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t


        self.tree = DecisionTreeClassifier(criterion="entropy", max_depth=depth, random_state=0)
        self.tree = self.tree.fit(x,y)

    def eval(self, data):
        """
        Method that evaluates the author for a document once the decision tree has been 
        trained.
        We assume that data is a 2D python list, with the target [0] == None
        """

        x = [None]*len(data)
        for row in range(len(data)):
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t

        x = self.tree.predict(x)
        #Now you will have to get the values from y and move them to the targe column of data
        return x


    def toDot(self, filename):
        """
        Makes a .dot file with the tree.
        """
        dot_data = export_graphviz(self.tree, out_file=filename, feature_names=self.labels)


    
