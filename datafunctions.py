""" Katie Lunceford and Jon Li
Data functions for formatting data to be passed into authorship attribution
programs.

The functions in this file are dataGenre, assignGenre, dataYear, assignYear, dataTop,
dataBottom, predData, trainGenre, trainYear, trainTop, trainBottom, trainGenreID,
trainYearID, trainTopID, trainBottomID, dataPCA, and predPCA.
"""
import BasicStats as b
import Doc as d
import SKTree as t
import tree as tr

# creates the data that gets passed into trees built based on genre
# pre: enters in a list of documents
# post: returns the data which is a 2d list that starts with the
# author and the second column is the genre code, the labels are
# ['author','genre']
def dataGenre(documents):
    data = []
    labels = ['author', 'genre']
    for doc in documents:
        data.append([doc.author, assignGenre(doc)])
    return data, labels

# method that assigns a genre based on a few categories
# pre: input is a document object
# post: returns a number 0-5 based on the document's genre
def assignGenre(doc):
    if doc.genre == 'short story':
        return 0
    elif doc.genre == 'fiction':
        return 1
    elif doc.genre == 'science fiction':
        return 2
    elif doc.genre == 'horror':
        return 3
    elif doc.genre == 'poem':
        return 4
    else:
        return 5

# creates the data that gets passed into trees built based on year
# pre: enters in a list of documents
# post: returns the data which is a 2d list that starts with the
# author and the second column is the year code, the labels are
# ['author','year']
def dataYear(documents):
    data = []
    labels = ['author', 'year']
    for doc in documents:
        data.append([doc.author, assignYear(doc)])
    return data, labels


# method that assigns a genre based on a few categories
# pre: input is a document object
# post: returns a number 0-2 based on the document's year
def assignYear(doc):
    if int(doc.year) < 1850:
        return 0
    elif int(doc.year) < 1900:
        return 1
    else:
        return 2


# creates the data that gets passed into trees built based on
# the top 10 words across all documents
# pre: a list of documents
# post: returns the data which is a 2d list that starts with the
# authors of each document and with the columns being 1 if the
# word from the corresponding label is in the document and 0
# otherwise, the labels are ['author'] followed by the top 10
# words across all the documents
def dataTop(documents):
    data = []
    labels = ['author']
    words = []
    for doc in documents:
        doc.generateWhole()
        for sent in doc.getSentences():
            w = [x.lower() for x in sent.string.split()]
            words += w
    stats = b.BasicStats()
    stats.dic = b.BasicStats.createFreqMap(words)
    top = stats.topNHeap(100)
    for x in top:
        labels.append(x[0])
    for doc in documents:
        words = []
        info = [doc.author]
        for sent in doc.getSentences():
            w = [y.lower() for y in sent.string.split()]
            words += w
        for x in labels[1:]:
            if x in words:
                info.append(1)
            else:
                info.append(0)
        data.append(info)
    return data, labels


# creates the data that gets passed into trees built based on the
# bottom 10 words across all documents
# pre: a list of documents
# post: returns the data which is a 2d list that starts with the
# authors of each document and with the columns being 1 if the word
# from the corresponding label is in the document and 0 otherwise,
# the labels are ['author'] followed by the top 10 words across all
# the documents
def dataBottom(documents):
    data = []
    labels = ['author']
    words = []
    for doc in documents:
        doc.generateWhole()
        for sent in doc.getSentences():
            w = [x.lower() for x in sent.string.split()]
            words += w
    stats = b.BasicStats()
    stats.dic = b.BasicStats.createFreqMap(words)
    bottom = stats.bottomNHeap(10)
    for x in bottom:
        labels.append(x[0])
    for doc in documents:
        words = []
        info = [doc.author]
        for sent in doc.getSentences():
            w = [y.lower() for y in sent.string.split()]
            words += w
        for x in labels[1:]:
            if x in words:
                info.append(1)
            else:
                info.append(0)
        data.append(info)
    return data, labels

# given labels and a document it creates the data needed to pass
# into a prediction for either a top 10 tree or a bottom 10 tree
# pre: takes in a document and a set of labels
# post: outputs a 2d list with one row that has corresponding
# 0s and 1s for whether or not each word from the labels is in
# the document
def predData(doc, labels):
    data = [[None]]
    doc.generateWhole()
    words = []
    for sent in doc.getSentences():
        w = [x.lower() for x in sent.string.split()]
        words += w
    for i in range(len(words)):
        if not words[i][-1].isalpha():
            words[i] = words[i][:-1]
    for x in labels[1:]:
        if x in words:
            data[0].append(1)
        else:
            data[0].append(0)

    return data

# called to train an SKTree based on genre
# pre: takes in a list of documents with known authors
# post: outputs an SKTree
def trainGenre(documents):
    data, labels = dataGenre(documents)
    s = t.SKTree()
    s.train(data, labels, 10)
    return s

# called to train an SKTree based on year
# pre: takes in a list of documents with known authors
# post: outputs an SKTree
def trainYear(documents):
    data, labels = dataYear(documents)
    s = t.SKTree()
    s.train(data, labels, 10)
    return s

# called to train an SKTree based on the top 10 words
# pre: takes in a list of documents with known authors
# post: outputs an SKTree
def trainTop(documents):
    data, labels = dataTop(documents)
    s = t.SKTree()
    s.train(data,labels,100)
    return s

# called to train an SKTree based on the bottom 10 words
# pre: takes in a list of documents with known authors
# post: outputs an SKTree
def trainBottom(documents):
    data, labels = dataBottom(documents)
    s = t.SKTree()
    s.train(data, labels, 30)
    return s

# called to train an ID3 tree based on genre
# pre: takes in a list of documents with known authors
# post: outputs an ID3 tree
def trainGenreID(documents):
    data, labels = dataGenre(documents)
    s = tr.DecisionTree()
    s.train(data, labels, 10)
    return s

# called to train an ID3 tree based on year
# pre: takes in a list of documents with known authors
# post: outputs an ID3 tree
def trainYearID(documents):
    data, labels = dataYear(documents)
    s = tr.DecisionTree()
    s.train(data, labels, 10)
    return s

# called to train an ID3 based on top 10 words
# pre: takes in a list of documents with known authors
# post: outputs an ID3 tree
def trainTopID(documents):
    data, labels = dataTop(documents)
    s = tr.DecisionTree()
    s.train(data, labels, 30)
    return s

# called to train an ID3 tree based on bottom 10 words
# pre: takes in a list of documents with known authors
# post: outputs an ID3 tree
def trainBottomID(documents):
    data, labels = dataBottom(documents)
    s = tr.DecisionTree()
    s.train(data, labels, 30)
    return s

# data processing method for PCA
# pre: takes in a list of documents with known authors
# post: outputs data which is a 2d list where the rows
# are documents with the ratio of the top words in each
# document and labels is a list of the top words
def dataPCA(documents):
    data = []
    labels = ['author']
    words = []
    for doc in documents:
        data.append([doc.author])
        doc.generateWhole()
        for sent in doc.getSentences():
            w = [x.lower() for x in sent.string.split()]
            words += w
    stats = b.BasicStats()
    stats.dic = b.BasicStats.createFreqMap(words)
    top = stats.topNHeap(100)
    for x in top:
        labels.append(x[0])
    for i in range(len(documents)):
        wCount = documents[i].getWordCnt()
        words = []
        for sent in documents[i].getSentences():
            w = [y.lower() for y in sent.string.split()]
            words += w
        for l in labels[1:]:
            cnt = 0
            for w in words:
                if w == l:
                    cnt += 1
            ratio = cnt/wCount
            data[i].append(ratio)
    return data, labels

# data processing method for PCA
# pre: takes in a document with an unknown author and a
# list of labels used to train a PCA
# post: outputs data, a 2d list with one row that has the
# ratio of the words from the labels in the document
def predPCA(doc, labels):
    data = [[None]]
    doc.generateWhole()
    wCount = doc.getWordCnt()
    words = []
    for sent in doc.getSentences():
        w = [y.lower() for y in sent.string.split()]
        words += w
    for l in labels[1:]:
        cnt = 0
        for w in words:
            if w == l:
                cnt += 1
        ratio = cnt/wCount
        data[0].append(ratio)
    return data


