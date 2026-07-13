import tkinter
from tkinter import *

display = ''
FontLabel = ("System", 30)
FontButton = ("Arial", 15)
ButtonWidth = 7
ButtonHeight = 3

NumberColor = "#808080"
OperatorColor = "#4d4d4d"
ButtonFG = "#f2f2f2"

root = Tk()
WindowFrame = Frame(root, width=385, height=500, bg="#333333")
WindowFrame.pack()


CalcDisplay = Label(WindowFrame, text=(display), font=FontLabel, width=16, height=2, bg="#999999", anchor=W, padx=0, pady=0, relief=SOLID)
CalcDisplay.place(x=0,y=0, anchor=NW)

def UpdateDisp():
    CalcDisplay.config(text=display)

def One(event):
    global display
    display += '1'
    UpdateDisp()
    return(display)

def Two(event):
    global display
    display += '2'
    UpdateDisp()
    return(display)

def Three(event):
    global display
    display += '3'
    UpdateDisp()
    return(display)

def Four(event):
    global display
    display += '4'
    UpdateDisp()
    return(display)

def Five(event):
    global display
    display += '5'
    UpdateDisp()
    return(display)

def Six(event):
    global display
    display += '6'
    UpdateDisp()
    return(display)

def Seven(event):
    global display
    display += '7'
    UpdateDisp()
    return(display)

def Eight(event):
    global display
    display += '8'
    UpdateDisp()
    return(display)

def Nine(event):
    global display
    display += '9'
    UpdateDisp()
    return(display)

def Zero(event):
    global display
    display += '0'
    UpdateDisp()
    return(display)

def Plus(event):
    global display
    display += '+'
    UpdateDisp()
    return(display)

def Minus(event):
    global display
    display += '-'
    UpdateDisp()
    return(display)

def Multiplication(event):
    global display
    display += '*'
    UpdateDisp()
    return(display)

def Division(event):
    global display
    display += '/'
    UpdateDisp()
    return(display)

def Equals(event):
    try:
        global display
        display = str(eval(display))
        UpdateDisp()
        return(display)
    
    except ZeroDivisionError:
        display = "ERROR"
        UpdateDisp()
        return(display)
    
    except SyntaxError:
        display = "ERROR"
        UpdateDisp()
        return(display)
    
    except NameError:
        display = "ERROR"
        UpdateDisp()
        return(display)

def Clear(event):
    global display
    display = ''
    UpdateDisp()
    return(display)


ButtonOne = Button(WindowFrame, text='1', width=ButtonWidth, height=ButtonHeight, bg=NumberColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonOne.place(x=5, y=110)
ButtonOne.bind('<Button>', One)

ButtonTwo = Button(WindowFrame, text='2', width=ButtonWidth, height=ButtonHeight, bg=NumberColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonTwo.place(x=100, y=110)
ButtonTwo.bind('<Button>', Two)

ButtonThree = Button(WindowFrame, text='3', width=ButtonWidth, height=ButtonHeight, bg=NumberColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonThree.place(x=195, y=110)
ButtonThree.bind('<Button>', Three)

ButtonFour = Button(WindowFrame, text='4', width=ButtonWidth, height=ButtonHeight, bg=NumberColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonFour.place(x=5, y=210)
ButtonFour.bind('<Button>', Four)

ButtonFive = Button(WindowFrame, text='5', width=ButtonWidth, height=ButtonHeight, bg=NumberColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonFive.place(x=100, y=210)
ButtonFive.bind('<Button>', Five)

ButtonSix = Button(WindowFrame, text='6', width=ButtonWidth, height=ButtonHeight, bg=NumberColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonSix.place(x=195, y=210)
ButtonSix.bind('<Button>', Six)

ButtonSeven = Button(WindowFrame, text='7', width=ButtonWidth, height=ButtonHeight, bg=NumberColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonSeven.place(x=5, y=310)
ButtonSeven.bind('<Button>', Seven)

ButtonEight = Button(WindowFrame, text='8', width=ButtonWidth, height=ButtonHeight, bg=NumberColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonEight.place(x=100, y=310)
ButtonEight.bind('<Button>', Eight)

ButtonNine = Button(WindowFrame, text='9', width=ButtonWidth, height=ButtonHeight, bg=NumberColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonNine.place(x=195, y=310)
ButtonNine.bind('<Button>', Nine)

ButtonZero = Button(WindowFrame, text='0', width=ButtonWidth, height=ButtonHeight, bg=NumberColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonZero.place(x=100, y=410)
ButtonZero.bind('<Button>', Zero)

ButtonPlus = Button(WindowFrame, text='+', width=ButtonWidth, height=ButtonHeight, bg=OperatorColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonPlus.place(x=290, y=110)
ButtonPlus.bind('<Button>', Plus)

ButtonMinus = Button(WindowFrame, text='-', width=ButtonWidth, height=ButtonHeight, bg=OperatorColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonMinus.place(x=290, y=210)
ButtonMinus.bind('<Button>', Minus)

ButtonMultiplication = Button(WindowFrame, text='×', width=ButtonWidth, height=ButtonHeight, bg=OperatorColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonMultiplication.place(x=290, y=310)
ButtonMultiplication.bind('<Button>', Multiplication)

ButtonDivision = Button(WindowFrame, text='÷', width=ButtonWidth, height=ButtonHeight, bg=OperatorColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonDivision.place(x=290, y=410)
ButtonDivision.bind('<Button>', Division)

ButtonEquals = Button(WindowFrame, text='=', width=ButtonWidth, height=ButtonHeight, bg=OperatorColor, font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonEquals.place(x=195, y=410)
ButtonEquals.bind('<Button>', Equals)

ButtonClear = Button(WindowFrame, text='CLEAR', width=ButtonWidth, height=ButtonHeight, bg="#FF8080", font=FontButton, fg=ButtonFG, relief=FLAT)
ButtonClear.place(x=5, y=410)
ButtonClear.bind('<Button>', Clear)

root.mainloop()
