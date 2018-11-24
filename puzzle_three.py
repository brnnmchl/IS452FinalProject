# puzzle_three.py

# code for the reference tavern puzzle

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

    answers_three = [answer1, answer2, answer3, answer4, answer5]

    return answers_three


submit()
answers_tow = puzzlethree()
time.sleep(10)
win.close()
