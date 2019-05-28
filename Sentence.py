"""Katie Lunceford//Jon Li
This is the Sentence object. It stores a string that represents a sentence with
punctuation. The attributes are string (the string of the sentence), wordCount
(the number of words in the sentence), charCount (the number of characters in
the sentence), and puncuation (the punctuation that the sentence ends with).
The methods are parseWords and parseChar.
"""

class Sentence:

    #the initialization function, it takes a single sentence string
    def __init__(self, string):
        self.string = string
        self.wordCount = len(self.string.split())
        self.charCount = len(self.string)
        self.punctuation = self.string[-1]

    #returns a list of all of the words in the sentence, using the split
    #method
    def parseWords(self):
        '''parses the document's words, which means the document is prepared for other operations by being split '''
        return self.string.split()

    #returns a list of all of the characters in the sentence, using a loop
    #through the string
    def parseChar(self):
        '''parses through the characters in each of the words that were parsed.'''
        characters = []
        for char in self.string:
            characters.append(char)
        return characters
