# castle_of_stacks.py

# code for the castle of stacks level

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

def antelope():
    antelope_pic.draw(win)
    narrationA = "From within the stacks, a creature\n" \
                    "appears, its horns tall and twisted,\n" \
                    "its eyes bright read and terrifying."
    narrationB = "It utters one question..."
    antelopedialog1 = "ANTELOPE:\n\n" \
                         "Is an antelope a document?"
    narrationC = "You are frozen in terror, your\n" \
                          "mind slowly dissolving as you\n" \
                          "try to come up with an answer."
    narrationD = "The last thing you hear is the\n" \
                          "horrible laughter of the ANTELOPE\n" \
                          "as it claims another victim."
    narration(narrationA, 8)
    narration(narrationB, 4)
    dialog(antelopedialog1, 4)
    narration(narrationC, 8)
    narration(narrationD, 8)
    antelope_pic.undraw()

def castlestacks():
    narration59 = "You cautiously make your way up\n" \
                  "the stairs, the soothing sounds of\n" \
                  "the tavern falling away behind you."
    narration60 = "At the top, you see a door decorated\n" \
                  "with intricate ironwork depicting\n" \
                  "some sort of stylized horned creature."
    narration(narration59, 7)
    narration(narration60, 7)

    open_door = prompt("Open the door? >")
    open_door_reply = reply().getText().lower()
    open_door.undraw()
    if open_door_reply == "yes":
        narration62 = "You push the door open cautiously\n" \
                      "and immediately feel your breath\n" \
                      "catch."
        narration63 = "Beyond is a vast labyrinth of\n" \
                      "bookstacks, twisting and twining\n" \
                      "for as far as the eye can see."
        narration64 = "You are standing on a platform and\n" \
                      "a staircase to your left leads down\n" \
                      "several stories."
        narration65 = "Taking a steadying breath, you descend\n" \
                      "the stairs, passing floor and floor\n" \
                      "of dark, ominous bookshelves."
        narration66 = "Once you reach the bottom floor, you\n" \
                      "are faced with three options."
        narration(narration62, 7)
        narration(narration63, 7)
        narration(narration64, 7)
        narration(narration65, 7)
        narration(narration66, 6)

        direction1 = prompt("Left, Right, Forward? >")
        direction1_reply = reply().getText().lower()
        direction1.undraw()
        if direction1_reply == "left":
            narration67 = "You get the distinct feeling\n" \
                          "you're being watched. You come\n" \
                          "to another intersection..."
            narration(narration67, 7)

            direction2 = prompt("Left, Right, Forward? >")
            direction2_reply = reply().getText().lower()
            direction2.undraw()
            if direction2_reply == "right":
                narration68 = "You think you hear something\n" \
                              "moving in the shadows, but you\n" \
                              "press on..."
                narration(narration68, 7)

                direction3 = prompt("Left, Right, Forward? >")
                direction3_reply = reply().getText().lower()
                direction3.undraw()
                if direction3_reply == "right":
                    narration69 = "You're almost halfway there,\n" \
                                  "so far so good. Right?"
                    narration(narration69, 6)

                    direction4 = prompt("Left, Right, Forward? >")
                    direction4_reply = reply().getText().lower()
                    direction4.undraw()
                    if direction4_reply == "forward":
                        narration70 = "From the corner of your eye, you\n" \
                                      "think you see a flash of red."
                        narration(narration70, 6)

                        direction5 = prompt("Left, Right, Forward? >")
                        direction5_reply = reply().getText().lower()
                        direction5.undraw()
                        if direction5_reply == "left":
                            narration71 = "The stacks feel close, you feel\n" \
                                          "your heartbeat speed up."
                            narration(narration71, 6)

                            direction6 = prompt("Left, Right, Forward? >")
                            direction6_reply = reply().getText().lower()
                            direction6.undraw()
                            if direction6_reply == "forward":
                                narration72 = "You are so close now... but what\n" \
                                              "was that? Is it getting closer?"
                                narration(narration72, 6)

                                direction7 = prompt("Left, Right, Forward? >")
                                direction7_reply = reply().getText().lower()
                                direction7.undraw()
                                if direction7_reply == "right":
                                    narration73 = "You turn the final corner and almost\n" \
                                                  "run straight into a young woman\n" \
                                                  "balanced precariously on a  stool, a\n" \
                                                  "stack of books in her arms."
                                    narration74 = "Luckily, you took Self-Defense for the\n" \
                                                  "Subject Librarian last semester, so\n" \
                                                  "you're quick on your feet."
                                    narration(narration73, 9)
                                    narration(narration74, 8)

                                    playerdialog23 = str(player_name.upper() + ":\n\n"
                                                        "Oh! Uh, h-hi?")
                                    dialog(playerdialog23, 3)

                                    narration75 = "With lightning quick movements, the\n" \
                                                  "young woman shelves the books, her\n" \
                                                  "hands moving almost too fast for you\n" \
                                                  "to see."
                                    narration76 = "When she's done, she turns and peers\n" \
                                                  "down at you curiously."
                                    narration(narration75, 8)
                                    narration(narration76, 6)

                                    shelver_pic.draw(win)
                                    deweydialog1 = "???:\n\n" \
                                                   "Ah, hello there. Are you lost?\n" \
                                                   "Can I help you?"
                                    dialog(deweydialog1, 5)
                                    shelver_pic.undraw()

                                    playerdialog24 = str(player_name.upper() + ":\n\n"
                                                         "I was, uh, looking for an item.\n"
                                                                               "It should be here.")
                                    dialog(playerdialog24, 5)

                                    narration77 = "You gesture vaguely."
                                    narration(narration77, 4)

                                    shelver_pic.draw(win)
                                    deweydialog2 = "???:\n\n" \
                                                   "Ah, did the Reference Librarians send\n" \
                                                   "you? That was kinda harsh."
                                    deweydialog3 = "DEWEY:\n\n" \
                                                   "I'm Librarian Commander Dewey of the\n" \
                                                   "Stacks Brigade, but you can just call\n" \
                                                   "me Dewey."
                                    deweydialog4 = "DEWEY:\n\n" \
                                                   "What item were you looking for?"
                                    dialog(deweydialog2, 6)
                                    dialog(deweydialog3, 7)
                                    dialog(deweydialog4, 4)
                                    shelver_pic.undraw()

                                    playerdialog25 = str(player_name.upper() + ":\n\n"
                                                            "The, uh, THOUSAND SHELF BOOKCART?")
                                    dialog(playerdialog25, 4)

                                    shelver_pic.draw(win)
                                    deweydialog5 = "DEWEY:\n\n" \
                                                   "Ooooooohhhhhhh... Wow. I never thought\n" \
                                                   "this day would come..."
                                    deweydialog6 = "DEWEY:\n\n" \
                                                   "There's an old story amongst the Brigade\n" \
                                                   "that one day the Once and Future Librarian\n" \
                                                   "would return to reclaim the BOOKCART."
                                    deweydialog7 = "DEWEY:\n\n" \
                                                   "*whispering*\n\n" \
                                                   "The boys are never gonna believe this..."
                                    dialog(deweydialog5, 7)
                                    dialog(deweydialog6, 8)
                                    dialog(deweydialog7, 6)
                                    shelver_pic.undraw()

                                    playerdialog26 = str(player_name.upper() + ":\n\n"
                                                        "That's... nice, but I, uh, really\n"
                                                                               "need the BOOKCART. Admin is getting\n"
                                                                               "up to some trouble and I'm supposed\n"
                                                                               "to stop them.")
                                    dialog(playerdialog26, 8)

                                    shelver_pic.draw(win)
                                    narration78 = "DEWEY climbs down from her stool\n" \
                                                  "and practically bounces over to\n" \
                                                  "you, her excitement palpable."
                                    narration(narration78, 7)

                                    deweydialog8 = "DEWEY:\n\n" \
                                                   "If you managed to make it through the\n" \
                                                   "Stacks on your own, it's got to be a\n" \
                                                   "sign!"
                                    deweydialog9 = "DEWEY:\n\n" \
                                                   "Even trained members of the Stacks\n" \
                                                   "Brigade usually get turned around for\n" \
                                                   "a day or two before they make it to\n" \
                                                   "their destination!"
                                    dialog(deweydialog8, 8)
                                    dialog(deweydialog9, 9)

                                    narration79 = "DEWEY turns and starts scanning the\n" \
                                                  "shelves around you both. After a moment,\n" \
                                                  "she grins and reaches for a thick,\n" \
                                                  "leather-bound volume."
                                    narration(narration79, 9)

                                    deweydialog10 = "DEWEY:\n\n" \
                                                    "Here we are!"
                                    dialog(deweydialog10, 3)
                                    shelver_pic.undraw()

                                    playerdialog27 = str(player_name.upper() + ":\n\n"
                                                        "...That's the BOOKCART?")
                                    dialog(playerdialog27, 4)

                                    shelver_pic.draw(win)
                                    deweydialog11 = "DEWEY:\n\n" \
                                                    "No, silly. The BOOKCART's inside the\n" \
                                                    "book. Go on! Open it!"
                                    dialog(deweydialog11, 6)
                                    shelver_pic.undraw()

                                    open_book = prompt("Open the book? >")
                                    open_book_reply = reply().getText().lower()
                                    open_book.undraw()
                                    if open_book_reply == 'yes':
                                        narration82 = "You flip the cover back and a burst\n" \
                                                      "of color and sound issues from the\n" \
                                                      "pages."
                                        narration83 = "You are blinded by the brilliance for\n" \
                                                      "a moment, and when you can see again,\n" \
                                                      "the BOOKCART is sitting before you."
                                        narration(narration82, 7)
                                        narration(narration83, 8)

                                        cart_pic.draw(win)
                                        player_inventory.append(bookcart)
                                        narration84 = "The THOUSAND SHELF BOOKCART\n" \
                                                      "is now in your inventory!"
                                        narration(narration84, 5)

                                        inventory_check = player_name.upper() + "'s Inventory\n\n" + player_inventory[0] + '\n' + player_inventory[1] + '\n' + player_inventory[2] + '\n' + player_inventory[3] + '\n' + player_inventory[4] + '\n' + player_inventory[5] + '\n' + player_inventory[6]
                                        narration(inventory_check, 10)
                                        cart_pic.undraw()

                                        shelver_pic.draw(win)
                                        deweydialog12 = "DEWEY:\n\n" \
                                                        "Oh... my... I-I can't BELIEVE THIS\n" \
                                                        "IS ACTUALLY HAPPENING!!"
                                        dialog(deweydialog12, 6)

                                        narration85 = "DEWEY dances around the BOOKCART,\n" \
                                                      "eyes wide in wonder. After fawning\n" \
                                                      "over it for a few moments, DEWEY\n" \
                                                      "turns back to you."
                                        narration(narration85, 8)

                                        deweydialog13 = "DEWEY:\n\n" \
                                                        "Can I... Can I get your autograph?"
                                        dialog(deweydialog13, 4)
                                        shelver_pic.undraw()

                                        autograph = prompt("Give your autograph? >")
                                        autograph_reply = reply().getText().lower()
                                        autograph.undraw()
                                        if autograph_reply == "yes":
                                            shelver_pic.draw(win)
                                            deweydialog14 = "DEWEY:\n\n" \
                                                            "Wow..."
                                            deweydialog15 = "DEWEY:\n\n" \
                                                            "I, um, I guess you've got to be\n" \
                                                            "off then."
                                            dialog(deweydialog14, 3)
                                            dialog(deweydialog15, 5)
                                            shelver_pic.undraw()

                                            playerdialog28 = str(player_name.upper() + ":\n\n"
                                                                "Wait... you're not going to, like,\n"
                                                                                       "challenge me to complete a puzzle\n"
                                                                                       "or something?")
                                            playerdialog29 = str(player_name.upper() + ":\n\n"
                                                                    "I can just... take it?")
                                            dialog(playerdialog28, 6)
                                            dialog(playerdialog29, 4)

                                            shelver_pic.draw(win)
                                            deweydialog16 = "DEWEY:\n\n" \
                                                            "Sure. The Stacks are a puzzle in and of\n" \
                                                            "themselves, so you pretty much already\n" \
                                                            "proved yourself as far as I'm concerned."
                                            dialog(deweydialog16, 8)
                                            shelver_pic.undraw()

                                            narration88 = "You nod and then turn to\n" \
                                                          "the BOOKCART."
                                            narration89 = "You realize you have no idea how\n" \
                                                          "you're going to carry a BOOKCART\n" \
                                                          "or where you're supposed to go next."
                                            narration(narration88, 5)
                                            narration(narration89, 8)

                                            playerdialog30 = str(player_name.upper() + ":\n\n"
                                                                "Hey, uh, DEWEY?")
                                            playerdialog31 = str(player_name.upper() + ":\n\n"
                                                                "You don't happen to know how to\n"
                                                                                       "use this thing, do you?")
                                            dialog(playerdialog30, 4)
                                            dialog(playerdialog31, 5)

                                            shelver_pic.draw(win)
                                            deweydialog17 = "DEWEY:\n\n" \
                                                            "Sure thing! Just, climb on and\n" \
                                                            "tell it where to go!"
                                            dialog(deweydialog17, 6)
                                            shelver_pic.undraw()

                                            playerdialog32 = str(player_name.upper() + ":\n\n"
                                                                "Climb... climb on?")
                                            dialog(playerdialog32, 4)

                                            narration90 = "DEWEY nods and pats the top\n" \
                                                          "of the BOOKCART."
                                            narration91 = "You stare at it for a moment before\n" \
                                                          "deciding you've definitely done\n" \
                                                          "weirder things before."
                                            narration92 = "While DEWEY steadies the cart,\n" \
                                                          "you climb aboard."
                                            narration(narration90, 5)
                                            narration(narration91, 7)
                                            narration(narration92, 6)

                                            shelver_pic.draw(win)
                                            deweydialog18 = "DEWEY:\n\n" \
                                                            "Good luck on your quest!"
                                            deweydialog19 = "DEWEY:\n\n" \
                                                            "DEAN PATRICK ARCHY is no pushover,\n" \
                                                            "but I believe you can beat him!"
                                            dialog(deweydialog18, 4)
                                            dialog(deweydialog19, 6)
                                            shelver_pic.undraw()

                                            playerdialog33 = str(player_name.upper() + ":\n\n"
                                                                "Thanks, DEWEY.")
                                            playerdialog34 = str(player_name.upper() + ":\n\n"
                                                                "But, ah... do you, do you know where\n"
                                                                                       "I can find him?")
                                            dialog(playerdialog33, 4)
                                            dialog(playerdialog34, 5)

                                            shelver_pic.draw(win)
                                            deweydialog20 = "DEWEY:\n\n" \
                                                            "He'll be up in the ADMIN'S TOWER."
                                            dialog(deweydialog20, 5)
                                            shelver_pic.undraw()

                                            where_to = prompt("Tell the BOOKCART\nwhere to go? >")
                                            where_to_reply = reply().getText().lower()
                                            where_to.undraw()
                                            if where_to_reply == "yes":
                                                playerdialog35 = str(player_name.upper() + ":\n\n"
                                                                    "To the ADMIN'S TOWER!")
                                                dialog(playerdialog35, 4)
                                                tower_title = Image(Point(4, 2.5), 'tower.gif')
                                                tower_title.draw(win)
                                                time.sleep(5)
                                                tower_title.undraw()
                                            else:
                                                narration93 = "You tell the BOOKCART to take\n" \
                                                              "you home and live the rest of\n" \
                                                              "your days regretting letting\n" \
                                                              "down the good people of the\n" \
                                                              "Library."
                                                narration(narration93, 9)
                                                mainmenu()
                                        else:
                                            narration86 = "You, rather cruelly, stomp all\n" \
                                                          "over DEWEY's dreams and crush her\n" \
                                                          "belief in humanity."
                                            narration87 = "Nice going," + player_name.upper() + "."
                                            narration(narration86, 8)
                                            narration(narration87, 4)
                                            mainmenu()
                                    else:
                                        narration80 = "You stare at the book and feel a\n" \
                                                      "wave of anxiety crash over you."
                                        narration81 = "You're not sure you're ready to be\n" \
                                                      "the Once and Future Librarian, and\n" \
                                                      "you sadly hand the book back to DEWEY."
                                        narration(narration80, 6)
                                        narration(narration81, 8)
                                        mainmenu()
                                else:
                                    antelope()
                                    mainmenu()
                            else:
                                antelope()
                                mainmenu()
                        else:
                            antelope()
                            mainmenu()
                    else:
                        antelope()
                        mainmenu()
                else:
                    antelope()
                    mainmenu()
            else:
                antelope()
                mainmenu()
        else:
            antelope()
            mainmenu()
    else:
        narration61 = "The floor opens up beneath you\n" \
                      "and you are devoured by silverfish."
        narration(narration61, 5)
        mainmenu()

    return player_inventory

player_inventory = inventory(player_class)
player_inventory.append(cardigan)
player_inventory.append(spectacles)
player_inventory.append(mug)
textbox = textbox()
submit()
player_inventory = castlestacks()
win.close()
