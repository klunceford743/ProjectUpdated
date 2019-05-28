"""Katie Lunceford and Jon Li
This is the DocumentStream object. The attributes are fileName, sents, title, and author

The methods are readWhole, writeWhole, and titleInfo.
"""
import Sentence as s
import DocumentStreamError as d

class DocumentStream:

    #the initialization function, takes fileName as an optional input, if
    #file name is left blank then it just holds an empty string
    def __init__(self, fileName = ''):
        self.fileName = fileName
        self.sents = []
        self.title = ""
        self.author = ""

    #a method that will return a list of all of the sentences in the file
    def readWhole(self):
        try:
            #raises a DocumentStreamError if the file does not exist or it
            #can't find it
            file = open(self.fileName, 'r')
        except:
            raise d.DocumentStreamError('File not found')

        #reads the whole file and stores it in text
        text = file.read()
        punctuation = ['.', '!', '?', ';']
        string = ''
        listSent = []
        i = 0

        #loops through the text and adds each character to a string,
        #if the character is in the punctuation list, or the next two
        #characters are breaks, then it adds the string to the list of
        #sentences and sets the string back to empty
        while i < len(text):
            string += text[i]
            if text[i] in punctuation:
                listSent.append(s.Sentence(string))
                string = ''
            elif i > 1 and text[i] == '\n' and text[i-1] == '\n':
                listSent.append(s.Sentence(string))
                string = ''
            #adds the last sentence to the list
            elif i == len(text) - 1:
                listSent.append(s.Sentence(string))
                break
            i += 1

        return listSent

    #a method that prints out the text with one sentence per line
    def writeWhole(self):
        if self.sents == []:
            self.sents = self.readWhole()
        
        for i in self.sents:
            #a statement that keeps track of whether or not the sentence is
            #blank, if it is then it won't be printed
            sentBlank = True
            for char in range(len(i.string)):
                if not i.string[char].isspace():
                    #if the character is not a space then the sentence isn't
                    #blank
                    sentBlank = False
                elif i.string[char] == '\n':
                    #if the character is a line break then it changes it to
                    #a space
                    i.string = i.string[:char] + ' ' + i.string[char + 1:]
            #prints the sentence if it is not blank
            if not sentBlank:
                print(i.string)

    #for books from the project Gutenberg, finds the title and author
    #information, then adds that to self.title and self.author, and
    #deletes the opening information from the list of sentences
    def titleInfo(self):
        
        #if self.sents is blank then reads the sentences in
        if self.sents == []:
            self.sents = self.readWhole()

        #checks that the project is from Project Gutenberg
        if self.sents[0].string[:21] != 'The Project Gutenberg':
            return
        #if it is from Project Gutenberg it finds the title, author, and
        #strips the introductory information from the list of sentences
        else:
            index = 0
            for i in self.sents:
                if i.string[:7] == 'Title: ':
                    self.title = i.string[7:-2]
                elif i.string[:8] == 'Author: ':
                    self.author = i.string[8:-2]
                elif i.string[:25] == '*** START OF THIS PROJECT':
                    self.sents = self.sents[index + 1:]
                index += 1
            return
