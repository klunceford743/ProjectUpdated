"""Katie Lunceford and Jon Li

This is the DocumentStreamError object that is an exception used to catch any
errors that appear while using the DocumentStreamObject.
"""

class DocumentStreamError(Exception):

    def __init__(self, data):
        self.data = data

