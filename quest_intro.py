# quest_intro.py

# This is the introductory segment of Library Quest where the player_name
# and player_class are gathered.

import time
from graphics import *

win = GraphWin("Library Quest", 800, 500)
win.setCoords(0.0, 0.0, 8.0, 5.0)
outline1 = Rectangle(Point(0.10, 0.10), Point(7.9, 4.9))
outline1.setWidth(10)
outline2 = Rectangle(Point(0.25, 0.25), Point(7.75, 4.75))
outline2.setWidth(5)
outline2.draw(win)
outline1.draw(win)

def inventory(player_class):
    if player_class == 'cataloger':
        inventory = ['MLIS', 'Student Debt', 'One (1) printed copy of the full MARC21 documentation']
    elif player_class == 'subject specialist':
        inventory = ['MLIS', 'Student Debt', "One (1) Master's or Doctorate in a field no one else has heard of"]
    elif player_class == 'archivist':
        inventory = ['MLIS', 'Student Debt', 'One (1) pocket full of 60 year old paperclips and binderclips']
    elif player_class == 'reference librarian':
        inventory = ['MLIS', 'Student Debt', 'One (1) enchanted Customer Service mask']
    elif player_class == 'youth services librarian':
        inventory = ['MLIS', 'Student Debt', 'One (1) baggie of crafting supplies']
    elif player_class == 'adult services librarian':
        inventory = ['MLIS', 'Student Debt', 'One (1) "Computers for Dummies" book']
    elif player_class == 'instruction librarian':
        inventory = ['MLIS', 'Student Debt', 'One (1) heavily annotated lesson plan']
    else:
        inventory = ['Your inventory seems to be a mystery...']
    return inventory

def buttons():
    submit_button = Text(Point(7.25, 0.625), "Submit")
    submit_button.setFace('courier')
    submit_button.draw(win)
    Rectangle(Point(7.0, 0.5), Point(7.5, 0.75)).draw(win)

    exit_button = Text(Point(0.75, 0.625), "Exit")
    exit_button.setFace('courier')
    exit_button.draw(win)
    Rectangle(Point(0.5, 0.5), Point(1.0, 0.75)).draw(win)

def dialog(dialog, sleeptime):
    dialogbloc = Text(Point(4.875, 2.875), dialog)
    dialogbloc.setFace('courier')
    dialogbloc.setSize(20)
    dialogbloc.draw(win)
    time.sleep(sleeptime)
    dialogbloc.undraw()
    return dialogbloc

def narration(narration, sleeptime):
    narrationbloc = Text(Point(4.875, 2.875), narration)
    narrationbloc.setFace('courier')
    narrationbloc.setSize(20)
    narrationbloc.setStyle('italic')
    narrationbloc.draw(win)
    time.sleep(sleeptime)
    narrationbloc.undraw()
    return narrationbloc

def prompt(prompt):
    promptbloc = Text(Point(2.5, 0.75), prompt)
    promptbloc.setFace('courier')
    promptbloc.setSize(20)
    promptbloc.draw(win)
    return promptbloc

def reply():
    responsebloc = Entry(Point(5.375, 0.75), 20)
    responsebloc.setText('')
    responsebloc.setFill('white')
    responsebloc.draw(win)
    win.getMouse()
    return responsebloc

def playername():
    textbox = Rectangle(Point(2.25, 1.25), Point(7.5, 4.5))
    textbox.setWidth(2)
    textbox.draw(win)

    buttons()

    narration1 = 'You are greeted inside\n' \
                 'by an elderly woman.'
    narration(narration1, 3)


    Image(Point(1.25, 3.75), 'agnes.gif').draw(win)
    agnesdialog1 = 'AGNES:\n\n' \
                   'Welcome to the Library.\n' \
                   'I am AGNES.\n' \
                   'What can I call you?'
    dialog(agnesdialog1, 7)

    prompt('What can I call you?')
    name = reply()

    return name

def playerclass(name):
    player_name = name.getText()
    agnesdialog2 = str("AGNES:\n\n" \
                   "It's a pleasure to meet you, \n" + player_name + '.')
    dialog(agnesdialog2, 3)


player_name = playername()
player_class = playerclass(player_name)
win.close()