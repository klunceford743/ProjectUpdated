""" Katie Lunceford
This is the main function. It asks for a user input file, converts this
file into a Document object and uses the text in this Document to create
a scatter plot of the top 10 most frequently used words in the document.

This was used for the checkpoints and is not implemented in the final
project. The most recently that it was used was to test the different 
running times between the topN using a dictionary and the topN using
a heap. Old code used for the command line plotter is commented out
"""

import Doc as d
import BasicStats as b
import CommandLinePlot as c
import DocumentStreamError as ds
import time


def main():

    file = input('Please enter a file: ' )
    try:
        #converts the file into a document object
        doc = d.Document(file)
        doc.generateWhole()
    
        words = []
        #makes a new list of all of the words in the file, removing any
        #punctuation and making everything lowercase, so that they will
        #all be counted as the same word
        for sent in doc.getSentences():
            if not sent.string[-1].isalpha():
                s = sent.string[:-1]
            else:
                s = sent.string
            w = [x.lower() for x in s.split()]
            words += w

        #uses the BasicStats object to create a dictionary of the
        #top 10 words used in the document
        """
        stats = b.BasicStats()
        stats.dic = b.BasicStats.createFreqMap(words)
        stats.sl = b.BasicStats.slinkFreq(words)
        stats.listFreq()
        top1 = stats.topN(10)
        print(top1)
        top2 = stats.newTopN(10)
        for i in range(10):
            print(top2.pop())
            
        top3 = stats.topNHeap(10)
        print(top3)

        bottom1 = stats.bottomN(10)
        print(bottom1)
        bottom2 = stats.bottomNHeap(10)
        print(bottom2)
        """

        stats = b.BasicStats()
        start1 = time.time()
        stats.dic = b.BasicStats.createFreqMap(words)
        top1 = stats.topN(100)
        end1 = time.time()
        print('Dictionary: {0:.5f} us.' .format( end1 - start1 ))
        """ The run time of this is n + 2m where n is the number of
words in the document and m is the length of the dictionary.
createFreqMap has a run time of n and topN has a runtime of 2m. m <= n
so n+2m =< 3n. Therefore, this is O(n).
"""

        start2 = time.time()
        stats.dic = b.BasicStats.createFreqMap(words)
        top2 = stats.topNHeap(100)
        end2 = time.time()
        print('Heap: {0:.5f} us.' .format( end2 - start2 ))
        """ The run time of this is n + 2m where n is the number of
words in the document and m is the length of the dictionary. createFreqMap has
a run time of n and topNHeap has a runtime of 2m.
m <= n, so n+2m =< 3n. Therefore, this is O(n). On average, we would still
expect the heap to perform faster than the dictionary."""

        
        
        """
        #makes a list of the number of times each of the top 10 words is used
        num = []
        for key in top:
            num.append(top[key])

        #makes a scatter plot using the number of time the top 10 words are used
        #as the y axis and the rank of those words (most to 10th most, along
        #along the x axis
        num.sort(reverse = True)
        plt = c.CommandLinePlotter()
        plt.twoDScatter(num)
        plt.barGraph(num)

        #makes a list of tuples of the words and their length
        wordList = []
        for key in top:
            wordList.append((key, top[key]))
        wordList.sort(key= lambda tup: tup[1], reverse = True)

        #prints the list of tuples as a key to know which word was the most
        #used to which was the 10th most used
        for i in range(len(wordList)):
            print('Word', i +1, wordList[i][0], end = '; ')"""

    #handles any exceptions that might occur from the DocumentStream class
    except ds.DocumentStreamError as E:
        print(E.data)
    
main()
