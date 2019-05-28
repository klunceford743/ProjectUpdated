"""Katie Lunceford and Jon Li

This file contains three classes. The main class is SLink that is 
supported by Node and SLinkIterator.

SLink has methods insert, __len__, remove, search, delAll, and __iter__.

Node only has an initialization method that has optional variables for
data and next_node. If left blank, data is an empty list and next_node 
is None.

SLinkIterator is the iterator for SLink that moves through the nodes 
by moving to the self.runner.next and returns the data from each node.

"""


class SLink(object):
    
    def __init__(self, head = None):
        """
        Initialization for SLink,  optional variable for head, which 
        should be a node, if not given then head is None
        """
        self.head = head

    def insert(self, data):
        """
        given data, inserts it to the front of the linked list
        pre: data should be a list
        post: a node containing the data is now the head of the
        list and the next node is the previous head
        """
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def __len__(self):
        """
        returns the number of nodes in the linked list
        pre: the list is contained of nodes
        post: c is an integer >= 0
        """
        runner = self.head
        c = 0 # c is the count 
        while runner is not None:
            c+=1
            runner = runner.next
        return c 

    def remove(self, word):
        """
        passed in a word and removes it from the linked list
        pre: the linked list is made of nodes, the data in each
        node is a list
        post: if the word is not in the data any of the nodes then
        it does nothing and prints a statement saying that the data
        is not in the list, otherwise, it removes the node that contains
        that word in its data from the linked list
        """
        prev = None
        runner = self.head
        while runner is not None and runner.data[0] != word:
            prev = runner
            runner = runner.next
        if runner is None:
            return 'The data is not in the list'
        if runner == self.head:
            self.head = runner.next
            del runner
        else:
            prev.next = runner.next
            del runner

    def search(self, word):
        """
        searches the linked list to see if the word is the
        first value of the data of any of the nodes in the 
        list
        pre: the linked list must be made of nodes and the data
        in each node must be a list
        post: returns True if the word is in the data of any of
        the nodes in the linked list and False otherwise
        """
        runner = self.head
        state = False
        while runner is not None:
            if runner.data[0] == word:
                state = True
                break
            runner = runner.next
        return state

    def delAll(self):
        """
        deletes all of the nodes in the linked list
        pre: the linked list is either None or made 
        up of nodes
        post: self.head = None
        """
        runner = self.head
        while runner is not None:
            temp = runner
            runner = runner.next
            del temp
        self.head = None

    def __iter__(self):
        """
        calls the SLinkIterator class to iterate through
        a linked list
        """
        return SLinkIterator(self.head)
                
class Node(object):
    def __init__(self,data = [], next_node = None):
        self.data = data
        self.next = next_node

class SLinkIterator:
    def __init__(self, head):
        self.runner = head
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.runner == None:
            raise StopIteration
        else:
            item = self.runner.data
            self.runner = self.runner.next
            return item

    
        
