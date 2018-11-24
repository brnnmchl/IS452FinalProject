# catalogers_dungeon.py

# this is the code for the cataloger's dungeon level

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
cat_pic = Image(Point(1.25, 3.75), 'cat.gif')
cataloger_pic = Image(Point(1.25, 3.75), 'cataloger.gif')
clarence_pic = Image(Point(1.25, 3.75), 'clarence.gif')
dean_pic = Image(Point(1.25, 3.75), 'dean.gif')
mug_pic = Image(Point(1.25, 3.75), 'mug.gif')
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

def puzzletwo():
    puzzlespace = Rectangle(Point(1.25, 1.75), Point(3.25, 3.75))
    puzzlespace.setWidth(2)
    puzzlespace.draw(win)

    latline1 = Line(Point(0.75, 2.25), Point(3.25, 2.25))
    latline2 = Line(Point(0.75, 2.75), Point(3.25, 2.75))
    latline3 = Line(Point(0.75, 3.25), Point(3.25, 3.25))
    latline4 = Line(Point(0.75, 3.75), Point(3.25, 3.75))
    latline5 = Line(Point(0.75, 1.75), Point(3.25, 1.75))
    latline1.draw(win)
    latline2.draw(win)
    latline3.draw(win)
    latline4.draw(win)
    latline5.draw(win)

    longline1 = Line(Point(1.25, 1.75), Point(1.25, 4.25))
    longline2 = Line(Point(1.75, 1.75), Point(1.75, 4.25))
    longline3 = Line(Point(2.25, 1.75), Point(2.25, 4.25))
    longline4 = Line(Point(2.75, 1.75), Point(2.75, 4.25))
    longline5 = Line(Point(3.25, 1.75), Point(3.25, 4.25))
    longline1.draw(win)
    longline2.draw(win)
    longline3.draw(win)
    longline4.draw(win)
    longline5.draw(win)

    leftlabel1 = Text(Point(0.9, 3.5), 'Mono-\ngraphs')
    leftlabel2 = Text(Point(0.9, 3), 'Serials')
    leftlabel3 = Text(Point(0.9, 2.5), 'Music')
    leftlabel4 = Text(Point(0.9, 2), 'Rare\nBooks')
    toplabel1 = Text(Point(1.5, 4), "LCSH")
    toplabel2 = Text(Point(2, 4), "NAF")
    toplabel3 = Text(Point(2.5, 4), "OCLC")
    toplabel4 = Text(Point(3, 4), "MaRC")
    leftlabel1.setFace('courier')
    leftlabel2.setFace('courier')
    leftlabel3.setFace('courier')
    leftlabel4.setFace('courier')
    toplabel1.setFace('courier')
    toplabel2.setFace('courier')
    toplabel3.setFace('courier')
    toplabel4.setFace('courier')
    leftlabel1.draw(win)
    leftlabel2.draw(win)
    leftlabel3.draw(win)
    leftlabel4.draw(win)
    toplabel1.draw(win)
    toplabel2.draw(win)
    toplabel3.draw(win)
    toplabel4.draw(win)

    hints = Text(Point(5.75, 3.75), "All the incoming new materials need to be\n"
                                 "delivered to the appropriate cataloger.\n"
                                 "Who is in charge of each type of material?\n\n"
                                 "1) Nigel always knows the most recent gossip from the\n"
                                 "Cats and Crochet Monthly Report.\n\n"
                                 "2) Olive has terrible asthma and cannot stand to be\n"
                                 "around books older than her grandmother.\n\n"
                                 "3) Laurie constantly complains that she can never get\n"
                                 "Maxwell's attention because he always has headphones on.")
    hints.setFace('courier')
    hints.draw(win)

    name1 = Text(Point(4.5, 2.5), "Laurie C. Smith-Hall >")
    name2 = Text(Point(4.5, 2), "Nigel A Fink >")
    name3 = Text(Point(4.5, 1.5), "Olive C. Lawrence-Carrey >")
    name4 = Text(Point(4.5, 1), "Maxwell R. Cliffwood >")
    name1.setFace('courier')
    name2.setFace('courier')
    name3.setFace('courier')
    name4.setFace('courier')
    name1.draw(win)
    name2.draw(win)
    name3.draw(win)
    name4.draw(win)

    answer1input = Entry(Point(6.5, 2.5), 15)
    answer1input.setText('')
    answer1input.setFill('white')
    answer1input.draw(win)
    win.getMouse()
    answer1input.undraw()
    answer1 = answer1input.getText().lower()
    finalanswer1 = Text(Point(6.5, 2.5), answer1)
    finalanswer1.setFace('courier')
    finalanswer1.draw(win)

    answer2input = Entry(Point(6.5, 2), 15)
    answer2input.setText('')
    answer2input.setFill('white')
    answer2input.draw(win)
    win.getMouse()
    answer2input.undraw()
    answer2 = answer2input.getText().lower()
    finalanswer2 = Text(Point(6.5, 2), answer2)
    finalanswer2.setFace('courier')
    finalanswer2.draw(win)

    answer3input = Entry(Point(6.5, 1.5), 15)
    answer3input.setText('')
    answer3input.setFill('white')
    answer3input.draw(win)
    win.getMouse()
    answer3input.undraw()
    answer3 = answer3input.getText().lower()
    finalanswer3 = Text(Point(6.5, 1.5), answer3)
    finalanswer3.setFace('courier')
    finalanswer3.draw(win)

    answer4input = Entry(Point(6.5, 1), 15)
    answer4input.setText('')
    answer4input.setFill('white')
    answer4input.draw(win)
    win.getMouse()
    answer4input.undraw()
    answer4 = answer4input.getText().lower()
    finalanswer4 = Text(Point(6.5, 1), answer4)
    finalanswer4.setFace('courier')
    finalanswer4.draw(win)

    finish_puzzle = prompt('Click "Submit" to finish. >')

    win.getMouse()

    puzzlespace.undraw()
    latline1.undraw()
    latline2.undraw()
    latline3.undraw()
    latline4.undraw()
    latline5.undraw()
    longline1.undraw()
    longline2.undraw()
    longline3.undraw()
    longline4.undraw()
    longline5.undraw()
    leftlabel1.undraw()
    leftlabel2.undraw()
    leftlabel3.undraw()
    leftlabel4.undraw()
    toplabel1.undraw()
    toplabel2.undraw()
    toplabel3.undraw()
    toplabel4.undraw()
    hints.undraw()
    name1.undraw()
    name2.undraw()
    name3.undraw()
    name4.undraw()
    finalanswer1.undraw()
    finalanswer2.undraw()
    finalanswer3.undraw()
    finalanswer4.undraw()
    finish_puzzle.undraw()

    answers_two = [answer1, answer2, answer3, answer4]

    return answers_two

def catalogersdungeon():
    narration20 = "As you descend the staircase, the air\n" \
                  "grows colder and the light dimmer."
    narration21 = "The sound you heard before grows louder,\n" \
                  "and though you can't quite place it yet,\n" \
                  "it sounds familiar."
    narration22 = "Clackclackclackclack"
    narration23 = "At the bottom of the staircase, through\n" \
                  "the gloom you see a rusted metal door, a\n" \
                  "sign dangling from one screw in the upper\n" \
                  "right corner reading,\n\n" \
                  "'Catalog at your own risk.'"
    narration(narration20, 5)
    narration(narration21, 8)
    narration(narration22, 3)
    narration(narration23, 9)

    open_door = prompt("Open the door? >")
    open_door_reply = reply().getText().lower()
    open_door.undraw()
    if open_door_reply == "yes":
        narration25 = "You open the door as quietly as possible\n" \
                      "and suddenly the noise from before makes\n" \
                      "sense."
        narration26 = "Spread out before you is a seemingly\n" \
                      "endless room filled with the hazy blue\n" \
                      "glow of computer screens."
        narration27 = "At each of the terminals, a cataloger\n" \
                      "sits hunched over, fingers flying across\n" \
                      "their keyboards or clicking their mouse."
        narration28 = "Their bloodshot eyes reflect the glow\n" \
                      "of their computer screens eerily."
        narration(narration25, 6)
        narration(narration26, 6)
        narration(narration27, 7)
        narration(narration28, 5)

        cataloger_pic.draw(win)
        gherdialog1 = "???:\n\n" \
                      "What are you doing here?"
        dialog(gherdialog1, 3)

        narration29 = "The sharp, hissing whisper nearly\n" \
                      "makes you jump out of your skin and\n" \
                      "you turn to see one of the catalogers,\n" \
                      "their large glasses reflecting the\n" \
                      "light from a nearby monitor."
        narration(narration29, 8)
        cataloger_pic.undraw()

        playerdialog8 = str(player_name.upper() + ":\n\n"
                                              "I-I'm on a quest.")
        dialog(playerdialog8, 3)

        cataloger_pic.draw(win)
        gherdialog2 = "???:\n\n" \
                      "A quest? We don't have time for\n" \
                      "quests! There are materials that\n" \
                      "need describing!"
        dialog(gherdialog2, 5)
        cataloger_pic.undraw()

        playerdialog9 = str(player_name.upper() + ":\n\n"
                                              "I'm sorry, I promise I won't bother\n"
                                                  "you long. I'm just trying to collect\n"
                                                  "the LIBRARY RELICS to destroy the\n"
                                                  "TOME OF LENDING.")
        dialog(playerdialog9, 7)

        cataloger_pic.draw(win)
        narration30 = "The cataloger raises an eyebrow. You\n" \
                      "think they might be glaring at you, but\n" \
                      "you can't be sure."
        narration(narration30, 7)

        gherdialog3 = "???:\n\n" \
                      "You must mean the SPECTACLES OF\n" \
                      "COMPUTER SIGHT."
        dialog(gherdialog3, 4)
        cataloger_pic.undraw()

        playerdialog10 = str(player_name.upper() + ":\n\n"
                                              "Um... sure. Yes. Those.")
        dialog(playerdialog10, 3)

        cataloger_pic.draw(win)
        gherdialog4 = "???:\n\n" \
                      "The SPECTACLES are sacred to us\n" \
                      "catalogers. We won't part with them\n" \
                      "easily, not even for a quest like this."
        dialog(gherdialog4, 7.5)
        cataloger_pic.undraw()

        playerdialog11 = str(player_name.upper() + ":\n\n"
                                              "Please! I just want to help\n"
                                                   "our patrons!")
        dialog(playerdialog11, 4)

        cataloger_pic.draw(win)
        narration31 = "The cataloger stares at you\n" \
                      "unnervingly."
        narration(narration31, 4)
        gherdialog5 = "???:\n\n" \
                      "I suppose I might be able to... work\n" \
                      "something out. But you won't get them\n" \
                      "for free!"
        gherdialog6 = "GHER:\n\n" \
                      "I am VOYA GHER, Head Cataoging Tactician\n" \
                      "and Metadata Strategist."
        gherdialog7 = "GHER:\n\n" \
                      "As I mentioned, we are very busy here\n" \
                      "and after the debacle that was the last\n" \
                      "OCLC undercover retrieval mission we've\n" \
                      "had some... unexpected downsizing in our\n" \
                      "ranks."
        gherdialog8 = "GHER:\n\n" \
                      "If you can help me deliver these new\n" \
                      "materials to the proper cataloger, I'll\n" \
                      "give you the SPECTACLES. Sound fair?"
        dialog(gherdialog5, 6)
        dialog(gherdialog6, 5)
        dialog(gherdialog7, 9)
        dialog(gherdialog8, 7)
        cataloger_pic.undraw()

        play_puzzle = prompt("Play the puzzle? >")
        play_puzzle_reply = reply().getText().lower()
        play_puzzle.undraw()
        if play_puzzle_reply == "yes":
            playerdialog12 = str(player_name.upper() + ":\n\n"
                                              "I'll do my best.")
            dialog(playerdialog12, 3)
            textbox.undraw()
            answers_two = puzzletwo()
            if answers_two == ['rare books', 'serials', 'monographs', 'music']:
                textbox.draw(win)
                cataloger_pic.draw(win)
                gherdialog9 = "GHER:\n\n" \
                              "You'd make a pretty good\n" \
                              "cataloging peon..."
                gherdialog10 = "GHER:\n\n" \
                               "Well, I suppose you earned this.\n" \
                               "Here."
                dialog(gherdialog9, 4)
                dialog(gherdialog10, 4)
                cataloger_pic.undraw()

                spectacles_pic.draw(win)
                player_inventory.append(spectacles)
                narration34 = "The SPECTACLES OF COMPUTER SIGHT\n" \
                              "are now in your inventory!"
                narration(narration34, 4)

                inventory_check = player_name.upper() + "'s Inventory\n\n" + player_inventory[0] + '\n' + player_inventory[1] + '\n' + player_inventory[2] + '\n' + player_inventory[3] + '\n' + player_inventory[4]
                narration(inventory_check, 9)
                spectacles_pic.undraw()

                cataloger_pic.draw(win)
                gherdialog11 = "GHER:\n\n" \
                               "If the situation is as dire as you\n" \
                               "make it sound, you'd probably best\n" \
                               "get a move on."
                gherdialog12 = "GHER:\n\n" \
                               "I'll let you use my interdepartmental\n" \
                               "portal, if you like. It'll take you\n" \
                               "right outside the REFERENCE TAVERN."
                gherdialog13 = "GHER:\n\n" \
                               "Any question you have, I guarantee\n" \
                               "they've got the answer."
                dialog(gherdialog11, 6.5)
                dialog(gherdialog12, 7)
                dialog(gherdialog13, 5.5)

                narration35 = "GHER directs you to a shadowy alcove\n" \
                              "where a strange circle of glowing\n" \
                              "liquid seems to be floating on the wall."
                narration36 = "You try not to stare too much. After\n" \
                              "all, you've definitely read about\n" \
                              "interdepartmental portals and you\n" \
                              "don't want to look like too much of\n" \
                              "a newbie."
                narration37 = "GHER pokes at the glowing liquid a\n" \
                              "few times and then gestures for you\n" \
                              "to step forward."
                narration(narration35, 7)
                narration(narration36, 8)
                narration(narration37, 7)

                gherdialog14 = "GHER:\n\n" \
                               "In you go. I recommend you talk to\n" \
                               "VIEU PHIND. She can help you locate\n" \
                               "the next RELIC."
                dialog(gherdialog14, 6)
                cataloger_pic.undraw()

                playerdialog13 = str(player_name.upper() + ":\n\n"
                                              "Thanks.")
                dialog(playerdialog13, 2)

                through_portal = prompt("Step through the portal? >")
                through_portal_reply = reply().getText().lower()
                through_portal.undraw()
                if through_portal_reply == 'yes':
                    tavern_title = Image(Point(4, 2.5), 'tavern.gif')
                    tavern_title.draw(win)
                    time.sleep(5)
                    tavern_title.undraw()
                else:
                    narration38 = "You feel a hand on your back and\n" \
                                  "you are firmly pushed into the\n" \
                                  "portal. You are falling, and falling,\n" \
                                  "and falling, and falling..."
                    narration(narration38, 8)
                    mainmenu()
            else:
                narration33 = "Gher grins eerily and the sound of\n" \
                          "typing suddenly falls silent. Hundreds\n" \
                          "of identical, bespectacled stares turn\n" \
                          "towards you. You turn, but there is no\n" \
                          "longer a door behind you. A pair of\n" \
                          "glasses descends in front of your eyes\n" \
                          "and you know no more."
                narration(narration33, 12)
                mainmenu()
        else:
            narration32 = "Gher grins eerily and the sound of\n" \
                          "typing suddenly falls silent. Hundreds\n" \
                          "of identical, bespectacled stares turn\n" \
                          "towards you. You turn, but there is no\n" \
                          "longer a door behind you. A pair of\n" \
                          "glasses descends in front of your eyes\n" \
                          "and you know no more."
            narration(narration32, 12)
            mainmenu()
    else:
        narration24 = "You hear a sound much like a muffled\n" \
                      "scream. Shadowy hands suddenly burst\n" \
                      "from the rough stone walls and you are\n" \
                      "dragged into the darkness."
        narration(narration24, 8)
        mainmenu()

    return player_inventory


player_inventory = inventory(player_class)
player_inventory.append(cardigan)
textbox = textbox()
submit()
player_inventory = catalogersdungeon()
win.close()
