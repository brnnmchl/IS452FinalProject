# puzzle_one.py

# code for the Archivist's Lair puzzle

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

def submit():
    submit_button = Text(Point(7.25, 0.625), "Submit")
    submit_button.setFace('courier')
    submit_button.draw(win)
    Rectangle(Point(7.0, 0.5), Point(7.5, 0.75)).draw(win)

    return submit_button

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

    answers_one = [answer1, answer2, answer3]

    return answers_one


submit()
puzzleone()
time.sleep(10)
win.close()
