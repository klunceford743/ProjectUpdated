""" Katie Lunceford//Jon Li
a simple stack using linked list to be used later on
"""

import sList as link

class SStack:

    def __init__(self):
        '''establishes the linked list'''
        self.st = link.SLink()
        self.size = 0

    def push(self, val):
        '''pushes the val into the stack'''
        self.st.insert(val)
        self.size += 1

    def pop(self):
        '''removes the top of the stack and returns the value of that'''
        if self.st.head is None:
            return None
        val = self.st.head.data
        self.st.head = self.st.head.next
        self.size -= 1
        return val

    def __len__(self):
        return self.size
