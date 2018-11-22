# archivists_lair.py

# this is the code for the archivist's lair level

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

def puzzleone():
    puzzlespace = Rectangle(Point(1.25, 2.25), Point(2.75, 3.75))
    puzzlespace.setWidth(2)
    puzzlespace.draw(win)

    latline1 = Line(Point(0.75, 2.25), Point(2.75, 2.25))
    latline2 = Line(Point(0.75, 2.75), Point(2.75, 2.75))
    latline3 = Line(Point(0.75, 3.25), Point(2.75, 3.25))
    latline4 = Line(Point(0.75, 3.75), Point(2.75, 3.75))
    latline1.draw(win)
    latline2.draw(win)
    latline3.draw(win)
    latline4.draw(win)

    longline1 = Line(Point(1.25, 2.25), Point(1.25, 4.25))
    longline2 = Line(Point(1.75, 2.25), Point(1.75, 4.25))
    longline3 = Line(Point(2.25, 2.25), Point(2.25, 4.25))
    longline4 = Line(Point(2.75, 2.25), Point(2.75, 4.25))
    longline1.draw(win)
    longline2.draw(win)
    longline3.draw(win)
    longline4.draw(win)

    leftlabel1 = Text(Point(0.9, 3.5), 'Micro-\n'
                                        'spatula')
    leftlabel2 = Text(Point(0.9, 3), 'Cotton\n'
                                        'gloves')
    leftlabel3 = Text(Point(0.9, 2.5), 'Hollinger\n'
                                        'box')
    toplabel1 = Text(Point(1.5, 4), "BBNK")
    toplabel2 = Text(Point(2, 4), "EAD")
    toplabel3 = Text(Point(2.5, 4), "M.PLP")
    leftlabel1.setFace('courier')
    leftlabel2.setFace('courier')
    leftlabel3.setFace('courier')
    toplabel1.setFace('courier')
    toplabel2.setFace('courier')
    toplabel3.setFace('courier')
    leftlabel1.draw(win)
    leftlabel2.draw(win)
    leftlabel3.draw(win)
    toplabel1.draw(win)
    toplabel2.draw(win)
    toplabel3.draw(win)

    hints = Text(Point(5.75, 4), "Materials have gone missing in the archive!\n"
                                 "Who was last seen with these items?\n\n"
                                 "1) Mr. Platt requested to view a record\n"
                                 "series titled 'Photographic Subject File.'\n\n"
                                 "2) Ed works for the preservation department\n"
                                 "and does not box up materials.")
    hints.setFace('courier')
    hints.draw(win)

    name1 = Text(Point(4.5, 3), "B.B.N. Knope >")
    name2 = Text(Point(4.5, 2.5), "Ed A. Danvers >")
    name3 = Text(Point(4.5, 2), "Mr. Percy L. Platt >")
    name1.setFace('courier')
    name2.setFace('courier')
    name3.setFace('courier')
    name1.draw(win)
    name2.draw(win)
    name3.draw(win)

    answer1input = Entry(Point(6.5, 3), 15)
    answer1input.setText('')
    answer1input.setFill('white')
    answer1input.draw(win)
    win.getMouse()
    answer1input.undraw()
    answer1 = answer1input.getText().lower()
    finalanswer1 = Text(Point(6.5, 3), answer1)
    finalanswer1.setFace('courier')
    finalanswer1.draw(win)

    answer2input = Entry(Point(6.5, 2.5), 15)
    answer2input.setText('')
    answer2input.setFill('white')
    answer2input.draw(win)
    win.getMouse()
    answer2input.undraw()
    answer2 = answer2input.getText().lower()
    finalanswer2 = Text(Point(6.5, 2.5), answer2)
    finalanswer2.setFace('courier')
    finalanswer2.draw(win)

    answer3input = Entry(Point(6.5, 2), 15)
    answer3input.setText('')
    answer3input.setFill('white')
    answer3input.draw(win)
    win.getMouse()
    answer3input.undraw()
    answer3 = answer3input.getText().lower()
    finalanswer3 = Text(Point(6.5, 2), answer3)
    finalanswer3.setFace('courier')
    finalanswer3.draw(win)

    finish_puzzle = prompt('Click "Submit" to finish. >')

    win.getMouse()

    puzzlespace.undraw()
    latline1.undraw()
    latline2.undraw()
    latline3.undraw()
    latline4.undraw()
    longline1.undraw()
    longline2.undraw()
    longline3.undraw()
    longline4.undraw()
    leftlabel1.undraw()
    leftlabel2.undraw()
    leftlabel3.undraw()
    toplabel1.undraw()
    toplabel2.undraw()
    toplabel3.undraw()
    hints.undraw()
    name1.undraw()
    name2.undraw()
    name3.undraw()
    finalanswer1.undraw()
    finalanswer2.undraw()
    finalanswer3.undraw()
    finish_puzzle.undraw()

    answers_one = [answer1, answer2, answer3]

    return answers_one

def archivistslair():
    narration5 = 'You walk cautiously down the stairs,\n' \
                 'keeping your wits about you as the smell\n' \
                 'of dust and old paper grows stronger and\n' \
                 'stronger.'
    narration6 = 'The further down you descend, you see\n' \
                 'more and more archaic and mysterious\n' \
                 'items hanging on the walls.'
    narration7 = 'At last you reach a door, flaking black\n' \
                 'lettering proclaiming,\n\n' \
                 '“Archives: Beware all ye who enter here.”\n\n' \
                 'Taking a steadying breath, you reach\n' \
                 'for the door…'
    narration(narration5, 6.5)
    narration(narration6, 5.5)
    narration(narration7, 7.5)

    archivedoor = prompt('Open the door? >')
    opendoor = reply().getText().lower()
    archivedoor.undraw()
    if opendoor == 'yes':
        narration8 = 'You push open the door, stepping\n' \
                     'into what appears to be a cave filled\n' \
                     'with shelves all lined with rows and\n' \
                     'rows of uniform grey boxes.'
        narration9 = 'You’re sure there are tables and chairs\n' \
                     'somewhere, but they have been long\n' \
                     'buried under the mountains and drifts\n' \
                     'of paper and memorabilia.'
        narration10 = 'A sudden shuffling sound to your left\n' \
                     'makes you start in alarm.'
        narration(narration8, 6)
        narration(narration9, 6)
        narration(narration10, 3)

        archivist_pic.draw(win)
        knopedialog1 = '???:\n\n' \
                       'Ah... what do we have here? What\n' \
                       'unsuspecting victi- I mean, potential\n' \
                       'researcher has found their way into\n' \
                       'my humble archive?'
        narration11 = 'A tall, skeletal looking old man is\n' \
                     'grinning at you, eyes glittering behind\n' \
                     'his slightly off-kilter glasses. He’s\n' \
                     'impeccably dressed, but there’s dust on\n' \
                     'his knees, scrapes on his knuckles, and\n' \
                     'paper cuts on his hands.'
        narration12 = 'You’ve read about people like this\n' \
                     'man before… Archivists.'
        dialog(knopedialog1, 6.5)
        narration(narration11, 7.5)
        narration(narration12, 3.5)
        archivist_pic.undraw()

        playerdialog3 = str(player_name.upper() + ":\n\n"
                                              "I'm " + player_name + ", the new\n" + player_class + ".")
        dialog(playerdialog3, 3.5)

        archivist_pic.draw(win)
        knopedialog2 = "???:\n\n" \
                       "Oh! How exciting! It's been so long\n" \
                       "since we've welcomed a new member into\n" \
                       "out little family here at the Library."
        knopedialog3 = "???:\n\n" \
                       "And after what happened to your poor\n" \
                       "predecessor, well..."
        knopedialog4 = "???:\n\n" \
                       "But where are my manners?! I am\n" \
                       "B. B. N. Knope, the Archivist."
        knopedialog5 = "KNOPE:\n\n" \
                       "What brings you down here, " + player_name + "?\n" \
                                                                    "You wouldn't, perchance, have been sent\n" \
                                                                    "down to do a little bit of processing,\n" \
                                                                    "would you?"
        knopedialog6 = "KNOPE:\n\n" \
                       "You know, we're always buried under\n" \
                       "a backlog, with new materials coming\n" \
                       "in every day... It's a nightmare!"
        knopedialog7 = "KNOPE:\n\n" \
                       "So... do you have a minute?\n" \
                       "Hour? Day? Year or ten to spare?"
        dialog(knopedialog2, 5)
        dialog(knopedialog3, 4.5)
        dialog(knopedialog4, 4)
        dialog(knopedialog5, 5.5)
        dialog(knopedialog6, 5)
        dialog(knopedialog7, 4)
        archivist_pic.undraw()

        playerdialog4 = str(player_name.upper() + ":\n\n"
                                              "Um... no. Not really,\n"
                                              "but I'll keep it in mind.")
        dialog(playerdialog4, 3.5)

        archivist_pic.draw(win)
        knopedialog8 = "KNOPE:\n\n" \
                       "Pity. It was worth a try.\n" \
                       "So, what can I help you with?"
        dialog(knopedialog8, 3.5)
        archivist_pic.undraw()

        playerdialog5 = str(player_name.upper() + ":\n\n"
                                              "Well, I was sent to gather the\n"
                                                  "LIBRARY RELICS in order to destroy\n"
                                                  "the TOME OF LENDING. AGNES told me\n"
                                                  "I would find one of them here.")
        dialog(playerdialog5, 5)

        archivist_pic.draw(win)
        knopedialog9 = "KNOPE:\n\n" \
                       "Hmm... I might just have what you're\n" \
                       "looking for, but one can't simply go\n" \
                       "around handing out RELICS to every\n" \
                       "random " + player_class + " who comes\n" \
                                                  "by looking for it."
        knopedialog10 = "KNOPE\n\n" \
                        "Did you even submit a materials request\n" \
                        "before you came down here?"
        dialog(knopedialog9, 6.5)
        dialog(knopedialog10, 4.5)
        archivist_pic.undraw()

        playerdialog5 = str(player_name.upper() + ":\n\n"
                                              "Look, it's really important.")
        dialog(playerdialog5, 3)

        archivist_pic.draw(win)
        knopedialog11 = "KNOPE:\n\n" \
                        "I'm sure it is, but stil..."
        knopedialog12 = "KNOPE:\n\n" \
                        "Oh! I've got it!"
        knopedialog13 = "KNOPE:\n\n" \
                        "Help me solve a little... missing\n" \
                        "materials problem, and I'll give you\n" \
                        "the RELIC."
        knopedialog14 = "KNOPE:\n\n" \
                        "Buuuut... if you can't solve the puzzle,\n" \
                        "you'll have to stay here and process our\n" \
                        "backlog."
        knopedialog15 = "KNOPE:\n\n" \
                        "Have we got a deal?"
        dialog(knopedialog11, 3)
        dialog(knopedialog12, 3)
        dialog(knopedialog13, 4)
        dialog(knopedialog14, 4.5)
        dialog(knopedialog15, 3)
        archivist_pic.undraw()

        archivepuzzle = prompt('Play the puzzle? >')
        playpuzzle = reply().getText().lower()
        archivepuzzle.undraw()
        if playpuzzle == "yes":
            playerdialog6 = str(player_name.upper() + ":\n\n"
                                              "Okay, I'll do it.")
            dialog(playerdialog6, 3)

            archivist_pic.draw(win)
            knopedialog16 = "KNOPE:\n\n" \
                            "Excellent!"
            dialog(knopedialog16, 2.5)
            archivist_pic.undraw()
            textbox.undraw()
            answers_one = puzzleone()
            if answers_one == ['hollinger box', 'microspatula', 'cotton gloves']:
                archivist_pic.draw(win)
                textbox.draw(win)
                knopedialog17 = "KNOPE:\n\n" \
                                "Well, I must say, I wasn't sure you'd\n" \
                                "figure that one out. Well done."
                knopedialog18 = "KNOPE:\n\n" \
                                "I suppose a deal is a deal... Here you go."
                dialog(knopedialog17, 4)
                dialog(knopedialog18, 3)
                archivist_pic.undraw()

                cardigan_pic.draw(win)
                player_inventory.append(cardigan)
                narration13 = "The CARDIGAN OF INVISIBILITY is now\n" \
                              "in your inventory!"
                narration(narration13, 4)

                inventory_check = player_name.upper() + "'s Inventory\n\n" + player_inventory[0] + '\n' + player_inventory[1] + '\n' + player_inventory[2] + '\n' + player_inventory[3]
                narration(inventory_check, 6)

                cardigan_pic.undraw()

                archivist_pic.draw(win)
                knopedialog19 = "KNOPE:\n\n" \
                                "If you're sure you want to continue, I'd\n" \
                                "recommend looking for the next RELIC in the\n" \
                                "CATALOGER'S DUNGEON."
                dialog(knopedialog19, 5)
                archivist_pic.undraw()

                playerdialog7 = str(player_name.upper() + ":\n\n"
                                              "Um... that sounds...")
                dialog(playerdialog7, 2.5)

                archivist_pic.draw(win)
                knopedialog20 = "KNOPE:\n\n" \
                                "Oh, i'ts just as terrifying as it\n" \
                                "sounds. Don't worry."
                knopedialog21 = "KNOPE:\n\n" \
                                "But you'd best be running along now!\n" \
                                "I've got far to much processing to do\n" \
                                "to be babysitting a new " + player_class + "."
                knopedialog22 = "KNOPE:\n\n" \
                                "You'll find the stairs to the DUNGEON\n" \
                                "over on the far wall there, behind some\n" \
                                "stacks of film reels."
                knopedialog23 = "KNOPE:\n\n" \
                                "Good luck."
                dialog(knopedialog20, 4)
                dialog(knopedialog21, 5)
                dialog(knopedialog22, 5)
                dialog(knopedialog23, 2)
                archivist_pic.undraw()

                narration14 = "You watch as KNOPE seems to disappear\n" \
                              "into the chaos of the archive."
                narration15 = "Eager to move on, you head towards the\n" \
                              "door and find it slightly ajar. A chill\n" \
                              "seems to hover around it and you think\n" \
                              "you can hear... something."
                narration(narration14, 3.5)
                narration(narration15, 6)

                take_stairs = prompt("Descend the stairs? >")
                take_stairs_reply = reply().getText().lower()
                take_stairs.undraw()
                if take_stairs_reply == "yes":
                    dungeon_title = Image(Point(4, 2.5), 'dungeon.gif')
                    dungeon_title.draw(win)
                    time.sleep(4)
                    dungeon_title.undraw()
                else:
                    narration16 = "The floor opens up beneath you\n" \
                                  "and you are devoured by silverfish."
                    narration(narration16, 3)
                    mainmenu()
            else:
                narration17 = "You are magically bound to remain\n" \
                              "in the archive until you have finished\n" \
                              "processing the back log."
                narration(narration17, 5)
                mainmenu()
        else:
            narration18 = "In your attempt to flee, you trip\n" \
                          "over a pile of boxes/papers and are\n" \
                          "dragged by a horde of giggling archive\n" \
                          "gnomes into the darkness. You are\n" \
                          "never heard from again."
            narration(narration18, 7)
            mainmenu()
    else:
        narration19 = "You see something shiny on the\n" \
                      "ground and bend to take a look. It's\n" \
                      "a paper clip. There is another, not\n" \
                      "to far away. Soon you have followed\n" \
                      "the trail of paper clips into the gloom.\n" \
                      "You are trapped. There is no way out."
        narration(narration19, 8)
        mainmenu()

    return player_inventory


player_inventory = inventory(player_class)
textbox = textbox()
submit()
player_inventory = archivistslair()
win.close()
