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

player_name = "testname"
player_class = 'testclass'

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






inventory = inventory(player_class)
textbox()
submit()
archivistslair()
win.close()
