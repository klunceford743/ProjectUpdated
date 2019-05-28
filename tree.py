""" Katie Lunceford and Jon Li

This file contains a Node class and a ID3 Decision Tree class.

The Node class is made as building blocks of the DecisionTree.
The initialization takes in data, and values. Values is a list
of the potential classifiers of the data. (ex: data would be 
engine size and values would be [small, medium, large]. The 
Node class has four attributes: self.data, self.count, 
self.values, and self.children. At the initialization, self.data = data
self.count = 0, self.values = values, and self.children = [None]*len(values).

The DecisionTree class builds an ID3 tree out of the Nodes. It has attributes
of self.root and self.columns which both equal None at the initialization. 
The methods are train and evaluate.

This file also contains functions for makeTree, predict, multiplePredictions,
findIndex, mostFreq, maxGain, partition, and calculateEntropy.
"""

import math

class Node:

    def __init__(self, data, values):
        self.data = data
        self.count = 0
        self.values = values
        self.children = [None]*len(values)

class DecisionTree:

    def __init__(self):
        self.root = None
        self.columns = None

    def train(self, data, inputAttr, maxDepth):
        """
        given data, column labels and maxDepth, trains a 
        decision tree
        pre: data is a 2D list where the first column of each
        row is the value of what we are training on and the
        other columns are the other attributes, inputAttr is a
        list of the column labels, and maxDepth is a positie integer
        post: self.columns = inputAttr and self.root is the root of 
        an ID3 decision tree made from the data that has a depth
        of less than or equal to maxDepth
        """
        self.columns = inputAttr
        self.root = makeTree(data, inputAttr, maxDepth)

    def evaluate(self, twoDList):
        """
        given a 2D list of data, makes predictions for each row based
        off of a trained decision tree.
        pre: twoDList is a 2D list where the first column of each row is 
        None and the proceeding columns are the attributes that correspond
        to the columns in self.columns, the decision tree must already be
        trained
        post: returns the same twoDlist with the first column of each row
        filled in as a prediction for that value
        """
        return multiplePredictions(self.root, self.columns, twoDList)



def makeTree(data, inputAttr, maxDepth):
    """
    helper function for the trian method in the decision tree
    pre: data is a 2D list that the first column of each row
    is the value we are training are and the other columns are
    the values for the corresponding inputAttr, inputAttr is 
    a list of the column labels, and maxDepth is a positive
    integer
    post: returns the root of an ID3 decision tree made out of
    the data, the depth of the tree is no larger than maxDepth
    """
    if data == []:
        raise Exception
    state = True
    val = data[0][0]
    for x in range(len(data)):
        if data[x][0] != val:
            state = False
            break
    if state:
        n = Node(val, [])
        n.count = len(data)
        return n
    if len(inputAttr) == 1:
        items = []
        for x in range(len(data)):
            items.append(data[x][0])
        val = mostFreq(items)
        n = Node(val, [])
        n.count = len(data)
        return n
    ind = maxGain(data)
    keys = []
    for x in data:
        if not (x[ind] in keys):
            keys.append(x[ind])
    newNode = Node(inputAttr[ind],keys)
    newNode.count = len(data)
    for x in range(len(keys)):
        newData = []
        for y in data:
            if y[ind] == keys[x]:
                new = y[:ind] + y[ind+1:]
                newData.append(new)
        newInput = inputAttr[:ind] + inputAttr[ind+1:]
        newNode.children[x] = makeTree(newData, newInput, maxDepth)
    return newNode


def predict(root, columns, oneDList):
    """
    helper function for multiplePredictions that makes a prediction
    based off of an ID3 decision tree for one document
    pre: root is the root of a decision tree, columns are the labels
    that were used to make that decision tree, and oneD list is a list 
    of a document where the first value is None and the next values
    correspond to the given columns
    post: returns a prediction for the first value in oneDList
    """
    if root == None:
        return None
    if root.children == []:
        return root.data
    ind = findIndex(root.data, columns)
    item = oneDList[ind]
    child = findIndex(item, root.values)
    if child == None:
        print('Cannot predict')
        return None
    answer = predict(root.children[child], columns, oneDList)
    return answer

def multiplePredictions(root, columns, twoDList):
    """
    helper function for the evalaute method in the DecisionTree
    class that makes predictions for multiple documents
    pre: root is the root of a decision tree, columns are the 
    attributes that the decision tree was trained on, and the
    twoDList is a list of data points where the first column of
    each row is None and the rest of the columns correspond to the
    columns used to train the decision tree
    post: returns the same twoDList but the first value of every row
    is filled in with a prediction for that attribute
    """
    for x in twoDList:
        x[0] = predict(root, columns, x)
    return twoDList


def findIndex(val, l):
    """
    helper function for predict that finds the index of a value for a given
    list, returns None if the value is not in the list
    pre: val is any value and l is a list
    post: returns either an integer between 0 and the length of the list 
    that is the index of where val is, or it returns None
    """
    for x in range(len(l)):
        if l[x] == val:
            return x
    return None





def mostFreq(items):
    """
    helper function for makeTree that given a list returns the value that occurs
    the most frequently in the list. 
    pre: items is a list
    post: returns the most freqently occuring value in the list
    """
    dic = {}
    for i in range(len(items)):
        if items[i] in dic:
            dic[items[i]] += 1
        else:
            dic[items[i]] = 1
    maximum = max(dic, key=dic.get)
    return maximum

def maxGain(data):
    """
    helper function for make tree that returns the index of 
    the attribute that has the maximum information gain for
    building the next branch in the ID3 tree
    pre: data is a 2d list where each row is an observation 
    and each column is an attribute, each row is the same
    length
    post: returns and index between 0 and the length of 
    each row that represents the attribute with the 
    maximum information gain
    """
    entropy = 2
    loc = 0
    for x in range(1,len(data[0])):
        items = []
        for y in range(len(data)):
            items.append([data[y][0],data[y][x]])
        ent = calculateEntropy(partition(items))
        if ent < entropy:
            entropy = ent
            loc = x
    return loc

def partition(twoDList):
    """
    helper function for maxGain that creates a 2d list that gets
    passed in to calculate entropy
    pre: a 2D list where each row is an observation and each column 
    is an attribute, the first column of each row is the value for 
    the attribute that we are training the tree for
    post: returns a 2d list that is a list of lists of the values for
    the training attribute broken down by keys from a different attribute
    """
    parts = []
    keys = []
    
    for x in range(len(twoDList)):
        if not (twoDList[x][1] in keys):
            keys.append(twoDList[x][1])
            
    for y in keys:
        l = []
        for x in range(len(twoDList)):
            if twoDList[x][1] == y:
                l.append(twoDList[x][0])
        parts.append(l)
    return parts

def calculateEntropy(partList):
    """
    a helper function for maxGain that takes in a partitioned list
    and returns the entropy of that attribute
    pre: partList is a 2D list, for format see the list that
    partitioned list returns
    post: a number that calculates the total entropy of the 
    attribute used to make the partitioned list.
    """
    totEnt = 0
    totLen = 0
    for x in partList:
        totLen += len(x)
    for x in partList:
        ent = 0
        keys = []
        for y in x:
            if not (y in keys):
                keys.append(y)
        for key in keys:
            count = 0
            for y in x:
                if y == key:
                    count += 1
            length = len(x)
            val = -(count/length)* math.log(count/length,2)
            ent += val
        totEnt += (len(x)/totLen)*ent
    return totEnt


