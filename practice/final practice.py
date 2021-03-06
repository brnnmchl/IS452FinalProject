# final practice.py

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

def intro():
    start_screen = Text(Point(4.0, 3.5), "LIBRARY QUEST\n\n"
                                         "(c)2018 Brinna Michael")
    start_screen.setFace("courier")
    start_screen.setSize(20)
    start_screen.draw(win)

    play_button = Text(Point(4.0, 1.5), "Play?")
    play_button.setFace("courier")
    play_button.setSize(20)
    play_button.draw(win)
    play_button_border = Rectangle(Point(3.5, 1.25), Point(4.5, 1.75)).draw(win)

    win.getMouse()

    start_screen.undraw()
    play_button.undraw()
    play_button_border.undraw()

    intro = Text(Point(4.0, 2.5), 'Years of study, thousands of bowls of ramen, and the\n'
                                  'sweet embrace of caffeine have led you to this moment.\n'
                                  'All of your hard work has finally paid off and you feel\n'
                                  'a thrill of excitement as you approach the intimidating\n'
                                  'oak door. You’re finally here…')
    intro.setFace("courier")
    intro.setStyle('italic')
    intro.setSize(20)
    intro.draw(win)
    time.sleep(5)

    intro.undraw()
    enter_lib = Text(Point(3.0, 2.5), "Open the door? >")
    enter_lib.setFace("courier")
    enter_lib.setSize(20)
    inputText = Entry(Point(4.5, 2.5), 5)
    inputText.setText('')
    inputText.setFill('white')
    inputText.draw(win)
    enter_lib.draw(win)

    submit_button = Text(Point(7.25, 0.625), "Submit")
    submit_button.setFace('courier')
    submit_button.draw(win)
    Rectangle(Point(7.0, 0.5), Point(7.5, 0.75)).draw(win)

    exit_button = Text(Point(0.75, 0.625), "Exit")
    exit_button.setFace('courier')
    exit_button.draw(win)
    Rectangle(Point(0.5, 0.5), Point(1.0, 0.75)).draw(win)

    win.getMouse()
    # ll = Point(0.5, 0.5)
    # ur = Point(1.0, 0.75)
    #
    # clickPoint = win.getMouse()
    # if clickPoint in ll.getX() < clickPoint.getX() < ur.getX() and ll.getY() < clickPoint.getY() < ur.getY():
    #     start_screen.draw(win)
    #     play_button.draw(win)
    # else:
    #     enter_lib.undraw()
    #     inputText.undraw()

    open_door = inputText.getText()
    if open_door == 'yes':
        inputText.undraw()
        enter_lib.undraw()
        title_scene = Text(Point(4.0, 2.5), 'Welcome to…')
        title_scene.setFace("courier")
        title_scene.setSize(20)
        title_scene.draw(win)
        time.sleep(2)

        title_scene.undraw()
        Image(Point(4.0, 2.5), 'logo.gif').draw(win)
        time.sleep(5)
    else:
        premature_rage_quit = Text(Point(4.0, 2.5), "Really?\n"
                                                    "You're really not curious?")
        premature_rage_quit.setFace("courier")
        premature_rage_quit.setSize(20)
        premature_rage_quit.draw(win)
        time.sleep(10)


intro()
# quest()
# lair()
# dungeon()
# tavern()
# stacks()
# tower()
win.close()


# print('For years, you have studied and trained and now\n'
#       'the time has arrived at last. You approach the\n'
#       'intimidating oak doors and push them open...\n\n')
# time.sleep(5)
# print('Welcome, to LIBRARY QUEST!\n'
#       '\u2669 \u266B \u2669 \u266B \u2669 \u266B \u2669 \u266B \u2669 \u266B \u2669 \u266B \u2669 \u266B\n\n')
# time.sleep(2)
# print('You are greeted inside the doors by an elderly woman.\n\n')
# time.sleep(3)
# player_name = input('AGNES: Welcome to the Library. I am Agnes.\n'
#                     'What can I call you? >').title()
# time.sleep(1)
# print("\n\nAGNES: It's a pleasure to meet you", player_name, ".\n\n")
# time.sleep(1)
# print("AGNES: This must be your first day. Well, don't\n"
#             "worry, we here at the Library are all quite\n"
#             "friendly. I'm sure you'll enjoy working here.\n\n")



