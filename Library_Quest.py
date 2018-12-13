# Library_Quest.py

# This is a library themed, text adventure game where you can gather
# magical items and stop patron privacy from being violated!

import time
from graphics import *
from lq_classes import *

# set the base graphic window
win = GraphWin("Library Quest", 800, 500)
win.setCoords(0.0, 0.0, 8.0, 5.0)
outline1 = Rectangle(Point(0.10, 0.10), Point(7.9, 4.9))
outline1.setWidth(10)
outline2 = Rectangle(Point(0.25, 0.25), Point(7.75, 4.75))
outline2.setWidth(5)
outline2.draw(win)
outline1.draw(win)

# set up basic functions
def textbox():
    textbox = Rectangle(Point(2.25, 1.25), Point(7.5, 4.5))
    textbox.setWidth(2)
    textbox.draw(win)
    return textbox

# read in the text files
infile = open('library_quest_bad_endings.txt', 'r')
bad_endings = infile.read()
infile.close()

infile = open('library_quest_dialog.txt', 'r')
dialog = infile.read()
infile.close()

infile = open('library_quest_narration.txt', 'r')
narration = infile.read()
infile.close()

section_break = "\n\n\n"

bad_endings_list = bad_endings.split(section_break)
dialog_list = dialog.split(section_break)
narration_list = narration.split(section_break)

# relics
cardigan = 'CARDIGAN OF INVISIBILITY'
spectacles = 'SPECTACLES OF COMPUTER SIGHT'
mug = 'BOTTOMLESS MUG'
bookcart = 'THOUSAND SHELF BOOKCART'


textbox_outline = textbox()

submit = Button(Point(7.25, 0.625), 0.5, 0.25, 'Submit', 'pale green', win)
exit = Button(Point(0.75, 0.625), 0.5, 0.25, 'Exit', 'tomato', win)

submit.activate()
exit.activate()

intro = Intro()

clickPoint = win.getMouse()

if submit.clicked(clickPoint):
    intro.dialog('hi', 5, win)
elif exit.clicked(clickPoint):
    win.close()
else:
    win.close()




