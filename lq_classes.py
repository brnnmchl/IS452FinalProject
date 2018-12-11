# lq_classes.py

# library of level classes

import time
from graphics import *


class Button:
    """base class for buttons"""

    def __init__(self, name):
        self.name = name

    def outline(self, x1, y1, x2, y2, win):
        self.outline = Rectangle(Point(x1, y1), Point(x2, y2)).draw(win)
        return self.outline

    def label(self, name, x1, y1, win):
        self.label = Text(Point(x1, y1), name)
        self.label.setFace('courier')
        self.label.draw(win)
        return self.label

    def clickButton(self, point, rectangle):
        ll = rectangle.getP1()
        ur = rectangle.getP2()
        return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

class Level:
    """base class for all levels"""

    def __init__(self, name):
        self.name = name

    def dialog(self, dialog, sleeptime, win):
        self.dialogbloc = Text(Point(4.875, 2.875), dialog)
        self.dialogbloc.setFace('courier')
        self.dialogbloc.setSize(20)
        self.dialogbloc.draw(win)
        time.sleep(sleeptime)
        self.dialogbloc.undraw()
        return self.dialogbloc

    def narration(self, narration, sleeptime, win):
        self.narrationbloc = Text(Point(4.875, 2.875), narration)
        self.narrationbloc.setFace('courier')
        self.narrationbloc.setSize(20)
        self.narrationbloc.setStyle('italic')
        self.narrationbloc.draw(win)
        time.sleep(sleeptime)
        self.narrationbloc.undraw()
        return self.narrationbloc

    def prompt(self, prompt, win):
        self.promptbloc = Text(Point(2.5, 0.75), prompt)
        self.promptbloc.setFace('courier')
        self.promptbloc.setSize(20)
        self.promptbloc.draw(win)
        return self.promptbloc

    def reply(self, win):
        self.responsebloc = Entry(Point(5.375, 0.75), 30)
        self.responsebloc.setText('')
        self.responsebloc.setFill('white')
        self.responsebloc.draw(win)
        win.getMouse()
        self.responsebloc.undraw()
        return self.responsebloc

    def setInventory(self, player_inventory, relic):
        self.inventory = player_inventory
        self.inventory.append(relic)
        return self.inventory

    def titlecard(self, titlecard_file, win):
        self.titlecard = Image(Point(4, 2.5), titlecard_file)
        self.titlecard.draw(win)
        time.sleep(8)
        self.titlecard.undraw()


class Menu:
    """Main Menu"""

    def __init__(self):
        self.name = "Library Quest"

    def playLevel(self, button):
        self.play_button_outline = button.outline()
        self.play_button_label = button.label()
        self.play_button

    # def seeCredits(self, button):



class Intro(Level):
    """Introduction class"""

    def __init__(self):
        super().__init__("Introduction")

    def playerName(self, prompt, win):
        self.promptbloc = Text(Point(2.5, 0.75), prompt)
        self.promptbloc.setFace('courier')
        self.promptbloc.setSize(20)
        self.promptbloc.draw(win)
        self.player_name = Entry(Point(5.375, 0.75), 30)
        self.player_name.setText('')
        self.player_name.setFill('white')
        self.player_name.draw(win)
        win.getMouse()
        self.player_name.undraw()
        self.promptbloc.undraw()
        return self.player_name

    def playerClass(self, prompt, win):
        self.promptbloc = Text(Point(2.5, 0.75), prompt)
        self.promptbloc.setFace('courier')
        self.promptbloc.setSize(20)
        self.promptbloc.draw(win)
        self.player_class = Entry(Point(5.375, 0.75), 30)
        self.player_class.setText('')
        self.player_class.setFill('white')
        self.player_class.draw(win)
        win.getMouse()
        self.player_class.undraw()
        self.promptbloc.undraw()
        return self.player_class


class Lair(Level):
    """Archivist's Lair class"""

    def __init__(self):
        super().__init__("Archvist's Lair")

    def puzzle(self, win):
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


class Dungeon(Level):
    """Cataloger's Dungeon class"""

    def __init__(self):
        super().__init__("Cataloger's Dungeon")

    def puzzle(self, win):
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

        answers_two = [answer1, answer2, answer3, answer4]

        return answers_two


class Tavern(Level):
    """Reference Tavern class"""

    def __init__(self):
        super().__init__("Reference Tavern")

    def puzzle(self, win):
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


class Stacks(Level):
    """Castle of Stacks class"""

    def __init__(self):
        super().__init__("Castle of Stacks")


class Tower(Level):
    """Admin's Tower Class"""

    def __init__(self):
        super().__init__("Admin's Tower")
