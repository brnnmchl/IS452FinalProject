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

def credit():
    header = Text(Point(4.0, 3.5), "LIBRARY QUEST")
    header.setFace('courier')
    header.setSize(20)
    header.draw(win)
    credits1 = Text(Point(2.0, 2.25), "(c) 2018 Brinna Michael\n\n"
                                     "Written by: Brinna Michael\n"
                                     "Art by: Brinna Michael")
    credits1.setFace('courier')
    credits1.setSize(15)
    credits1.draw(win)
    credits2 = Text(Point(6.0, 2.25), "I would like to thank\n"
                                      "my very patient roommate,\n"
                                      "Andrea, and my extremely\n"
                                      "supportive friends and\n"
                                      "family for being my guinea\n"
                                      "pigs and cheer squad.")
    credits2.setFace('courier')
    credits2.setSize(15)
    credits2.draw(win)
    exit = Button(Point(0.75, 0.625), 0.5, 0.25, 'Exit', 'tomato', 12, win)
    exit.activate()
    clickPoint = win.getMouse()
    if exit.clicked(clickPoint):
        win.close()


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


# game code

## Main Menu
mainmenu = Menu()
menu = mainmenu.startScreen('Library Quest', win)

play = Button(Point(4, 2.5), 1, 0.5, "Play?", 'pale green', 20, win)
play.activate()
clickPoint = win.getMouse()
play.remove()
menu.undraw()

if play.clicked(clickPoint):
    mainmenu.startNarration(narration_list[0], 12, win)
    prompt1 = mainmenu.startPrompt('Open the door? >', win)
    reply1 = mainmenu.startReply(win)
    submit = Button(Point(7.25, 0.625), 0.5, 0.25, 'Submit', 'pale green', 12, win)
    submit.activate()
    clickPoint = win.getMouse()
    if submit.clicked(clickPoint):
        submit.deactivate()
        open_door = reply1.getText().lower()
        if open_door == "yes":
            prompt1.undraw()
            reply1.undraw()
            mainmenu.startNarration('Welcome to...', 3, win)
            mainmenu.titlecard("logo.gif", win)

            ## Introduction
            textbox_outline = textbox()
            exit = Button(Point(0.75, 0.625), 0.5, 0.25, 'Exit', 'tomato', 12, win)
            exit.activate()

            intro = Intro()
            intro.narration(narration_list[1], 4, win)
            agnes = intro.setIcon('agnes.gif')
            agnes.draw(win)
            intro.dialog(dialog_list[0], 5.5, win)
            prompt2 = intro.prompt('Enter player name: >', win)
            reply2 = intro.reply(win)
            submit.activate()
            clickPoint = win.getMouse()
            if submit.clicked(clickPoint):
                prompt2.undraw()
                reply2.undraw()
                submit.deactivate()
                player_name = reply2.getText()

                intro.dialog("AGNES:\n\n" \
                   "It's a pleasure to meet you, \n" + player_name.upper() + '.', 4, win)
                intro.dialog(dialog_list[1], 7, win)
                intro.dialog(dialog_list[2], 4, win)

                class_options = Text(Point(4.875, 2.875), narration_list[2])
                class_options.setFace('courier')
                class_options.setSize(20)
                class_options.setStyle('italic')
                class_options.draw(win)

                prompt3 = intro.prompt('Choose player class: >', win)
                reply3 = intro.reply(win)
                submit.activate()
                clickPoint = win.getMouse()
                if submit.clicked(clickPoint):
                    prompt3.undraw()
                    reply3.undraw()
                    class_options.undraw()
                    submit.deactivate()
                    player_class = reply3.getText()
                    player_inventory = intro.setInventory(player_class)

                    intro.dialog(dialog_list[3], 8, win)
                    agnes.undraw()
                    intro.narration(narration_list[3], 6, win)

                    agnes.draw(win)
                    intro.dialog(dialog_list[4], 4, win)
                    agnes.undraw()

                    clarence = intro.setIcon('clarence.gif')
                    clarence.draw(win)
                    intro.dialog(dialog_list[5], 5, win)
                    clarence.undraw()

                    agnes.draw(win)
                    intro.dialog(dialog_list[6], 3.5, win)
                    agnes.undraw()

                    clarence.draw(win)
                    intro.dialog(dialog_list[7], 7, win)
                    intro.dialog(dialog_list[8], 5, win)
                    clarence.undraw()

                    agnes.draw(win)
                    intro.dialog(dialog_list[9], 8, win)
                    agnes.undraw()

                    clarence.draw(win)
                    intro.dialog(str("CLARENCE:\n\n" \
                      "Wait... You must be the new\n" + player_class + "!"), 5, win)
                    intro.dialog(dialog_list[10], 6, win)
                    intro.dialog(dialog_list[11], 8, win)
                    clarence.undraw()

                    intro.dialog(str(player_name.upper() + ":\n\n" \
                                  "The LIBRARY RELICS?"), 3, win)

                    clarence.draw(win)
                    intro.dialog(dialog_list[12], 4, win)
                    intro.dialog(dialog_list[13], 8, win)
                    clarence.undraw()

                    agnes.draw(win)
                    intro.dialog(dialog_list[14], 8, win)
                    intro.dialog(dialog_list[15], 6, win)
                    intro.dialog(str("AGNES:\n\n" + player_name.upper() + ", will you\n" \
                                                 "take on this quest?"), 4.5, win)
                    agnes.undraw()

                    prompt4 = intro.prompt("Take the quest? >", win)
                    reply4 = intro.reply(win)
                    submit.activate()
                    clickPoint = win.getMouse()
                    if submit.clicked(clickPoint):
                        prompt4.undraw()
                        reply4.undraw()
                        submit.deactivate()
                        takequest = reply4.getText().lower()
                        if takequest == "yes":
                            agnes.draw(win)
                            intro.dialog(dialog_list[16], 3, win)
                            intro.dialog(dialog_list[17], 3, win)
                            intro.narration(narration_list[4], 8, win)
                            intro.dialog(dialog_list[18], 7, win)
                            agnes.undraw()

                            clarence.draw(win)
                            intro.dialog(str("CLARENCE:\n\n" \
                                    "Good luck, " + player_name.upper() + '.'), 3.5, win)
                            clarence.undraw()

                            intro.dialog(str(player_name.upper() + ":\n\n"
                                              "T-Thanks."), 3, win)
                            intro.narration(narration_list[5], 7, win)

                            prompt5 = intro.prompt('Descend the stairs? >', win)
                            reply5 = intro.reply(win)
                            submit.activate()
                            clickPoint = win.getMouse()
                            if submit.clicked(clickPoint):
                                prompt5.undraw()
                                reply5.undraw()
                                submit.deactivate()
                                takestairs = reply5.getText().lower()
                                if takestairs == "yes":
                                    ## Archivist's Lair
                                    intro.titlecard('archive.gif', win)
                                    lair = Lair()
                                    lair.narration(narration_list[6], 8, win)
                                    lair.narration(narration_list[7], 4, win)

                                    prompt6 = lair.prompt('Open the door? >', win)
                                    reply6 = lair.reply(win)
                                    submit.activate()
                                    clickPoint = win.getMouse()
                                    if submit.clicked(clickPoint):
                                        prompt6.undraw()
                                        reply6.undraw()
                                        submit.deactivate()
                                        open_door = reply6.getText().lower()
                                        if open_door == "yes":
                                            lair.narration(narration_list[8], 8, win)
                                            lair.narration(narration_list[9], 7, win)
                                            lair.narration(narration_list[10], 7, win)
                                            lair.narration(narration_list[11], 4, win)
                                            lair.narration(narration_list[12], 9, win)
                                            lair.narration(narration_list[13], 8, win)
                                            archivist = lair.setIcon('archivist.gif')
                                            archivist.draw(win)
                                            lair.narration(narration_list[14], 6, win)
                                            lair.narration(narration_list[15], 8, win)
                                            lair.narration(narration_list[16], 7, win)
                                            lair.narration(narration_list[17], 6, win)
                                            lair.dialog(dialog_list[19], 8, win)
                                            archivist.undraw()

                                            lair.dialog(str(player_name.upper() + ":\n\n"
                                              "I'm " + player_name.upper() + ", the new\n" + player_class + "."), 4, win)

                                            archivist.draw(win)
                                            lair.dialog(dialog_list[20], 6, win)
                                            lair.dialog(dialog_list[21], 6, win)
                                            lair.dialog(dialog_list[22], 5, win)
                                            lair.dialog(dialog_list[23], 6.5, win)
                                            lair.dialog(dialog_list[24], 6, win)
                                            lair.dialog(dialog_list[25], 5, win)
                                            archivist.undraw()

                                            lair.dialog(str(player_name.upper() + ":\n\n"
                                              "Um... no. Not really,\n"
                                              "but I'll keep it in mind."), 4.5, win)

                                            archivist.draw(win)
                                            lair.dialog(dialog_list[26], 4.5, win)
                                            archivist.undraw()

                                            lair.dialog(str(player_name.upper() + ":\n\n"
                                              "Well, I was sent to gather the\n"
                                                  "LIBRARY RELICS in order to destroy\n"
                                                  "the TOME OF LENDING. AGNES told me\n"
                                                  "I would find one of them here."), 8, win)

                                            archivist.draw(win)
                                            lair.dialog("KNOPE:\n\n" \
                                                "Hmm... I might just have what you're\n" \
                                                "looking for, but one can't simply go\n" \
                                                "around handing out RELICS to every\n" \
                                                "random " + player_class + " who comes\n" \
                                                  "by looking for it.", 8, win)
                                            lair.dialog(dialog_list[27], 5, win)
                                            archivist.undraw()

                                            lair.dialog(str(player_name.upper() + ":\n\n"
                                              "Look, it's really important."), 4, win)

                                            archivist.draw(win)
                                            lair.dialog(dialog_list[28], 3.5, win)
                                            lair.dialog(dialog_list[29], 3.5, win)
                                            lair.dialog(dialog_list[30], 6, win)
                                            lair.dialog(dialog_list[31], 6, win)
                                            lair.dialog(dialog_list[32], 4, win)
                                            archivist.undraw()

                                            prompt7 = lair.prompt('Play the puzzle? >', win)
                                            reply7 = lair.reply(win)
                                            submit.activate()
                                            clickPoint = win.getMouse()
                                            if submit.clicked(clickPoint):
                                                prompt7.undraw()
                                                reply7.undraw()
                                                submit.deactivate()
                                                playpuzzle = reply7.getText().lower()
                                                if playpuzzle == "yes":
                                                    lair.dialog(str(player_name.upper() + ":\n\n"
                                                        "Okay, I'll do it."), 3, win)

                                                    archivist.draw(win)
                                                    lair.dialog(dialog_list[33], 3, win)
                                                    archivist.undraw()

                                                    textbox_outline.undraw()
                                                    answers_one = lair.puzzle(win)
                                                    if answers_one == ['hollinger box', 'microspatula', 'cotton gloves']:
                                                        textbox_outline.draw(win)
                                                        archivist.draw(win)
                                                        lair.dialog(dialog_list[34], 5.5, win)
                                                        lair.dialog(dialog_list[35], 4, win)
                                                        archivist.undraw()

                                                        cardigan_pic = lair.setIcon('cardigan.gif')
                                                        cardigan_pic.draw(win)
                                                        lair.addInventory(player_inventory, cardigan)
                                                        lair.narration(narration_list[18], 5, win)
                                                        lair.narration(player_name.upper() + "'s Inventory\n\n" + player_inventory[0] + '\n' + player_inventory[1] + '\n' + player_inventory[2] + '\n' + player_inventory[3], 8, win)
                                                        cardigan_pic.undraw()

                                                        archivist.draw(win)
                                                        lair.dialog(dialog_list[36], 7, win)
                                                        archivist.undraw()

                                                        lair.dialog(str(player_name.upper() + ":\n\n"
                                                            "Um... that sounds..."), 3, win)

                                                        archivist.draw(win)
                                                        lair.dialog(dialog_list[37], 5, win)
                                                        lair.dialog("KNOPE:\n\n" \
                                                            "But you'd best be running along now!\n" \
                                                            "I've got far to much processing to do\n" \
                                                            "to be babysitting a new " + player_class + ".", 7, win)
                                                        lair.dialog(dialog_list[38], 7, win)
                                                        lair.dialog(dialog_list[39], 3, win)
                                                        archivist.undraw()

                                                        lair.narration(narration_list[19], 5, win)
                                                        lair.narration(narration_list[20], 8, win)

                                                        prompt8 = lair.prompt("Descend the stairs? >", win)
                                                        reply8 = lair.reply(win)
                                                        submit.activate()
                                                        clickPoint = win.getMouse()
                                                        if submit.clicked(clickPoint):
                                                            prompt8.undraw()
                                                            reply8.undraw()
                                                            submit.deactivate()
                                                            takestairs = reply8.getText().lower()
                                                            if takestairs == "yes":
                                                                ## Cataloger's Dungeon
                                                                lair.titlecard('dungeon.gif', win)
                                                                dungeon = Dungeon()
                                                                dungeon.narration(narration_list[21], 5, win)
                                                                dungeon.narration(narration_list[22], 8, win)
                                                                dungeon.narration(narration_list[23], 3, win)
                                                                dungeon.narration(narration_list[24], 10, win)

                                                                prompt9 = dungeon.prompt('Open the door? >', win)
                                                                reply9 = dungeon.reply(win)
                                                                submit.activate()
                                                                clickPoint = win.getMouse()
                                                                if submit.clicked(clickPoint):
                                                                    prompt9.undraw()
                                                                    reply9.undraw()
                                                                    submit.deactivate()
                                                                    open_door = reply9.getText().lower()
                                                                    if open_door == "yes":
                                                                        dungeon.narration(narration_list[25], 7, win)
                                                                        dungeon.narration(narration_list[26], 7, win)
                                                                        dungeon.narration(narration_list[27], 7, win)
                                                                        dungeon.narration(narration_list[28], 5, win)

                                                                        cataloger = dungeon.setIcon("cataloger.gig", win)
                                                                        cataloger.draw(win)
                                                                        dungeon.dialog(dialog_list[40], 3, win)
                                                                        dungeon.narration(narration_list[29], 10, win)
                                                                        cataloger.undraw()

                                                                        dungeon.dialog(str(player_name.upper() + ":\n\n"
                                                                            "I-I'm on a quest."), 3, win)

                                                                        cataloger.draw(win)
                                                                        dungeon.dialog(dialog_list[41], 6, win)
                                                                        cataloger.undraw()

                                                                        dungeon.dialog(str(player_name.upper() + ":\n\n"
                                                                            "I'm sorry, I promise I won't bother\n"
                                                                            "you long. I'm just trying to collect\n"
                                                                            "the LIBRARY RELICS to destroy the\n"
                                                                            "TOME OF LENDING."), 8, win)

                                                                        cataloger.draw(win)
                                                                        dungeon.narration(narration_list[30], 7, win)
                                                                        dungeon.dialog(dialog_list[42], 4.5, win)
                                                                        cataloger.undraw()

                                                                        dungeon.dialog(str(player_name.upper() + ":\n\n"
                                                                            "Um... sure. Yes. Those."), 4, win)

                                                                        cataloger.draw(win)
                                                                        dungeon.dialog(dialog_list[43], 8, win)
                                                                        cataloger.undraw()

                                                                        dungeon.dialog(str(player_name.upper() + ":\n\n"
                                                                            "Please! I just want to help\n"
                                                                            "our patrons!"), 5, win)

                                                                        cataloger.draw(win)
                                                                        dungeon.narration(narration_list[31], 4, win)
                                                                        dungeon.dialog(dialog_list[44], 6, win)
                                                                        dungeon.dialog(dialog_list[45], 5, win)
                                                                        dungeon.dialog(dialog_list[46], 10, win)
                                                                        dungeon.dialog(dialog_list[47], 7, win)
                                                                        cataloger.undraw()

                                                                        prompt10 = dungeon.prompt("Play the puzzle? >", win)
                                                                        reply10 = dungeon.reply(win)
                                                                        submit.activate()
                                                                        clickPoint = win.getMouse()
                                                                        if submit.clicked(clickPoint):
                                                                            prompt10.undraw()
                                                                            reply10.undraw()
                                                                            submit.deactivate()
                                                                            playpuzzle = reply10.getText().lower()
                                                                            if playpuzzle == "yes":
                                                                                dungeon.dialog(str(player_name.upper() + ":\n\n"
                                                                                    "I'll do my best."), 3, win)

                                                                                textbox_outline.undraw()
                                                                                answers_two = dungeon.puzzle(win)
                                                                                if answers_two == ['rare books', 'serials', 'monographs', 'music']:
                                                                                    textbox_outline.draw(win)
                                                                                    cataloger.draw(win)
                                                                                    dungeon.dialog(dialog_list[48], 4, win)
                                                                                    dungeon.dialog(dialog_list[49], 4, win)
                                                                                    cataloger.undraw()

                                                                                    spectacles_pic = dungeon.setIcon('spectacles.gif', win)
                                                                                    spectacles_pic.draw(win)
                                                                                    dungeon.addInventory(player_inventory, spectacles)
                                                                                    dungeon.narration(narration_list[32], 5, win)
                                                                                    dungeon.narration(player_name.upper() + "'s Inventory\n\n" + player_inventory[0] + '\n' + player_inventory[1] + '\n' + player_inventory[2] + '\n' + player_inventory[3] + '\n' + player_inventory[4], 10, win)
                                                                                    spectacles_pic.undraw()

                                                                                    cataloger.draw(win)
                                                                                    dungeon.dialog(dialog_list[50], 7, win)
                                                                                    dungeon.dialog(dialog_list[51], 7, win)
                                                                                    dungeon.dialog(dialog_list[52], 5, win)
                                                                                    dungeon.narration(narration_list[33], 7, win)
                                                                                    dungeon.narration(narration_list[34], 9, win)
                                                                                    dungeon.narration(narration_list[35], 7, win)
                                                                                    dungeon.dialog(dialog_list[53], 7, win)
                                                                                    cataloger.undraw()

                                                                                    dungeon.dialog(str(player_name.upper() + ":\n\n"
                                                                                            "Thanks."), 3, win)

                                                                                    prompt11 = dungeon.prompt("Step through the portal? >", win)
                                                                                    reply11 = dungeon.reply(win)
                                                                                    submit.activate()
                                                                                    clickPoint = win.getMouse()
                                                                                    if submit.clicked(clickPoint):
                                                                                        prompt11.undraw()
                                                                                        reply11.undraw()
                                                                                        submit.deactivate()
                                                                                        through_portal = reply11.getText().lower()
                                                                                        if through_portal == "yes":
                                                                                            ## Reference Tavern
                                                                                            dungeon.titlecard('tavern.gif', win)

                                                                                        else:
                                                                                            dungeon.narration(bad_endings_list[6], 9, win)
                                                                                            credit()
                                                                                else:
                                                                                    textbox_outline.draw(win)
                                                                                    dungeon.narration(bad_endings_list[7], 13, win)
                                                                                    credit()
                                                                            else:
                                                                                dungeon.narration(bad_endings_list[7], 13, win)
                                                                                credit()
                                                                    else:
                                                                        dungeon.narration(bad_endings_list[8], 10, win)
                                                                        credit()
                                                            else:
                                                                prompt8.undraw()
                                                                reply8.undraw()
                                                                submit.deactivate()
                                                                lair.narration(bad_endings_list[2], 6, win)
                                                                credit()
                                                    else:
                                                        textbox_outline.draw(win)
                                                        lair.narration(bad_endings_list[3], 7, win)
                                                        credit()
                                                else:
                                                    prompt7.undraw()
                                                    reply7.undraw()
                                                    submit.deactivate()
                                                    lair.narration(bad_endings_list[4], 10, win)
                                                    credit()
                                        else:
                                            prompt6.undraw()
                                            reply6.undraw()
                                            submit.deactivate()
                                            lair.narration(bad_endings_list[5], 12, win)
                                            credit()
                                else:
                                    prompt5.undraw()
                                    reply5.undraw()
                                    submit.deactivate()
                                    intro.narration(bad_endings_list[1], 7, win)
                                    credit()
                        else:
                            prompt4.undraw()
                            reply4.undraw()
                            submit.deactivate()
                            intro.narration(bad_endings_list[2], 7, win)
                            credit()
                elif exit.clicked(clickPoint):
                    credit()
            elif exit.clicked(clickPoint):
                credit()
        else:
            prompt1.undraw()
            reply1.undraw()
            mainmenu.startNarration(bad_endings_list[0], 9, win)
            credit()





