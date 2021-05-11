#Raghu Alluri
#4/19/2018
#This program will make a calculator interface thiat is usable for calculations
#such as arithimetic functions and more
from tkinter import *
from math import sin, cos, radians, pi
import sys as sysys




#Defined a screen / window for tkinter application
root = Tk()
#Set the width and height of the initial window
root.geometry("340x380")
#Set the title of the window
root.title("Simple Calculator")




#Set's the top frame at the top of the screen to a certain height
topFrame = Frame(root, width = 340, height = 20, bd = 1, relief = "raise")
topFrame.pack(side = TOP)




#Set's the bottom frame from the end of the top frame to the bottom of the screen
bottomFrame = Frame(root, width = 340, height = 380, bd = 1, relief = "raise")
bottomFrame.pack(side = BOTTOM)




#Main code written for calculations
#--------

"""A Class is made to store all related functions of inputs and returning
outputs in this case."""

class calcInputReturn:
#When a button is clicked it will set that string onto the display. It will be appended
    def pressedButton(pressed):
        global this
        this = this + str(pressed)
        textOnScreen.set(this)

    #When the clear button is clicked, it will set the screen to be an empty string
    def clearAll():
        global this
        this = ''
        textOnScreen.set('')

    #When the delete key is pressed, it will delete the previous operation or number pressed
    def deletePrevKey():
        global this, list_this
        thing = list(this)
        if len(thing) > 0:
            del thing[-1]
            this = ''.join(thing)
            textOnScreen.set(this)
        else:
            this = ''
            textOnScreen.set(this)

    #When the equal sign in clicked, it will evaluate the operations on the Screen
    #Or it will return an error if there is a syntax error by the user
    def equalAnswer():
        global ans, this
        try:
            ans = str(eval(this))
            textOnScreen.set(ans)
            this = ''
        except:
            textOnScreen.set('Error1')

#Sets the textScreen so that it can be received as string type variable for the calculator screen
global textOnScreen
this = ''
textOnScreen = StringVar()

#--------
#End of main programming for calculations of calculator




#A class is made to keep all widgets in topFrames together as an object
class upperFrame:
    #Parameters have been set to allow easy access of calling them and changing values of them

    def displayScreen(sw, jr, fs):
        #Calculator Screen to Display Answer is defined as a reciever or string values
        screen = Entry(topFrame, font = ('Arial', fs), textvariable = textOnScreen, bd = 1, width = sw, justify = jr)
        screen.grid(row = 0, column = 0)




#A class is made to keep all widgets in bottomFrames together as an object
class lowerFrame:

    def preRow(px, py, fgc):
        #Preliminary Row of buttons which primarily comprise of operators (ex. 'sin', 'pi', etc.)
        buttonBrc1 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 14), width = 2, text = '(', bg = 'gray5', command = lambda : calcInputReturn.pressedButton('(')). grid(row = 0, column = 0)
        buttonBrc2 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 14), width = 2, text = ')', bg = 'gray5', command = lambda : calcInputReturn.pressedButton(')')). grid(row = 0, column = 1)
        buttonSin = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 14), width = 2, text = 'sin(x)', bg = 'gray5', command = lambda : calcInputReturn.pressedButton('sin')). grid(row = 0, column = 2)
        buttonDel = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 14), width = 2, text = 'Del', bg = 'gray5', command = lambda : calcInputReturn.deletePrevKey()). grid(row = 0, column = 3)
        buttonPi = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 14), width = 2, text = 'π', bg = 'gray5', command = lambda : calcInputReturn.pressedButton('pi')). grid(row = 0, column = 4)

    def firstRow(px, py, fgc):
        #Row 1 of the buttons on calculator
        button9 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '9', bg = "gray24", command = lambda : calcInputReturn.pressedButton(9)). grid(row = 1, column = 0)
        button8 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '8', bg = "gray24", command = lambda : calcInputReturn.pressedButton(8)). grid(row = 1, column = 1)
        button7 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '7', bg = "gray24", command = lambda : calcInputReturn.pressedButton(7)). grid(row = 1, column = 2)
        buttonAdd = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '+', bg = "gray5", command = lambda : calcInputReturn.pressedButton('+')). grid(row = 1, column = 3)
        buttonDegToRad = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = 'Deg', bg = 'gray5', command = lambda : calcInputReturn.pressedButton('radians')). grid(row = 1, column = 4)

    def secondRow(px, py, fgc):
        #Row 2 of the buttons on calculator
        button6 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '6', bg = "gray24", command = lambda : calcInputReturn.pressedButton(6)). grid(row = 2, column = 0)
        button5 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '5', bg = "gray24", command = lambda : calcInputReturn.pressedButton(5)). grid(row = 2, column = 1)
        button4 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '4', bg = "gray24", command = lambda : calcInputReturn.pressedButton(4)). grid(row = 2, column = 2)
        buttonMin = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '-', bg = "gray5", command = lambda : calcInputReturn.pressedButton('-')). grid(row = 2, column = 3)
        buttonSquare = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = 'x^2', bg = 'gray5', command = lambda : calcInputReturn.pressedButton('**2')). grid(row = 2, column = 4)

    def thirdRow(px, py, fgc):
        #Row 3 of the buttons on calculator
        button3 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '3', bg = "gray24", command = lambda : calcInputReturn.pressedButton(3)). grid(row = 3, column = 0)
        button2 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '2', bg = "gray24", command = lambda : calcInputReturn.pressedButton(2)). grid(row = 3, column = 1)
        button1 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '1', bg = "gray24", command = lambda : calcInputReturn.pressedButton(1)). grid(row = 3, column = 2)
        buttonTimes = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = 'x', bg = "gray5", command = lambda : calcInputReturn.pressedButton('*')). grid(row = 3, column = 3)
        buttonExp = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = 'x^y', bg = 'gray5', command = lambda : calcInputReturn.pressedButton('**')). grid(row = 3, column = 4)

    def fourthRow(px, py, fgc):
        #Row 4 of the buttons on calculator
        button0 = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '0', bg = "gray24", command = lambda : calcInputReturn.pressedButton(0)). grid(row = 4, column = 0)
        buttonClear = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = 'C', bg = "red", command = lambda : calcInputReturn.clearAll()). grid(row = 4, column = 1)
        buttonEquals = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '=', bg = "dodger blue", command = lambda : calcInputReturn.equalAnswer()). grid(row = 4, column = 2)
        buttonDiv = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '/', bg = "gray5", command = lambda : calcInputReturn.pressedButton('/')). grid(row = 4, column = 3)
        buttonDecimal = Button(bottomFrame, padx = px, pady = py, bd = 1, fg = fgc, font = ('arial', 18), width = 2, height = 2, text = '.', bg = 'gray5', command = lambda : calcInputReturn.pressedButton('.')). grid(row = 4, column = 4)




#Defining all parameters in this section for functions
scrw = 15
jusr = "right"
fontsize = 30

pdx = 16
pdy = 1
fgcol = "white"




#Calling all functions here for display and functionality
upperFrame.displayScreen(scrw, jusr, fontsize)

lowerFrame.preRow(pdx, pdy, fgcol)
lowerFrame.firstRow(pdx, pdy, fgcol)
lowerFrame.secondRow(pdx, pdy, fgcol)
lowerFrame.thirdRow(pdx, pdy, fgcol)
lowerFrame.fourthRow(pdx, pdy, fgcol)




#Runs the loop of this code until the user has exited from the window
root.mainloop()
sysys.exit()
