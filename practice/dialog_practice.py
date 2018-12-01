# dialog practice

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

def dialog():
    dialogbloc = Text(Point(4.875, 2.875), 'ANTELOPE:\n\n'
                                           'Is an antelope\n'
                                           'a document?\n'
                                           'We may never know,\n'
                                           'but it is\n'
                                           'to imagine.\n'
                                           'Now I am simply\n'
                                           'testing how many\n'
                                           'newlines will fit\n'
                                           'in this box.')
    dialogbloc.setFace('courier')
    dialogbloc.setSize(20)
    return dialogbloc

dialog().draw(win)

textbox = Rectangle(Point(2.25, 1.25), Point(7.5, 4.5))
textbox.setWidth(2)
textbox.draw(win)

Image(Point(1.25, 3.75), 'antelope.gif').draw(win)

submit_button = Text(Point(7.25, 0.625), "Submit")
submit_button.draw(win)
Rectangle(Point(7.0, 0.5), Point(7.5, 0.75)).draw(win)

exit_button = Text(Point(0.75, 0.625), "Exit")
exit_button.draw(win)
Rectangle(Point(0.5, 0.5), Point(1.0, 0.75)).draw(win)

prompt = Text(Point(2.5, 0.75), 'Is an antelope\n'
                                'a document? >')
prompt.setFace('courier')
prompt.setSize(20)
prompt.draw(win)

response = Entry(Point(5.375, 0.75), 20)
response.setText('')
response.setFill('white')
response.draw(win)

win.getMouse()


time.sleep(2)
win.close()
