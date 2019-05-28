"""Katie Lunceford and Jon Li

The CommandLinePlotter object that will be used to generate scatter plots. The only
attribute is the plot which holds a twoD array that will show axis and the points on the
scatter plot.

It's methods are generatePlane and twoDScatter and barGraph
"""

import string as s
import random

class CommandLinePlotter:
    
    #the initialization method starts off with a blank plot.
    def __init__(self):
        self.plot = []

    # a method that generates a blank plot (labeled y and x axes) given a range for x and y
    # pre: xStart, xEnd, yStart and yEnd are integers, where xStart is less than xEnd,
    # and yStart is before yEnd, yScale is an optional variable that is the scale for the
    # y axis
    # post: self.plot is an empty scatter plot with the given dimensions
    def generatePlane(self, xStart, xEnd, yStart, yEnd, yScale = None):
        self.plot = []
        y = yEnd
        #creates a list of three spaces for each x value
        lines = ['   ' for i in range(xEnd-xStart+2)]
        
        while y >= yStart:
            #creates a string of the y value, and the appropriate number of spaces and a |
            #to generate the y axis
            axis = str(y*yScale) + ' '*(4-len(str(y*yScale))) + '|'
            
            #adds the list of blank spaces so the dimensions of the plot will be
            #consistent and appends this to the plot
            self.plot.append([axis]+lines)
            y-=1

        #creates the x axis using the appropriate number of underscores to generate
        #the line based off of how many x coordinates there are
        underScore = ['___' for i in range(xEnd - xStart + 2)]

        #creates a blank spt before the x axis begins and appends it to the plot
        secLast = [ '    |'] + underScore
        self.plot.append(secLast)

        #generates the x axis using the x values and appends it to the plot
        xAxis = [str(x) + ' '*(3-len(str(x))) for x in range(xStart, xEnd + 1)]
        lastLine = ['     '] + xAxis
        self.plot.append(lastLine)

    # a method that creates a scatter plot given two lists (the second list is optional)
    # if the second list is left blank, the first list creates the y coordinates and
    # the x coordinates are 1 to the length of the first list
    # if there are two lists given, the first list is the x coordinates and the
    # second list is the y coordinates
    # pre: list1 is a 1d list of numbers, list2 is an optional variable
    # post: prints out self.plot, showing a scatterplot of the lists passed in
    
    def twoDScatter(self, list1, list2 = []):

        try:
            windowSize = os.get_terminal_size.columns/lines
        except:
            windowSize = 10

        #if list2 is blank, it sets y as list1 and x as 1 to the length of list1
        if list2 == []:
            y = list1
            x = [i for i in range(1,len(list1) + 1)]
 
        else:
            x = list1
            y = list2

        #gets the range for the x and y axes
        xEnd = max(x)
        xStart = min(x)
        yscale = max(y)//windowSize
        yNew = [i//yscale for i in y]
        yEnd = max(yNew)
        yStart = min(yNew)
        
        
        #uses generatePlane to create a blank plot
        self.generatePlane(xStart, xEnd, yStart, yEnd, yscale)

        #for each x value, it plots a mark according to the given x and y coordinates
        for i in range(len(x)):
            self.plot[int(yEnd - yNew[i])][x[i]-xStart + 1] = 'x  '

        #loop to print the plot as a string
        for line in self.plot:
            string = ''
            for item in line:
                string += str(item)
            print(string)


    # generates a bar graph of the lists passed in. if there is one list passed in
    # then that is the y coordinates and the x coordinates are 1 to the lenght of
    # the first list. if there are two lists list1 is the x and list2 is the y
    # pre: list1 is a list of numbers
    # post: prints out a bar graph of the lists passed in
    def barGraph(self, list1, list2 = []):

        try:
            windowSize = os.get_terminal_size.columns/lines
        except:
            windowSize = 10

        #if list2 is blank, it sets y as list1 and x as 1 to the length of list1
        if list2 == []:
            y = list1
            x = [i for i in range(1,len(list1) + 1)]
 
        else:
            x = list1
            y = list2

        #gets the range for the x and y axes
        xEnd = max(x)
        xStart = min(x)
        yscale = max(y)//windowSize
        yNew = [i//yscale for i in y]
        yEnd = max(yNew)
        yStart = min(yNew)
        
        
        #uses generatePlane to create a blank plot
        self.generatePlane(xStart, xEnd, yStart, yEnd, yscale)

        #for each x value, it plots a mark according to the given x and y coordinates
        for i in range(len(x)):
            char = random.choice(s.printable)
            for num in range(1, yNew[i]+ 1):
                self.plot[int(yEnd - num)][x[i]-xStart + 1] = char + '  '

        #loop to print the plot as a string
        for line in self.plot:
            string = ''
            for item in line:
                string += str(item)
            print(string)
