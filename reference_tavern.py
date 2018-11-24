# reference_tavern.py

# code for the reference tavern level

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

def puzzlethree():
    puzzlespace = Rectangle(Point(1.25, 1.25), Point(3.75, 3.75))
    puzzlespace.setWidth(2)
    puzzlespace.draw(win)

    latline1 = Line(Point(0.75, 2.25), Point(3.75, 2.25))
    latline2 = Line(Point(0.75, 2.75), Point(3.75, 2.75))
    latline3 = Line(Point(0.75, 3.25), Point(3.75, 3.25))
    latline4 = Line(Point(0.75, 3.75), Point(3.75, 3.75))
    latline5 = Line(Point(0.75, 1.75), Point(3.75, 1.75))
    latline6 = Line(Point(0.75, 1.25), Point(3.75, 1.25))
    latline1.draw(win)
    latline2.draw(win)
    latline3.draw(win)
    latline4.draw(win)
    latline5.draw(win)
    latline6.draw(win)

    longline1 = Line(Point(1.25, 1.25), Point(1.25, 4.25))
    longline2 = Line(Point(1.75, 1.25), Point(1.75, 4.25))
    longline3 = Line(Point(2.25, 1.25), Point(2.25, 4.25))
    longline4 = Line(Point(2.75, 1.25), Point(2.75, 4.25))
    longline5 = Line(Point(3.25, 1.25), Point(3.25, 4.25))
    longline6 = Line(Point(3.75, 1.25), Point(3.75, 4.25))
    longline1.draw(win)
    longline2.draw(win)
    longline3.draw(win)
    longline4.draw(win)
    longline5.draw(win)
    longline6.draw(win)

    leftlabel1 = Text(Point(0.8, 3.5), 'PsychInfo')
    leftlabel2 = Text(Point(0.8, 3), 'SportDiscus')
    leftlabel3 = Text(Point(0.8, 2.5), 'GreenFile')
    leftlabel4 = Text(Point(0.8, 2), 'Sociological\nAbstracts')
    leftlabel5 = Text(Point(0.8, 1.5), 'Genderwatch')
    toplabel1 = Text(Point(1.5, 4), "Magnus")
    toplabel2 = Text(Point(2, 4), "Barry")
    toplabel3 = Text(Point(2.5, 4), "Merle")
    toplabel4 = Text(Point(3, 4), "Angus")
    toplabel5 = Text(Point(3.5, 4), "Lup")
    leftlabel1.setFace('courier')
    leftlabel2.setFace('courier')
    leftlabel3.setFace('courier')
    leftlabel4.setFace('courier')
    leftlabel5.setFace('courier')
    toplabel1.setFace('courier')
    toplabel2.setFace('courier')
    toplabel3.setFace('courier')
    toplabel4.setFace('courier')
    toplabel5.setFace('courier')
    leftlabel1.draw(win)
    leftlabel2.draw(win)
    leftlabel3.draw(win)
    leftlabel4.draw(win)
    leftlabel5.draw(win)
    toplabel1.draw(win)
    toplabel2.draw(win)
    toplabel3.draw(win)
    toplabel4.draw(win)
    toplabel5.draw(win)

    hints = Text(Point(5.75, 3.5), "Five patrons need to find articles about their\n"
                                    "research topics. Which database is recommended\n"
                                    "to each patron?\n\n"
                                    "1) Lup does not care about any 'sportsball' games\n"
                                    "and she loudly declares this to any who will listen.\n\n"
                                    "2) Barry is curious about thirdwave feminist theory\n"
                                    "and wants to find some articles to read on the topic.\n\n"
                                    "3) Merle is in a rush to finish his final paper on\n"
                                    "species of beans adn needs four more citations.\n\n"
                                    "4) Angus is concerned about his parents' habit of\n"
                                    "personifying bird figurines and wants to know more\n"
                                    "about hallucinations.")
    hints.setFace('courier')
    hints.draw(win)

    name1 = Text(Point(4.5, 2.25), "Magnus >")
    name2 = Text(Point(4.5, 2), "Barry >")
    name3 = Text(Point(4.5, 1.75), "Merle >")
    name4 = Text(Point(4.5, 1.5), "Angus >")
    name5 = Text(Point(4.5, 1.25), "Lup >")
    name1.setFace('courier')
    name2.setFace('courier')
    name3.setFace('courier')
    name4.setFace('courier')
    name5.setFace('courier')
    name1.draw(win)
    name2.draw(win)
    name3.draw(win)
    name4.draw(win)
    name5.draw(win)

    answer1input = Entry(Point(6, 2.25), 25)
    answer1input.setText('')
    answer1input.setFill('white')
    answer1input.draw(win)
    win.getMouse()
    answer1input.undraw()
    answer1 = answer1input.getText().lower()
    finalanswer1 = Text(Point(6, 2.25), answer1)
    finalanswer1.setFace('courier')
    finalanswer1.draw(win)

    answer2input = Entry(Point(6, 2), 25)
    answer2input.setText('')
    answer2input.setFill('white')
    answer2input.draw(win)
    win.getMouse()
    answer2input.undraw()
    answer2 = answer2input.getText().lower()
    finalanswer2 = Text(Point(6, 2), answer2)
    finalanswer2.setFace('courier')
    finalanswer2.draw(win)

    answer3input = Entry(Point(6, 1.75), 25)
    answer3input.setText('')
    answer3input.setFill('white')
    answer3input.draw(win)
    win.getMouse()
    answer3input.undraw()
    answer3 = answer3input.getText().lower()
    finalanswer3 = Text(Point(6, 1.75), answer3)
    finalanswer3.setFace('courier')
    finalanswer3.draw(win)

    answer4input = Entry(Point(6, 1.5), 25)
    answer4input.setText('')
    answer4input.setFill('white')
    answer4input.draw(win)
    win.getMouse()
    answer4input.undraw()
    answer4 = answer4input.getText().lower()
    finalanswer4 = Text(Point(6, 1.5), answer4)
    finalanswer4.setFace('courier')
    finalanswer4.draw(win)

    answer5input = Entry(Point(6, 1.25), 25)
    answer5input.setText('')
    answer5input.setFill('white')
    answer5input.draw(win)
    win.getMouse()
    answer5input.undraw()
    answer5 = answer5input.getText().lower()
    finalanswer5 = Text(Point(6, 1.25), answer5)
    finalanswer5.setFace('courier')
    finalanswer5.draw(win)

    puzzlespace.undraw()
    latline1.undraw()
    latline2.undraw()
    latline3.undraw()
    latline4.undraw()
    latline5.undraw()
    latline6.undraw()
    longline1.undraw()
    longline2.undraw()
    longline3.undraw()
    longline4.undraw()
    longline5.undraw()
    longline6.undraw()
    leftlabel1.undraw()
    leftlabel2.undraw()
    leftlabel3.undraw()
    leftlabel4.undraw()
    leftlabel5.undraw()
    toplabel1.undraw()
    toplabel2.undraw()
    toplabel3.undraw()
    toplabel4.undraw()
    toplabel5.undraw()
    hints.undraw()
    name1.undraw()
    name2.undraw()
    name3.undraw()
    name4.undraw()
    name5.undraw()
    finalanswer1.undraw()
    finalanswer2.undraw()
    finalanswer3.undraw()
    finalanswer4.undraw()
    finalanswer5.undraw()
    finish_puzzle.undraw()

    answers_three = [answer1, answer2, answer3, answer4, answer5]

    return answers_three

def referencetavern():
    narration39 = "You pass through the portal and\n" \
                  "experience a sensation not unlike\n" \
                  "getting unceremoniously dropped in\n" \
                  "a puddle."
    narration40 = "As you emerge, spluttering on the\n" \
                  "other side, you are surprised to feel\n" \
                  "a comforting warmth accompanied by\n" \
                  "the sounds of gentle music and laughter."
    narration41 = "Before you, you see a cozy looking\n" \
                  "building with pleasant planters full\n" \
                  "of petunias sitting outside and a warm\n" \
                  "glow in the windows."
    narration42 = "Above the door, a handsome sign proclaims,\n\n" \
                  "'REFERENCE TAVERN'."
    narration(narration39, 8)
    narration(narration40, 8)
    narration(narration41, 8)
    narration(narration42, 5)

    enter_tavern = prompt("Enter the tavern? >")
    enter_tavern_response = reply().getText().lower()
    enter_tavern.undraw()
    if enter_tavern_response == "yes":
        narration44 = "You step through the door and are greeted\n" \
                      "by te sight of a charming room filled with\n" \
                      "tables and chatting patrons."
        narration45 = "At each table, a patron sits with a person\n" \
                      "in a uniform shirt, pouring over books or\n" \
                      "looking at convenient computer screens\n" \
                      "showing journal databases."
        narration46 = "Off to the side, you see two tables empty\n" \
                      "of patrons."
        narration47 = "At one, there is a young woman with\n" \
                      "impeccably done cat-eye eyeliner,\n" \
                      "smiling and waving you over."
        narration48 = "At the other, there is a cat, its\n" \
                      "eyes hypnotic and its fur appearing\n" \
                      "enticingly fluffy."
        narration(narration44, 7)
        narration(narration45, 8)
        narration(narration46, 3)
        narration(narration47, 7)
        narration(narration48, 7)

        pick_table = prompt("Which table do you approach? >")
        pick_table_reply = reply().getText().lower()
        pick_table.undraw()
        if pick_table_reply == "first":
            reference_pic.draw(win)
            phinddialog1 = "???:\n\n" \
                           "Welcome to the REFERENCE TAVERN!"
            phinddialog2 = "PHIND:\n\n" \
                           "I'm VIEU PHIND.\n" \
                           "How can I help you today?"
            dialog(phinddialog1, 3)
            dialog(phinddialog2, 3.5)
            reference_pic.undraw()

            playerdialog14 = str(player_name.upper() + ":\n\n"
                                              "Oh, well, I'm on a quest.")
            dialog(playerdialog14, 3)

            reference_pic.draw(win)
            phinddialog3 = "PHIND:\n\n" \
                           "A quest! How exciting!\n" \
                           "What is your quest?"
            dialog(phinddialog3, 4)
            reference_pic.undraw()

            playerdialog15 = str(player_name.upper() + ":\n\n"
                                              "I need to gather the LIBRARY RELICS so\n"
                                                       "that I can destroy the TOME OF LENDING.")
            dialog(playerdialog15, 5)

            reference_pic.draw(win)
            phinddialog4 = "PHIND:\n\n" \
                           "I see. That's a tricky task you have\n" \
                           "there. Where have you looked so far?"
            dialog(phinddialog4, 5)
            reference_pic.undraw()

            playerdialog16 = str(player_name.upper() + ":\n\n"
                                              "Well, first I went to the ARCHIVIST'S LAIR\n"
                                                       "and got the CARDIGAN OF INVISIBILITY.")
            dialog(playerdialog16, 5)

            reference_pic.draw(win)
            phinddialog5 = "PHIND:\n\n" \
                           "That's great! Archives have many excellent\n" \
                           "resources. How else have you approached\n" \
                           "your search?"
            dialog(phinddialog5, 6)
            reference_pic.undraw()

            playerdialog17 = str(player_name.upper() + ":\n\n"
                                              "Um... I went to the CATALOGER'S DUNGEON\n"
                                                       "next and got the SPECTACLES OF COMPUTER\n"
                                                       "SIGHT.")
            dialog(playerdialog17, 5)

            reference_pic.draw(win)
            phinddialog6 = "PHIND:\n\n" \
                           "Fantastic! Since catalogers are\n" \
                           "responsible for creating records so\n" \
                           "that users can find materials in the\n" \
                           "Library, they are excellent comrades\n" \
                           "when designing a search strategy."
            phinddialog7 = "PHIND:\n\n" \
                           "You seem to be doing well in your\n" \
                           "search so far. Tell me a little\n" \
                           "more about your quest."
            dialog(phinddialog6, 8)
            dialog(phinddialog7, 5)
            reference_pic.undraw()

            playerdialog18 = str(player_name.upper() + ":\n\n"
                                              "Well, VOYA GHER sent me up here and\n"
                                                       "suggested I speak with you about finding\n"
                                                       "the next RELIC, though I'm not sure what\n"
                                                       "it is.")
            dialog(playerdialog18, 7.5)

            reference_pic.draw(win)
            phinddialog8 = "PHIND:\n\n" \
                           "Oh! VOYA sent you?! They are such a\n" \
                           "sweetheart!"
            dialog(phinddialog8, 4.5)
            reference_pic.undraw()

            playerdialog19 = str(player_name.upper() + ":\n\n"
                                              "S-Sure...")
            dialog(playerdialog19, 3)

            reference_pic.draw(win)
            phinddialog9 = "PHIND:\n\n" \
                           "Well, if VOYA sent you, it must be\n" \
                           "very urgent, your quest."
            phinddialog10 = "PHIND:\n\n" \
                            "So you're looking for the next\n" \
                            "LIBRARY RELIC... Let me see..."
            dialog(phinddialog9, 4.5)
            dialog(phinddialog10, 4.5)

            narration50 = "PHIND turns to the computer sitting on\n" \
                          "the table, turning the screen towards you."
            narration(narration50, 5)

            phinddialog11 = "PHIND:\n\n" \
                            "The first thing to do is open up the\n" \
                            "Library catalog. Up at the top of the\n" \
                            "page, you'll see a search box."
            phinddialog12 = "PHIND:\n\n" \
                            "Let's try typing in 'library' AND 'relic'\n" \
                            "to see what we have in our holdings."
            phinddialog13 = "PHIND:\n\n" \
                            "Oh! Look at that! It looks like we have\n" \
                            "four LIBRARY RELICS. Two of them are\n" \
                            "checked out, but it looks like the other\n" \
                            "two are available."
            phinddialog14 = "PHIND:\n\n" \
                            "Let's see... Looks like the THOUSAND SHELF\n" \
                            "BOOKCART is the CASTLE OF STACKS and the\n" \
                            "BOTTOMLESS MUG is..."
            phinddialog15 = "PHIND:\n\n" \
                            "Oh! Well, I guess it's your lucky day. It\n" \
                            "seems the BOTTOMLESS MUG is here at the\n" \
                            "REFERENCE TAVERN!"
            phinddialog16 = "PHIND:\n\n" \
                            "Hmm... it seems it's a\n" \
                            "non-circulating item..."
            dialog(phinddialog11, 7)
            dialog(phinddialog12, 6)
            dialog(phinddialog13, 8)
            dialog(phinddialog14, 7)
            dialog(phinddialog15, 7)
            dialog(phinddialog16, 4)
            reference_pic.undraw()

            playerdialog20 = str(player_name.upper() + ":\n\n"
                                              "Oh man... I really need it, though.\n"
                                                       "Is there any way you can make an\n"
                                                       "exception?")
            dialog(playerdialog20, 6)

            reference_pic.draw(win)
            narration51 = "PHIND looks at you, face thoughtful.\n" \
                          "You give her the best puppy-dog eyes you\n" \
                          "can muster. It's one of your many hidden\n" \
                          "talents, after all."
            narration(narration51, 8)
            phinddialog17 = "PHIND:\n\n" \
                            "Well... I suppose I might be able to make\n" \
                            "an exception... But I'll need a favor from\n" \
                            "you first."
            phinddialog18 = "PHIND:\n\n" \
                            "I've got some patrons on chat that need\n" \
                            "database recommendations. If you help\n" \
                            "direct them to the right databases, I'll\n" \
                            "give you the MUG."
            phinddialog19 = "PHIND:\n\n" \
                            "Sound fair?"
            dialog(phinddialog17, 8)
            dialog(phinddialog18, 9)
            dialog(phinddialog19, 3)
            reference_pic.undraw()

            play_puzzle = prompt("Play the puzzle? >")
            play_puzzle_response = reply().getText().lower()
            play_puzzle.undraw()
            if play_puzzle_response == "yes":
                playerdialog21 = str(player_name.upper() + ":\n\n"
                                              "I'll do my best.")
                dialog(playerdialog21, 3)
                textbox.undraw()
                answers_three = puzzlethree()
                if answers_three == ['sportdiscus', 'genderwatch', 'greenfile', 'psychinfo', 'sociological abstracts']:
                    textbox.draw(win)
                    reference_pic.draw(win)
                    phinddialog20 = "PHIND:\n\n" \
                                    "Wow! You're pretty good at this!"
                    phinddialog21 = "PHIND:\n\n" \
                                    "Fair's fair, here you go."
                    dialog(phinddialog20, 3)
                    dialog(phinddialog21, 3)
                    reference_pic.undraw()

                    mug_pic.draw(win)
                    player_inventory.append(mug)
                    narration54 = "The BOTTOMLESS MUG is now\n" \
                                  "in your inventory!"
                    narration(narration54, 4)

                    inventory_check = player_name.upper() + "'s Inventory\n\n" + player_inventory[0] + '\n' + player_inventory[1] + '\n' + player_inventory[2] + '\n' + player_inventory[3] + '\n' + player_inventory[4] + '\n' + player_inventory[5]
                    narration(inventory_check, 10)
                    mug_pic.undraw()

                    reference_pic.draw(win)
                    phinddialog22 = "PHIND:\n\n" \
                                    "Our catalog search showed that the last\n" \
                                    "RELIC is in the CASTLE OF STACKS. Let\n" \
                                    "me see..."
                    phinddialog23 = "PHIND:\n\n" \
                                    "Okay, it looks like the directtons have\n" \
                                    "been included here in the catalog record."
                    phinddialog24 = "PHIND:\n\n" \
                                    "Remember these! Any wrong turn in the\n" \
                                    "STACKS could leave you wandering aimlessly\n" \
                                    "for eternity."
                    phinddialog25 = "PHIND:\n\n" \
                                    "Alright, you'll head down to the lowest\n" \
                                    "and then the directions are..."
                    dialog(phinddialog22, 7)
                    dialog(phinddialog23, 7)
                    dialog(phinddialog24, 7)
                    dialog(phinddialog25, 6)

                    narration55 = Text(Point(4.875, 2.875), "Once you enter the STACKS, go:\n" \
                                  "LEFT, RIGHT, RIGHT, FORWARD,\n" \
                                  "LEFT, FORWARD, RIGHT.")
                    narration55.setFace('courier')
                    narration55.setSize(20)
                    narration55.setStyle('italic')
                    narration55.draw(win)

                    directions = prompt("Got it? >")

                    win.getMouse()

                    narration55.undraw()
                    directions.undraw()

                    phinddialog26 = "PHIND:\n\n" \
                                    "You can find the door to the STACKS\n" \
                                    "just up those stairs, at the back of\n" \
                                    "the room."
                    phinddialog27 = "PHIND:\n\n" \
                                    "Have a good quest!"
                    dialog(phinddialog26, 7)
                    dialog(phinddialog27, 3)
                    reference_pic.undraw()

                    playerdialog22 = str(player_name.upper() + ":\n\n"
                                              "Thanks, you too.")
                    dialog(playerdialog22, 3)

                    narration56 = "You and PHIND stare at each other for\n" \
                                  "a long, awkward moment before you turn\n" \
                                  "and beat a hasty retreat."
                    narration57 = "At the back of the room, you find the\n" \
                                  "stairs PHIND mentioned."
                    narration(narration56, 8)
                    narration(narration57, 6)

                    ascend_stairs = prompt("Ascend the stairs? >")
                    ascend_stairs_reply = reply().getText().lower()
                    ascend_stairs.undraw()
                    if ascend_stairs_reply == "yes":
                        castle_title = Image(Point(4, 2.5), 'tavern.gif')
                        castle_title.draw(win)
                        time.sleep(5)
                        castle_title.undraw()
                    else:
                        narration58 = "You hesitate and glance back. The\n" \
                                      "cat stares at you with it's soulful\n" \
                                      "eyes. Perhaps... perhaps you'd be\n" \
                                      "better off petting it..."
                        narration(narration58, 9)
                        mainmenu()
                else:
                    narration53 = "PHIND grins and reaches up. Her fingers\n" \
                                  "seem to peel away her face and suddenly\n" \
                                  "you realize it is a mask. She hands you\n" \
                                  "the enchanted customer service mask. You\n" \
                                  "take it, resigned to an eternity trapped\n" \
                                  "in customer service."
                    narration(narration53, 12)
                    mainmenu()
            else:
                narration52 = "PHIND shrugs and directs you towards\n" \
                              "the table with the cat. You find\n" \
                              "minimal comfort as you pet it, and\n" \
                              "pet it, and pet it..."
                narration(narration52, 8)
                mainmenu()
        else:
            narration49 = "The cat is indeed as fluffy as it\n" \
                          "appeared. Time seems to slip away\n" \
                          "from you as you continue to pet it,\n" \
                          "and pet it, and pet it, and pet it...."
            narration(narration49, 8)
            mainmenu()
    else:
        narration43 = "The comforting feeling dissipates and\n" \
                      "is replaced by a poignant feeling of\n" \
                      "foreboding. You hear a sound and turn\n" \
                      "to see an ominous forest behind you. One\n" \
                      "pair of eyes, then two, three, four,\n" \
                      "appear in the shadows. No one hears you\n" \
                      "scream."
        narration(narration43, 12)
        mainmenu()


    return player_inventory


player_inventory = inventory(player_class)
player_inventory.append(cardigan)
player_inventory.append(spectacles)
textbox = textbox()
submit()
player_inventory = referencetavern()
win.close()
