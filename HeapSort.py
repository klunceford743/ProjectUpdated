"""Katie Lunceford and Jon Li
This file contains the HeapSort class that uses a heap to
sort the top and bottom words from a dictionary. The class
has attributes of self.heap that starts as an empty heap and
self.size that starts at 0.

The class also has methods for maxSort, maxMoveUp, maxChild,
minSort, minMoveUp, and minChild.

There are also helper functions outside of the class which are 
maxHeapRemove, maxFixDown, minHeapRemove, minFixdown, 
leftChildOne, and rightChildOne.
"""



class HeapSort:

    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    # method that uses heap to sort items in a dictionary
    # returns the top n values
    # pre: self.heap[0] should be empty and self.size = 0, 
    # nums is a dictionary where are all the keys are words
    # and the values are integers (counts of those words)
    # n is a postive integer
    # post: returns a list of tuples sorted by the second value
    # of length n
    def maxSort(self, nums, n):
        """
        method that uses heap to sort items in a dictionary
        returns the top n values
        pre: self.heap[0] should be empty and self.size = 0, 
        nums is a dictionary where are all the keys are words
        and the values are integers (counts of those words)
        n is a postive integer
        post: returns a list of tuples sorted by the second value
        of length n, descending order
        """
        i = len(nums)//2
        self.size = len(nums)
        self.heap = [0] + [(k,v) for k,v in nums]
        while i > 0:
            self.maxMoveUp(i)
            i = i - 1

        y = []
        x = 0
        while self.heap != [0] and x < n:
            y.append(maxHeapRemove(self.heap))
            x += 1

        return y

    
    def maxMoveUp(self, i):
        """
        helper method for maxSort that is passed
        an index and moves from that index down the heap
        so that each parent is always larger than its two
        children
        pre: self.heap is not empty and i <= self.size//2
        post: self.heap should be sorted from self.heap[i]
        down
        """
        while i * 2 <= self.size:
            m = self.maxChild(i)
            if self.heap[i][1] < self.heap[m][1]:
                temp = self.heap[i]
                self.heap[i] = self.heap[m]
                self.heap[m] = temp
            i = m

    def maxChild(self, i):
        """
        helper method for maxMoveUp that, given an index,
        finds the child of that index with the maximum value
        pre: i is an integer >0 and <= self.size//2
        post: returns an index <= self.size
        """
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i*2][1] > self.heap[i*2+1][1]:
            return i * 2
        return i* 2 + 1

    
    def minSort(self, nums, n):
        """
        method that uses heap to sort items in a dictionary
        returns the bottom n values
        pre: self.heap[0] should be empty and self.size = 0, 
        nums is a dictionary where are all the keys are words
        and the values are integers (counts of those words)
        n is a postive integer
        post: returns a list of tuples sorted by the second value
        of length n, ascending order
        """
        i = len(nums)//2
        self.size = len(nums)
        self.heap = [0] + [(k,v) for k,v in nums]
        while i > 0:
            self.minMoveUp(i)
            i = i - 1

        y = []
        x = 0
        while self.heap != [0] and x < n:
            y.append(minHeapRemove(self.heap))
            x += 1

        return y

    def minMoveUp(self, i):
        """
        helper method for minSort that is passed
        an index and moves from that index down the heap
        so that each parent is always smaller than its two
        children
        pre: self.heap is not empty and i <= self.size//2
        post: self.heap should be sorted from self.heap[i]
        down
        """
        while i * 2 <= self.size:
            m = self.minChild(i)
            if self.heap[i][1] > self.heap[m][1]:
                temp = self.heap[i]
                self.heap[i] = self.heap[m]
                self.heap[m] = temp
            i = m

    def minChild(self, i):
        """
        helper method for minMoveUp that, given an index,
        finds the child of that index with the minimum value
        pre: i is an integer >0 and <= self.size//2
        post: returns an index <= self.size
        """
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i*2][1] < self.heap[i*2+1][1]:
            return i * 2
        return i* 2 + 1

def maxHeapRemove(heap):
    """
    helper function for maxSort that removes and returns the 
    value at the top of the heap and then re-sorts it so the 
    new maximum is on top
    pre: passes in a sorted maximum heap
    post: returns the maximum value from the heap and the
    heap is now sorted with the new maximum value on top
    """
    top = heap[len(heap)-1]
    m = heap[1]
    heap[1] = top
    heap.pop()
    maxFixdown(heap, 1)
    return m


def maxFixdown(heap, ind):
    """
    helper function for maxHeapRemove that recursively
    re-sorts the heap from a given index
    pre: heap is an unsorted heap and ind is a integer 
    >0 and < len(heap)
    post: heap is now sorted from the index down
    """
    l = leftChildOne(heap, ind)
    r = rightChildOne(heap,ind)
    if l == None:
        return
    if r == None:
        if heap[ind][1] < heap[l][1]:
            temp = heap[l]
            heap[l] = heap[ind]
            heap[ind] = temp
        return
    if heap[ind][1] < max(heap[l][1], heap[r][1]):
        if heap[l][1] >= heap[r][1]:
            temp = heap[l]
            heap[l] = heap[ind]
            heap[ind] = temp
            maxFixdown(heap, l)
        else:
            temp = heap[r]
            heap[r] = heap[ind]
            heap[ind] = temp
            maxFixdown(heap,r)

def minHeapRemove(heap):
    """
    helper function for minSort that removes and returns the 
    value at the top of the heap and then re-sorts it so the 
    new minimum is on top
    pre: passes in a sorted minimum heap
    post: returns the minimum value from the heap and the
    heap is now sorted with the new minimum value on top
    """
    top = heap[len(heap)-1]
    m = heap[1]
    heap[1] = top
    heap.pop()
    minFixdown(heap, 1)
    return m


def minFixdown(heap, ind):
    """
    helper function for minHeapRemove that recursively
    re-sorts the heap from a given index
    pre: heap is an unsorted heap and ind is a integer 
    >0 and < len(heap)
    post: heap is now sorted from the index down
    """
    l = leftChildOne(heap, ind)
    r = rightChildOne(heap,ind)
    if l == None:
        return
    if r == None:
        if heap[ind][1] > heap[l][1]:
            temp = heap[l]
            heap[l] = heap[ind]
            heap[ind] = temp
        return
    if heap[ind][1] > min(heap[l][1], heap[r][1]):
        if heap[l][1] <= heap[r][1]:
            temp = heap[l]
            heap[l] = heap[ind]
            heap[ind] = temp
            minFixdown(heap, l)
        else:
            temp = heap[r]
            heap[r] = heap[ind]
            heap[ind] = temp
            minFixdown(heap,r)

def leftChildOne(tree, index):
    """
    helper function for maxFixdown and minFixdown that
    returns the index of the left child of a given index
    it returns None if the given index does not have a 
    left child
    pre: tree is any tree, index is a positive integer that
    is less than the length of the tree
    post: if it doesn't return None, then child = index*2 and
    is less than the length of the tree
    """
    child = index*2
    if child >= len(tree):
        return None
    return child

def rightChildOne(tree, index):
    """
    helper function for maxFixdown and minFixdown that
    returns the index of the right child of a gien index
    it returns None if the given index does not have a 
    right child
    pre: tree is any tree, index is a positive integer that is
    less than the length of the tree
    post: if it doesn't return None, then the child = index*2+1
    and is less than the length of the tree
    """
    child = index*2 + 1
    if child >= len(tree):
        return None
    return child
