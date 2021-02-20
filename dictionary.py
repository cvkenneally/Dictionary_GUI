from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title("Connor's Dictionary") # The name that is displayed on the toolbar at the top of the frame

# Declare constants
TITLE = tkFont.Font(family = "Arial", size = 20)
FONTS = tkFont.Font(family = "Arial", size = 12)

# Declare the Dictionary itself
class my_dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

dictionary = my_dictionary()
dictionary.add("CPU", "Central Processing Unit")

# Functions / Actions
def searchFor():
    # This function finds the value for the key and displays it under the Definition
    wordToFind = key.get()
    if wordToFind in dictionary:
        valueForWord = dictionary[wordToFind]
        var.set(valueForWord)
    else:
        var.set("That word is not in your dictionary.")

def clear():
    # This function will clear all entry's and labels
    var.set("")
    key.select_clear()

def addToDictionary():
    # This function will add the key and new definition into the dictionary
    tempKey = key.get()
    tempValue = newValue.get()

    dictionary.add(tempKey, tempValue)

# Initial frame
guiFrame = Frame(root)
    # guiFrame.pack()  <-- this isnt needed when using grid

header = Label(root, text = "Connor's Dictionary", font = TITLE)
header.grid(row = 0, column = 1)

keyLabel = Label(root, text = "Word", font = FONTS)
keyLabel.grid(row = 1, column = 0)

key = Entry(root, width = 50)
key.grid(row = 1, column = 1)

valueLabel = Label(root, text = "Definition", font = FONTS)
valueLabel.grid(row = 2, column = 0)

var = StringVar()
value = Message(root, textvariable = var, width = 300)
value.grid(row = 2, column = 1)

searchButton = Button(root, text = "Search", command = searchFor)
searchButton.grid(row = 1, column = 3)

clearButton = Button(root, text = "Clear", command = clear)
clearButton.grid(row = 2, column = 3)

addButton = Button(root, text = "Add", command = addToDictionary)
addButton.grid(row = 3, column = 3)

newValueLabel = Label(root, text = "New Definition", font = FONTS)
newValueLabel.grid(row = 3, column = 0)

newValue = Entry(root, width = 50)
newValue.grid(row = 3, column = 1)

root.mainloop() # This is the loop to run the window 
