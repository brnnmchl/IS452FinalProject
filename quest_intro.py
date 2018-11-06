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

agnes_pic = Image(Point(1.25, 3.75), 'agnes.gif')
antelope_pic = Image(Point(1.25, 3.75), 'antelope.gif')
cat_pic = Image(Point(1.25, 3.75), 'cat.gif')
cataloger_pic = Image(Point(1.25, 3.75), 'cataloger.gif')
clarence_pic = Image(Point(1.25, 3.75), 'clarence.gif')
dean_pic = Image(Point(1.25, 3.75), 'dean.gif')
reference_pic = Image(Point(1.25, 3.75), 'reference.gif')


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
    responsebloc = Entry(Point(5.375, 0.75), 30)
    responsebloc.setText('')
    responsebloc.setFill('white')
    responsebloc.draw(win)
    win.getMouse()
    responsebloc.undraw()
    return responsebloc

def playername():
    textbox = Rectangle(Point(2.25, 1.25), Point(7.5, 4.5))
    textbox.setWidth(2)
    textbox.draw(win)

    buttons()

    narration1 = 'You are greeted inside\n' \
                 'by an elderly woman.'
    narration(narration1, 3)

    agnes_pic.draw(win)
    agnesdialog1 = 'AGNES:\n\n' \
                   'Welcome to the Library.\n' \
                   'I am AGNES.\n' \
                   'What can I call you?'
    dialog(agnesdialog1, 5)

    nameprompt = prompt('Enter player name: >')
    name = reply().getText()
    nameprompt.undraw()
    return name

def playerclass(name):
    player_name = name
    agnesdialog2 = str("AGNES:\n\n" \
                   "It's a pleasure to meet you, \n" + player_name + '.')
    agnesdialog3 = "AGNES:\n\n" \
                   "This must be your first day.\n" \
                   "Well, don't worry, we here at the\n" \
                   "Library are all quite friendly.\n" \
                   "I'm sure you'll enjoy working here."
    agnesdialog4 = "AGNES:\n\n" \
                   "What position are you starting today?"
    agnesdialog5 = "AGNES:\n\n" \
                   "Ah yes! We've been excited to have\n" \
                   "you join us! I hope you'll have many\n" \
                   "wonderful adventures while working here."

    dialog(agnesdialog2, 3.5)
    dialog(agnesdialog3, 6)
    dialog(agnesdialog4, 3.5)
    class_options = Text(Point(4.875, 2.875), 'Select one:\n\n'
                                              'Cataloger\n'
                                              'Subject Specialist\n'
                                              'Archivist\n'
                                              'Reference Librarian\n'
                                              'Youth Services Librarian\n'
                                              'Adult Services Librarian\n'
                                              'Instruction Librarian')
    class_options.setFace('courier')
    class_options.setSize(20)
    class_options.setStyle('italic')
    class_options.draw(win)
    positionprompt = prompt('Choose player class: >')
    position = reply().getText()
    positionprompt.undraw()
    class_options.undraw()

    dialog(agnesdialog5, 6)
    narration2 = 'You hear a loud crash and both\n' \
                 'you and AGNES turn to see a young\n' \
                 'man rushing towards you.'
    agnes_pic.undraw()
    narration(narration2, 4.5)

    agnes_pic.draw(win)
    agnesdialog6 = 'AGNES:\n\n' \
                   'Oh my! CLARENCE,\n' \
                   'what is going on?'
    dialog(agnesdialog6, 3.5)
    agnes_pic.undraw()
    clarence_pic.draw(win)

    clarencedialog1 = "CLARENCE:\n\n" \
                      "It's terrible, AGNES!\n" \
                      "The dean has finally made his decision!"
    dialog(clarencedialog1, 3.5)

    clarence_pic.undraw()
    agnes_pic.draw(win)
    agnesdialog7 = "AGNES:\n\n" \
                   "No! It can't be!"
    dialog(agnesdialog7, 3)

    agnes_pic.undraw()
    clarence_pic.draw(win)
    clarencedialog2 = "CLARENCE:\n\n" \
                      "Unfortunately, it's true. We're going to\n" \
                      "be tracking patrons' borrowing history\n" \
                      "in the TOME OF LENDING!"
    clarencedialog3 = "CLARENCE:\n\n" \
                      "DEAN PATRICK ARCHY has already\n" \
                      "locked it in the ADMIN'S TOWER!"
    dialog(clarencedialog2, 5.5)
    dialog(clarencedialog3, 3.5)

    clarence_pic.undraw()
    agnes_pic.draw(win)
    agnesdialog8 = "AGNES:\n\n" \
                   "Oh, it's too horrible...\n" \
                   "and with the LIBRARY RELICS\n" \
                   "scattered throughout the Library...\n" \
                   "Whatever shall we do?"
    dialog(agnesdialog8, 5.5)

    agnes_pic.undraw()
    clarence_pic.draw(win)
    clarencedialog4 = str("CLARENCE:\n\n" \
                      "Wait... You must be the new\n" + position + "!")
    clarencedialog5 = "CLARENCE:\n\n" \
                      "There might still be a chance!\n" \
                      "If you can gather the LIBRARY RELICS\n" \
                      "and destroy the TOME OF LENDING,\n" \
                      "we might be able to stop this madness!"
    dialog(clarencedialog4, 3.5)
    dialog(clarencedialog5, 6)

    clarence_pic.undraw()
    playerdialog1 = str(player_name.upper() + ":\n\n" \
                                  "The LIBRARY RELICS?")
    dialog(playerdialog1, 2.5)

    clarence_pic.draw(win)
    clarencedialog6 = "CLARENCE:\n\n" \
                      "Four magical treasures that grant\n" \
                      "the user incredible powers."
    clarencedialog7 = "CLARENCE:\n\n" \
                      "The CARDIGAN OF INVISIBILITY,\n" \
                      "the SPECTACLES OF COMPUTER SIGHT,\n" \
                      "the BOTTOMLESS MUG,\n" \
                      "and the THOUSAND SHELF BOOKCART."
    dialog(clarencedialog6, 4.5)
    dialog(clarencedialog7, 6)

    clarence_pic.undraw()
    agnes_pic.draw(win)
    agnesdialog9 = "AGNES:\n\n" \
                   "But the RELICS have been scattered\n" \
                   "throughout the Library for many\n" \
                   "years, and it will be no small task\n" \
                   "to find them all."
    agnesdialog10 = "AGNES:\n\n" \
                   "You will face many dangers and\n" \
                   "encounter many traps along the way."
    dialog(agnesdialog9, 6.5)
    dialog(agnesdialog10, 4.5)

    return position

def startquest():
    agnesdialog11 = str("AGNES:\n\n" + player_name + ", will you\n" \
                                                 "take on this quest?")
    dialog(agnesdialog11, 3.5)
    agnes_pic.undraw()

    takethequest = prompt("Take the quest? >")
    questtaken = reply()
    questtakenstr = questtaken.getText().lower()
    takethequest.undraw()
    questtaken.undraw()
    if questtakenstr == 'yes':
        agnes_pic.draw(win)
        agnesdialog12 = "AGNES:\n\n" \
                    "Oh, thank you, thank you!"
        agnesdialog13 = "AGNES:\n\n" \
                    "But you must hurry!"
        dialog(agnesdialog12, 2.5)
        dialog(agnesdialog13, 2.5)

        narration3 = "AGNES points towards a stone archway\n" \
                 "where you can see a flight of stairs\n" \
                 "leads down into the darkness.\n" \
                 "A cool, musty smelling breeze wafts\n" \
                 "out of it and you feel a little\n" \
                 "shiver of fear."
        narration(narration3, 6.5)

        agnesdialog14 = "AGNES:\n\n" \
                    "Down those stairs you will find the\n" \
                    "ARCHIVIST'S LAIR. There you will\n" \
                    "find the CARDIGAN OF INVISIBILITY."
        dialog(agnesdialog14, 5.5)

        agnes_pic.undraw()
        clarence_pic.draw(win)
        clarencedialog8 = str("CLARENCE:\n\n" \
                      "Good luck, " + player_name + '.')
        dialog(clarencedialog8, 2.5)

        clarence_pic.undraw()

        playerdialog2 = str(player_name.upper() + ":\n\n"
                                              "T-Thanks.")
        dialog(playerdialog2, 2.5)

        narration4 = "You grit your teeth and square\n" \
                 "your shoulders. You're ready for\n" \
                 "this. This is what all those\n" \
                 "MLIS classes have prepared you\n" \
                 "for. You walk over to the archway."
        narration(narration4, 5.5)

        takestairs_p = prompt("Descend the stairs? >")
        takestairs_r = reply()
        takestairs_str = takestairs_r.getText().lower()
        if takestairs_str == 'yes':
            takestairs_p.undraw()
            takestairs_r.undraw()
        else:
            takestairs_p.undraw()
            takestairs_r.undraw()
            nostairs = Text(Point(4.875, 2.875), "The floor opens up beneath you\n"
                                             "and you are devoured by silverfish.")
            nostairs.setSize(20)
            nostairs.setFace('courier')
            nostairs.setStyle('italic')
            nostairs.draw(win)
            time.sleep(5)
            nostairs.undraw()
            mainmenu()
    else:
        noquest = Text(Point(4.875, 2.875), "The world crumbles to chaos.\n"
                                        "You see yourself 20 years from now\n"
                                        "living the real live version of 1984.")
        noquest.setFace("courier")
        noquest.setSize(20)
        noquest.setStyle('italic')
        noquest.draw(win)
        time.sleep(7)
        noquest.undraw()
        mainmenu()

player_name = playername()
player_class = playerclass(player_name)
startquest()
win.close()
