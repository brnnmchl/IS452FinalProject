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

def inventory(player_class):
    if player_class == 'cataloger':
        player_inventory = ['MLIS', 'Student Debt', 'One (1) printed copy of the\nfull MARC21 documentation']
    elif player_class == 'subject specialist':
        player_inventory = ['MLIS', 'Student Debt', "One (1) Master's or Doctorate in\na field no one else has heard of"]
    elif player_class == 'archivist':
        player_inventory = ['MLIS', 'Student Debt', 'One (1) pocket full of 60 year old\npaperclips and binderclips']
    elif player_class == 'reference librarian':
        player_inventory = ['MLIS', 'Student Debt', 'One (1) enchanted Customer Service mask']
    elif player_class == 'youth services librarian':
        player_inventory = ['MLIS', 'Student Debt', 'One (1) baggie of crafting supplies']
    elif player_class == 'adult services librarian':
        player_inventory = ['MLIS', 'Student Debt', 'One (1) "Computers for Dummies" book']
    elif player_class == 'instruction librarian':
        player_inventory = ['MLIS', 'Student Debt', 'One (1) heavily annotated lesson plan']
    else:
        player_inventory = ['Notebook filled with strange symbols', 'Invisible pen', 'Arcane talisman']
    return player_inventory

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

# images
agnes_pic = Image(Point(1.25, 3.75), 'agnes.gif')
antelope_pic = Image(Point(1.25, 3.75), 'antelope.gif')
archivist_pic = Image(Point(1.25, 3.75), 'archivist.gif')
cardigan_pic = Image(Point(1.25, 3.75), 'cardigan.gif')
cart_pic = Image(Point(1.25, 3.75), 'cart.gif')
cat_pic = Image(Point(1.25, 3.75), 'cat.gif')
cataloger_pic = Image(Point(1.25, 3.75), 'cataloger.gif')
clarence_pic = Image(Point(1.25, 3.75), 'clarence.gif')
dean_pic = Image(Point(1.25, 3.75), 'dean.gif')
mug_pic = Image(Point(1.25, 3.75), 'mug.gif')
shelver_pic = Image(Point(1.25, 3.75), 'shelver.gif')
spectacles_pic = Image(Point(1.25, 3.75), 'spectacles.gif')
reference_pic = Image(Point(1.25, 3.75), 'reference.gif')

# relics
cardigan = 'CARDIGAN OF INVISIBILITY'
spectacles = 'SPECTACLES OF COMPUTER SIGHT'
mug = 'BOTTOMLESS MUG'
bookcart = 'THOUSAND SHELF BOOKCART'


textbox_outline = textbox()

submit = Button('submit')
submit_outline = submit.outline(7.0, 0.5, 7.5, 0.75, win)
submit_label = submit.label('Submit', 7.25, 0.625, win)

exit = Button('exit')
exit_outline = exit.outline(0.5, 0.5, 1.0, 0.75, win)
exit_label = exit.label("Exit", 0.75, 0.625, win)

intro = Intro()

while True:
    clickPoint = win.getMouse()

    if clickPoint is None:
        win.close()
    elif exit.clickButton(clickPoint, exit_outline):
        win.close()
    elif submit.clickButton(clickPoint, submit_outline):
        intro.dialog('hi', 5, win)
    else:
        win.close()



