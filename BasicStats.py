""" Katie Lunceford and Jon Li

This is the BasicStats object that is used to generate stats about given
strings. The attributes are a dictionary and a linked list.

There are static methods called createFreqMap and slinkFreq. The other
methods are topN, bottomN, newTopN, topNHeap, and bottomNHeap
"""

import sList as s
import SStack as stack
import HeapSort as h

class BasicStats:

    #the initialization function, the only attribute starts off as a blank
    #dictionary and blank linked list
    def __init__(self):
        self.dic = {}
        self.sl = s.SLink()

    # can be called before an instance is initialized, takes a list of words
    # as an input and returns a dictionary of what words are used as the keys
    # and the frequency with which they're used as the values
    # pre-conditions: wordList is 1D list of words
    # post: returns wordCount, dictionary of individual words as the keys and
    # the values are the number of times they appear in the wordList
    @staticmethod
    def createFreqMap(wordList):
        wordCount = {}
        for i in range(len(wordList)):
            #checks if the word is already in the dictionary, if it is it
            #adds one to the value, if it is not it adds it to the dictionary
            #with an initial value of 0
            word = wordList[i]
            if not word[-1].isalpha():
                word = word[:-1]
            if word in wordCount:
                wordCount[word] += 1
            elif wordList[i].isalpha():
                wordCount[word] = 1
        return wordCount
    """
    The number of operations in this method is n, where n is the length
    of wordList. The theta notation of this is also n.
    """

    # takes a list of words as a dictionary and returns a singularly
    # linked list
    # pre: wordList is a 1D list of words
    # post: wordCount is a linked list and the data in each is a
    # python list that contains the word and the count [word, count]
    @staticmethod
    def slinkFreq(wordList):
        wordCount = s.SLink()
        for i in wordList:
            runner = wordCount.head
            while runner is not None and runner.data[0] != i:
                runner = runner.next
            if runner is None:
                wordCount.insert([i,1])
            else:
                num = runner.data[1] + 1
                runner.data = [i,num]
        return wordCount
    """ The number of operations in this method is n* the sum from i = 1 to n
    where n is the length of wordList because each time the linked list can
    potentially grow by one, in which case there will be another operation
    on the inside loop. The theta notation of this is n^2 """
                

    # uses the dictionary stored in self, and inputs a number, then outputs
    # a dictionary of just the top n most frequently used words
    # pre: self.dic must be non-empty and n is an integer > 0
    # post: returns a dictionary of the n words used the most times, with
    # the keys as the words and the values as the count
    def topN(self, n):
        top = {}
        #creates a list of n 0s
        topNums = [0 for x in range(n)]
        for key in self.dic:
            #if the value in the dic is greater than the smallest number in
            #topNums, then it replaces that value
            if self.dic[key] > topNums[0]:
                topNums[0] = self.dic[key]
            #sorts the top numbers so the smallest value is first
            topNums.sort()

        #iterates through the dictionary and if the value matches one of the
        #top n most frequently used numbers, then it adds that to a new
        #dictionary that only stores the most frequently used words
        for key in self.dic:
            if self.dic[key] in topNums:
                top[key] = self.dic[key]
                
                #if the word is used the least number of times that would
                #qualify it to be in the top list, then the first value of
                #topNums is deleted so we don't end up with more than n words
                if self.dic[key] == topNums[0]:
                    del topNums[0]
        return top
    """
    The number of operations in this method is 2n, where n is the
    length of self.dic. The theta notation of this is just n.
    """

    # a method similar to topN that uses the dictionary stored in self, and
    # inputs a number, then outputs a dictionary of just the bottom n most
    # frequently used words
    # pre: self.dic myst be non-empty and n is an integer > 0
    # post: returns a dictionary of the n words used the least times, with
    # the keys as the words and the values as the count
    def bottomN(self, n):
        bottom = {}
        #creates a list of n 0s
        bottomNums = [0 for x in range(n)]
        for key in self.dic:
            #if the smallest value is 0 that automatically gets replaced
            if bottomNums[0] == 0:
                bottomNums[0] = self.dic[key]
                
            #if there are no zeros then it checks if the value is smaller
            #than the largest number in the list, and if it is then it
            #replaces that number
            elif self.dic[key] < bottomNums[-1] and key.isalpha():
                bottomNums[-1] = self.dic[key]
            #bottomNums is sorted each time
            bottomNums.sort()

        #iterates through the dictionary and if the value matches one of the
        #bottom n least frequently used numbers, then it adds that to a new
        #dictionary that only stores the least frequently used words
        for key in self.dic:
            if self.dic[key] in bottomNums:
                bottom[key] = self.dic[key]

                #if the word is used the most number of times that it would
                #qualify for the bottom list, then the last value of bottomNums
                #is deleted so we don't end up with more than n words
                if self.dic[key] == bottomNums[-1]:
                    del bottomNums[-1]            
        return bottom

    """
    Yes, it would be faster to do this at the same time. Because both methods
    are using the same loops, if we put this in one method, then we would only
    have to go through each loop once and create both lists topNums and
    bottomNums at the same time.
    """

    # method that uses the linked list instead of the dictionary to find the
    # top n most frequently used words
    # pre: self.sl is not empty and n is an integer > 0
    # post: returns a linked list of size n with the top words, in order
    def newTopN(self,n):
        top = stack.SStack()
        for i in range(n):
            top.push(['', -1])
        for word in self.sl:
            runner = top.st.head
            prev = None
            while runner is not None and word[1] > runner.data[1]:
                prev = runner
                runner = runner.next
            if runner != top.st.head and word[0].isalpha():
                newNode = s.Node(word)
                prev.next = newNode
                newNode.next = runner
                top.pop()

        return top
    
    # method that uses a max heap to find the top n most frequently used words.
    # uses self.dic to generate the heap
    # pre: self.dic is not empty and n is an integer greater than 0
    # post: returns a sorted python list of size n in descending order, 2D list of
    # [word, count]
    def topNHeap(self, n):
        heap = h.HeapSort()
        x = heap.maxSort(self.dic.items(), n)
        return x
    """ The number of operations in this is (in the worst case scenario 2n).
    See analysis of HeapSort on homework 6. This is O(n).
    """
    
    # method that uses a min heap to find the bottom n least frequently used
    # words. uses self.dic to generate the heap
    # pre: self.dic is not empty and n is an integer greater than 0
    # post: returns a sorted python list in increasing order, 2D list of
    # [word,count]
    def bottomNHeap(self,n):
        heap = h.HeapSort()
        x = heap.minSort(self.dic.items(), n)
        return x







    
                
