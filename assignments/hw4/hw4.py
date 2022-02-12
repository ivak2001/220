"""
Name: Iva Karalic
hw4.py

Problem: Using graphics to make shapes.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Point, Text, Rectangle, Circle

import math


def squares():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to duplicate square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(200, 200), Point(180, 180))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        double = shape.clone()
        double.move(change_x, change_y)
        double.draw(win)

    close_pt = Point(200, 50)
    close = Text(close_pt, "Click again to quit")
    close.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    window = GraphWin("Rectangle", 400, 400)
    message = Text(Point(200, 50), "Click on two points")
    message.draw(window)

    p1 = window.getMouse()
    p1.draw(window)
    p2 = window.getMouse()
    p2.draw(window)

    rec = Rectangle(p1, p2)
    rec.setFill("blue")
    rec.draw(window)

    ln = abs(p2.getY() - p1.getY())
    w = abs(p2.getX() - p1.getX())
    perimeter = 2 * (ln + w)
    area = ln * w
    per = Text(Point(100, 350), "Perimeter: " + str(perimeter))
    ar = Text(Point(300, 350), "Area: " + str(area))
    per.draw(window)
    ar.draw(window)

    message.setText("Click again to quit")
    window.getMouse()
    window.close()


def circle():
    win = GraphWin("Circle", 400, 400)
    message = Text(Point(200, 50), "Click on a point to set the center")
    message.draw(win)

    center_pt = win.getMouse()
    center_pt.draw(win)

    message.setText("Click on another point to draw the circle")

    circumference = win.getMouse()
    circumference.draw(win)

    x = center_pt.getX() - circumference.getX()
    y = center_pt.getY() - circumference.getY()
    radius = math.sqrt((x**2) + (y**2))

    cir = Circle(center_pt, radius)
    cir.setFill("green")
    cir.draw(win)
    rad = Text(Point(200, 350), "radius: " + str(radius))
    rad.draw(win)

    message.setText("Click again to close")
    win.getMouse()
    win.close()



def pi2():
    sum = eval(input("Enter in number of terms to sum: "))
    acc = 0
    for i in range(sum):
        num = 4
        denom = 1 + (2 * i)
        formula = (num/denom) * ((-1)**i)
        acc = acc + formula
    print("Sum =", acc)
    print("Accuracy from pi: ", math.pi - acc)

def main():
    squares()
    rectangle()
    circle()
    pi2()

main()


if __name__ == '__main__':
    pass
