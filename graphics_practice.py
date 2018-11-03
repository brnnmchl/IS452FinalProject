from graphics import *
import time

# win = GraphWin('Shapes', 320, 240) # the second two parameters change the size of the window (w x h)
#
# center = Point(100, 100)
# circ = Circle(center, 30)
# circ.setFill('red')
# circ.draw(win)
#
# label = Text(center, "Red Circle")
# label.draw(win)
#
# rect = Rectangle(Point(30, 30), Point(70, 70))
# rect.draw(win)
#
# line = Line(Point(20, 30), Point(180, 199))
# line.draw(win)
#
# oval = Oval(Point(20, 150), Point(180, 199))
# oval.draw(win)

# map = GraphWin('Map of The Library', 450, 400)
# rect = Rectangle(Point(30, 30), Point(35, 35))
# rect.setFill('red')
# rect.draw(map)
#
# label = Text(Point(27, 25), "Front Door")
# label.draw(map)


# def main():
#     win = GraphWin("Draw a Triangle")
#     win.setCoords(0.0, 0.0, 10.0, 10.0)
#     message = Text(Point(5, 0.5), "Click on three points")
#     message.draw(win)
#
#     p1 = win.getMouse()
#     p1.draw(win)
#     p2 = win.getMouse()
#     p2.draw(win)
#     p3 = win.getMouse()
#     p3.draw(win)
#
#     triangle = Polygon(p1, p2, p3)
#     triangle.setFill('peachpuff')
#     triangle.setOutline('cyan')
#     triangle.draw(win)
#
#     message.setText("Click anywhere to quit.")
#     win.getMouse()
# main()
#
# def main():
#     win = GraphWin("Celsius Converter", 400, 300)
#     win.setCoords(0.0, 0.0, 3.0, 4.0)
#
#     Text(Point(1,3), ' Celsius Temperature:').draw(win)
#     Text(Point(1,1), "Fahrenheit Temperature:").draw(win)
#     inputText = Entry(Point(2.25, 3), 5)
#     inputText.setText('0.0')
#     inputText.draw(win)
#     outputText = Text(Point(2.25, 1), '')
#     outputText.draw(win)
#     button = Text(Point(1.5,2.0), "Convert It")
#     button.draw(win)
#     Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)
#
#     win.getMouse()
#
#     celsius = float(inputText.getText())
#     fahrenheit = 9.0/5.0 * celsius + 32
#
#     outputText.setText(round(fahrenheit, 2))
#     button.setText('Quit')
#
#     win.getMouse()
#     win.close()
# main()

def main():
    win = GraphWin("Antelope")
    win.setCoords(0.0, 0.0, 3.0, 3.0)
    antelope = 'antelope'
    dialog = str("Is an " + antelope + " a document?")
    Text(Point(1.5,0.5), dialog).draw(win)
    Image(Point(1.5,1.75), 'antelope.gif').draw(win)
    time.sleep(30)
    win.close()

main()
