from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, LabelFrame
from TextFilter import *
from tkinter import *
import Doc as d
import SKTree as t
import datafunctions as f
import tree as tr
import SKPCA as p

class GUI:

    def __init__(self, master):
        '''The init is where the phsysical layout of the GUI is. Has all the labels,textboxes, buttons, and entry-points
           All the buttons have commands attached to them that are called.'''
        self.master = master
        master.title("CSCI Final Project")
        self.file = None
        self.fileL = []
        self.filtL = []
        self.prediction = None
        self.master.minsize(width=350,height=700)
        self.author = None
        self.genre = None
        self.year = None
        self.entered_file = ''
        self.statMethod = 0
        self.skGenre = None
        self.skYear = None
        self.skTop = None
        self.skBottom = None
        self.idGenre = None
        self.idYear = None
        self.idTop = None
        self.idBottom = None

# message Label Text Stuff

        self.workingLabel = Label(master ,text = "File to Edit: ")
        
# Entry box storage section

        vcmd = master.register(self.validate)
        vcmd2 = master.register(self.validateGenre)
        vcmd3 = master.register(self.validateYear)
        vcmd4 = master.register(self.validateAuthor)
        self.entry = Entry(master, validate="key",validatecommand=(vcmd, '%P'))
                        
# Buttons and input boxes declaration
        self.add_document = Button(master, text="Add Document", command=lambda: self.update("add"))
        self.label1 = Label(master, text= "Document Name: ")

        self.fileEntry = Entry(master,validate='key',validatecommand = (vcmd, '%P'),bd=3)
        

        self.filter0 = Button(master, text= "Normalize White Space", command=lambda: self.applyFilter("nw"))       
        self.filter1 = Button(master, text= "Normalize Case", command=lambda: self.applyFilter("nc"))        
        self.filter2 = Button(master, text= "Strip Null", command=lambda: self.applyFilter("sn"))                                                                                         
        self.filter3 = Button(master, text= "Strip Numbers", command=lambda: self.applyFilter("snum"))
        self.filter4 = Button(master, text= "Strip Common Words", command=lambda: self.applyFilter("common"))
        self.appFilter = Button(master, text= "APPLY FILTERS", command=lambda: self.applyFilter("apply filters"))

        self.addInfo = Label(master,text = "-----------Add Info--------------")
        self.addInfo.grid(row=3,column=1,stick=W+E)
        self.GenreButt = Label(master, text = 'Enter Genre: ')
        self.GenreEnt = Entry(master, validate='key',validatecommand = (vcmd2, '%P'),bd=3)       
        self.YearButt = Label(master,  text = 'Enter Year: ')
        self.YearEnt = Entry(master,validate='key',validatecommand = (vcmd3, '%P'), bd=3)                                                                                      
        self.AuthorButt = Label(master, text = 'Enter Author: ')
        self.AuthorEnt = Entry(master, validate='key',validatecommand = (vcmd4, '%P'), bd=3)

        self.filtlab = Label(master,text="------------Filters------------")
        self.filtlab.grid(row=7,column=1)
                             
        self.trainsection = Label(master,text="--------Training----------")
        self.trainsection.grid(row=14,column=1,stick=W+E)
        self.statmethod1 = Button(master,text = "Sk Tree Genre",command = lambda: self.chooseStat('1'))
        self.statmethod2 = Button(master,text = "Sk Tree Year",command = lambda: self.chooseStat('2'))
        self.statmethod3 = Button(master,text = "ID3 Genre",command = lambda: self.chooseStat('3'))
        self.statmethod4 = Button(master,text = "ID3 Year ",command = lambda: self.chooseStat('4'))
        self.statmethod5 = Button(master,text = "SK Top Words",command = lambda: self.chooseStat('5'))
        self.statmethod6 = Button(master,text = "SK Bottom Words",command = lambda: self.chooseStat('6'))
        self.statmethod7 = Button(master,text = "ID3 Top Words",command = lambda: self.chooseStat('7'))
        self.statmethod8 = Button(master,text = "ID3 Bottom Words",command = lambda: self.chooseStat('8'))
        self.statmethod9 = Button(master,text = "SK PCA",command = lambda: self.chooseStat('9'))
        
        self.trainButton = Button(master,text = "TRAIN", command = lambda: self.training(),bd = 3)

        self.PredictButton = Button(master,text="Predict Document",bd=5,command = lambda:self.predict())
        self.predictEntry = Entry(master)

        self.master.bind('<Return>',lambda event:self.update("enter"))
                           
#Layout and grid
        self.label1.grid(row=1,column=0,columnspan=2,stick=W+E)
        self.fileEntry.grid(row=1,column = 2, columnspan = 2,stick=W+E)

        self.add_document.grid(row=6,column=3,stick=W+E)
        self.filter0.grid(row=8,column=1,stick=W+E)
        self.filter1.grid(row=9,column=1,stick=W+E)
        self.filter2.grid(row=10,column=1,stick=W+E)
        self.filter3.grid(row=11,column=1,stick=W+E)
        self.filter4.grid(row=12,column=1,stick=W+E)
        self.appFilter.grid(row=13,column=1,stick=W+E)

        self.GenreButt.grid(row = 4,column=1,stick=W+E)
        self.GenreEnt.grid(row=4, column =2,stick = W+E)
        self.AuthorButt.grid(row = 5,column=1,stick=W+E)
        self.AuthorEnt.grid(row=5, column =2,stick = W+E)
        self.YearButt.grid(row = 6,column=1,stick=W+E)
        self.YearEnt.grid(row=6, column =2,stick = W+E)

        self.statmethod1.grid(row=15,column =1, stick = W+E)
        self.statmethod2.grid(row=15,column =2, stick = W+E)
        self.statmethod3.grid(row=16,column =1, stick = W+E)
        self.statmethod4.grid(row=16,column =2, stick = W+E)
        self.statmethod5.grid(row=17,column =1, stick = W+E)
        self.statmethod6.grid(row=17,column =2, stick = W+E)
        self.statmethod7.grid(row=18,column =1, stick = W+E)
        self.statmethod8.grid(row=18,column =2, stick = W+E)
        self.statmethod9.grid(row=19,column =1, stick = W+E)
        self.trainButton.grid(row=19,column=2,stick=W+E)

        self.predictgenrelabel = Label(master, text = "Genre of Predicted: ")
        self.predictfileLabel = Label(master,text = "File to Predicted: ")
        self.predictyearLabel = Label (master,text = "Year of Predict: ")
        self.predictfileEntry = Entry(master, validate='key',validatecommand = (vcmd, '%P'))
        self.predictgenreEntry = Entry(master, validate='key',validatecommand = (vcmd2, '%P'))
        self.predictyearEntry = Entry(master,validate='key',validatecommand = (vcmd3, '%P'),bd=3)

        self.predictgenrelabel.grid(row=20,column=2,stick=W+E)
        self.predictfileLabel.grid(row=20,column=1,stick=W+E)
        self.predictfileEntry.grid(row=21,column=1,stick=W+E)
        self.predictgenreEntry.grid(row=21,column=2,stick=W+E)
        self.predictyearLabel.grid(row=20,column=3,stick=W+E)
        
        self.PredictButton.grid(row=22,column=1,stick=W+E)
        self.predictyearEntry.grid(row=21,column=3,stick=W+E)


        self.Documents = Label(master,text="Title                   Genre              Author       Year")
        self.Documents.grid(row=24,column=1)
        
        self.text = Text(master)
        self.text.grid(row=25,column=1)
        
    def validate(self, new_text):
        '''Validates the entered text to make sure it is words'''
        if not new_text: # the field is being cleared
            self.entered_file= ''
            return True

        try:
            self.entered_file = str(new_text)                                                                                
            return True
        except ValueError:
            return False

    def validateGenre(self,newtext):
        '''makes sure the entered text is text'''
        if not newtext:
            self.genre = None
            return True
        try:
            self.genre = str(newtext)
            return True
        except ValueError:
            return False

    def validateAuthor(self,newtext):
        '''makes sure author label is text'''
        if not newtext:
            self.author = None
            return True
        try:
            self.author = str(newtext)
            return True
        except ValueError:
            return False

    def validateYear(self,newtext):
        '''makes sure the entered value is a valid year'''
        if not newtext:
            self.year = 0
            return True
        try:
            self.year = str(newtext)
            return True
        except ValueError:
            return False

    def addInfo(self,infotype):
        '''adds the information for each file'''
        if infotype == 'genre':
            self.newFile.genre = self.genre
        if infotype == 'year':
            self.newFile.year = self.year
        if infotype == 'author':
            self.newFile.author = self.author

    def applyFilter(self,method):
        '''Adds filter to list of filter methods if the button pressed is not "Apply Filter". If the button is Apply Filter,
            then the list of filters will subsequently be applied to the documents.'''
        if method == "apply filters":
            for doc in self.fileL:
                newtext = TextFilter(doc.fileName, self.filtL)
                newtext.apply()
                doc.doc = newtext.doc
        else:
            if method not in self.filtL:
                self.filtL.append(str(method))
                
    def applyPredFilt(self,file):
        newtext = TextFilter(file.fileName, self.filtL)
        newtext.apply()
        file.doc = newtext.doc
        return file
                
    def chooseStat(self,method):
        '''applies the Stat Method'''
        self.statMethod = method

    def training(self):
        '''applies the statistical method for training that the user has clicked on to the documents that were passed'''
        if self.statMethod == '1':
            self.skGenre = f.trainGenre(self.fileL)
        elif self.statMethod == '2':
            self.skYear = f.trainYear(self.fileL)
        elif self.statMethod == '3':
            self.idGenre = f.trainGenreID(self.fileL)
        elif self.statMethod == '4':
            self.idYear = f.trainYearID(self.fileL)
        elif self.statMethod == '5':
            self.skTop = f.trainTop(self.fileL)
        elif self.statMethod == '6':
            self.skBottom = f.trainBottom(self.fileL)
        elif self.statMethod == '7':
            self.idTop = f.trainTopID(self.fileL)
        elif self.statMethod == '8':
            self.idBottom = f.trainBottomID(self.fileL)
        elif self.statMethod == '9':
            data, labels = f.dataPCA(self.fileL)
            self.pca = p.SKPCA()
            self.pca.train(data, labels, 2)
    

    def predict(self):
        '''calls all the methods for each button that corresponds to a prediction method'''
        file = d.Document(self.entered_file)
        file.genre = self.genre
        file.year = self.year
        if self.statMethod == '1':
            data = [[None, f.assignGenre(file)]]
            pred = self.skGenre.eval(data)
        elif self.statMethod == '2':
            data = [[None, f.assignYear(file)]]
            pred = self.skYear.eval(data)
        elif self.statMethod == '3':
            data = [[None, f.assignGenre(file)]]
            pred = self.idGenre.evaluate(data)[0]
        elif self.statMethod == '4':
            data = [[None, f.assignYear(file)]]
            pred = self.idYear.evaluate(data)[0]
        elif self.statMethod == '5':
            data = f.predData(file, self.skTop.labels)
            pred = self.skTop.eval(data)
        elif self.statMethod == '6':
            data = f.predData(file, self.skBottom.labels)
            pred = self.skBottom.eval(data)
        elif self.statMethod == '7':
            data = f.predData(file, self.idTop.columns)
            pred = self.idTop.evaluate(data)[0]
        elif self.statMethod == '8':
            data = f.predData(file, self.idBottom.columns)
            pred = self.idBottom.evaluate(data)[0]
        elif self.statMethod == '9':
            newfile = self.applyPredFilt(file)
            data = f.predPCA(newfile, self.pca.labels)
            ind = self.pca.eval(data)
            pred = [self.fileL[ind].author]
        self.prediction = pred[0]
        print('The predicted author is: ' + str(self.prediction))
        file.author = pred[0]
        self.fileL.append(file)
        self.text.insert(INSERT,' '*10 + str(file.fileName) + ' '*5 + str(file.genre) + ' '*5 + str(file.author) + ' '*5 + str(file.year) + '\n')
        self.predictfileEntry.delete(0,END)
        self.predictyearEntry.delete(0,END)
        self.predictgenreEntry.delete(0,END)

        

            
                    

    def update(self, method):
        '''This method appends and prepares the file doc entered along with entered attributes
           and then writes in the information into a text box at the bottom. '''
        if method == "add":
            file = d.Document(self.entered_file)
            file.author = self.author
            file.genre = self.genre
            file.year = self.year
            self.fileL.append(file)
            self.text.insert(INSERT,' '*10 + str(file.fileName) + ' '*5 + str(file.genre) + ' '*5 + str(file.author) + ' '*5 + str(file.year) + '\n')
 # Makes all the entries blank                                                
        self.fileEntry.delete(0,END)
        self.AuthorEnt.delete(0,END)
        self.YearEnt.delete(0,END)
        self.GenreEnt.delete(0,END)

#runs the GUI
root = Tk()
my_gui = GUI(root)
root.mainloop()
