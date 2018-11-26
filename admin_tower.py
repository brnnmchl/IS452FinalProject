# admin_tower.py

# code for the admin's tower level

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

cardigan = 'CARDIGAN OF INVISIBILITY'
spectacles = 'SPECTACLES OF COMPUTER SIGHT'
mug = 'BOTTOMLESS MUG'
bookcart = 'THOUSAND SHELF BOOKCART'

player_name = "Brinna"
player_class = 'cataloger'

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

def textbox():
    textbox = Rectangle(Point(2.25, 1.25), Point(7.5, 4.5))
    textbox.setWidth(2)
    textbox.draw(win)

    return textbox

def submit():
    submit_button = Text(Point(7.25, 0.625), "Submit")
    submit_button.setFace('courier')
    submit_button.draw(win)
    Rectangle(Point(7.0, 0.5), Point(7.5, 0.75)).draw(win)

    return submit_button

def exit():
    exit_button = Text(Point(0.75, 0.625), "Exit")
    exit_button.setFace('courier')
    exit_button.draw(win)
    Rectangle(Point(0.5, 0.5), Point(1.0, 0.75)).draw(win)

    return exit_button

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

def admintower():
    narration94 = "As soon as you utter your destination,\n" \
                  "the BOOKCART rockets off."
    narration95 = "Colors rush by, all blurred together\n" \
                  "as you hurtle along through the Library."
    narration96 = "And just as quickly as you took off, the\n" \
                  "BOOKCART stops, nearly throwing you\n" \
                  "clear across the spacious lobby area\n" \
                  "you landed in."
    narration97 = "The lobby has only one door, which\n" \
                  "seems suspicious, made of polished\n" \
                  "mahogany and glass with neat, golden\n" \
                  "lettering."
    narration98 = "Office of DEAN PATRICK ARCHY."
    narration99 = "Your heart pounds in your ears. This\n" \
                  "is it. You're finally here. The final\n" \
                  "showdown."
    narration100 = "You climb off the cart and consider\n" \
                   "what to do."
    narration101 = "You could knock, equip the RELICS,\n" \
                   "or just leave..."
    narration(narration94, 7)
    narration(narration95, 7)
    narration(narration96, 9)
    narration(narration97, 9)
    narration(narration98, 5)
    narration(narration99, 8)
    narration(narration100, 6)
    narration(narration101, 6)

    lobby_choice = prompt("Knock, equip, or leave? >")
    lobby_choice_reply = reply().getText().lower()
    lobby_choice.undraw()
    if lobby_choice_reply == "knock":
        narration104 = "You march up to the door, ready\n" \
                       "to do battle, and knock three times."
        narration105 = "From behind the door, you hear a\n" \
                       "sickly sweet voice call out..."
        narration(narration104, 6.5)
        narration(narration105, 6.5)

        dean_pic.draw(win)
        archydialog1 = "ARCHY:\n\n" \
                       "Come in!"
        dialog(archydialog1, 3.5)
        dean_pic.undraw()

        enter_office1 = prompt("Enter the office? >")
        enter_office_reply1 = reply().getText().lower()
        enter_office1.undraw()
        if enter_office_reply1 == "yes":
            narration106 = "You open the door and charge in,\n" \
                           "expecting a fight, but what you see\n" \
                           "is a rather terrifying man."
            narration107 = "He wears a pristine suit and his\n" \
                           "eyes are like a snake's, pinning\n" \
                           "you in place."
            narration108 = "He smiles, his teeth blindingly\n" \
                           "white and razor sharp."
            narration(narration106, 8)
            narration(narration107, 8)
            narration(narration108, 7)

            dean_pic.draw(win)
            archydialog2 = "ARCHY:\n\n" \
                           "Ah, how nice of you to stop by,\n" + player_name.upper() + "."
            archydialog3 = "ARCHY:\n\n" \
                           "I had such high hopes for you, but\n" \
                           "gathering the RELICS? Trying to foil\n" \
                           "my nefarious plot?"
            archydialog4 = "ARCHY:\n\n" \
                           "*sigh* It just won't do."
            dialog(archydialog2, 5)
            dialog(archydialog3, 7)
            dialog(archydialog4, 4)

            narration109 = "Before you can make a move, ARCHY\n" \
                           "catches your eye and using some sort\n" \
                           "of dark, admin arts, he turns you to\n" \
                           "stone."
            narration(narration109, 9)
            dean_pic.undraw()
            mainmenu()
        else:
            narration110 = "Knowing that you'd give yourself away,\n" \
                           "you hold still, waiting with bated breath\n" \
                           "until you hear ARCHY stand with a grumble\n" \
                           "and start walking towards the door."
            narration111 = "You step back slightly as the door opens\n" \
                           "and a man so terrifying you almost freeze\n" \
                           "looks out."
            narration112 = "He wears a pristine suit and his eyes,\n" \
                           "like a snake's, survey the lobby."
            narration113 = "You can feel all your frustration and\n" \
                           "rage at the state of the world well up\n" \
                           "within you just by looking at him."
            narration114 = "Before you can make a move, he turns his\n" \
                           "gaze on you and smiles, his teeth\n" \
                           "blindingly white and razor sharp."
            narration(narration110, 9)
            narration(narration111, 8)
            narration(narration112, 6)
            narration(narration113, 8)
            narration(narration114, 8)

            dean_pic.draw(win)
            archydialog5 = "ARCHY:\n\n" \
                           "Oh, come now " + player_name.upper() + ".\n" \
                                                                   "That's just rude, making a guy get\n" \
                                                                   "up from his work like that."
            archydialog6 = "ARCHY:\n\n" \
                           "Guess I'll have to terminate your\n" \
                           "contract early."
            dialog(archydialog5, 7)
            dialog(archydialog6, 6)
            dean_pic.undraw()

            narration115 = "Using some sort of dark, admin arts,\n" \
                           "he immediately turns you to stone."
            narration(narration115, 7)
            mainmenu()
    elif lobby_choice_reply == "leave":
        narration116 = "You feel whatever courage you had\n" \
                       "dissipate in the face of this door."
        narration117 = "Shaking your head and sending a\n" \
                       "silent apology to all the poor souls\n" \
                       "of the Library who will suffer for your\n" \
                       "cowardice, you hop back on the BOOKCART."
        narration118 = "You ask the BOOKCART to take you\n" \
                       "anywhere but here."
        narration119 = "There is a whoos and a blur of color,\n" \
                       "and you find yourself in front of a\n" \
                       "desk where a terrifying man sits, his\n" \
                       "snake-like eyes unamused as he sets his\n" \
                       "pen down."
        narration(narration116, 7)
        narration(narration117, 9)
        narration(narration118, 7)
        narration(narration119, 9)

        dean_pic.draw(win)
        archydialog7 = "ARCHY:\n\n" \
                       "Oh, honestly. Can't you even try\n" \
                       "to finish the game? After all, you\n" \
                       "got this far."
        archydialog8 = "ARCHY:\n\n" \
                       "*sigh* Well, it doesn't matter anymore.\n" \
                       "I have work to do."
        dialog(archydialog7, 8)
        dialog(archydialog8, 7)
        dean_pic.undraw()

        narration120 = "He catches your eye and using some\n" \
                       "sort of dark, admin arts, turns you\n" \
                       "to stone."
        narration(narration120, 8)
        mainmenu()
    elif lobby_choice_reply == "equip":
        narration121 = "You pull on the CARDIGAN OF INVISIBILITY\n" \
                       "and don the SPECTACLES OF COMPUTER\n" \
                       "SIGHT. In one hand, you ready the\n" \
                       "BOTTOMLESS MUG."
        narration122 = "With trepidation, you move forward\n" \
                       "and knock on the door."
        narration123 = "From behind the door, you hear a\n" \
                       "sickly sweet voice call out..."
        narration(narration121, 9)
        narration(narration122, 7)
        narration(narration123, 7)

        dean_pic.draw(win)
        archydialog9 = "ARCHY:\n\n" \
                       "Come in!"
        dialog(archydialog9, 3)
        dean_pic.undraw()

        enter_office2 = prompt("Enter the office? >")
        enter_office_reply2 = reply().getText().lower()
        enter_office2.undraw()
        if enter_office_reply2 == "yes":
            ##
        else:
            ##
    else:
        narration102 = "Was that an option?"
        narration103 = "No, no it wasn't. Nice try."
        narration(narration102, 4)
        narration(narration103, 4)
        mainmenu()


player_inventory = inventory(player_class)
player_inventory.append(cardigan)
player_inventory.append(spectacles)
player_inventory.append(mug)
player_inventory.append(bookcart)
textbox = textbox()
submit()
admintower()
win.close()
