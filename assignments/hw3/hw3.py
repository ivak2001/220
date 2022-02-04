"""
Name: Iva Karalic
hw3.py

Problem: Using loops and user input to calculate the answers.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    x = eval(input("How many grades will you enter? "))
    acc = 0
    for i in range(1, x + 1):
        grade = eval(input("Enter grade: "))
        acc = acc + grade
        final = acc / x
    print(final)


def tip_jar():
    acc = 0
    for i in range(5):
        amount = eval(input("How much would you like to donate? "))
        acc = acc + amount
    print(acc)


def newton():
    x = eval(input("What number do you want to square root? "))
    improve = eval(input("How many times should we improve the approximation? "))
    approx = x / 2
    for i in range(improve):
        approx = ((approx + (x / approx)) / 2)
    print("The square root is approximately ", approx)


def sequence():
    x = eval(input("How many terms would you like? "))
    for i in range(x + 1):
        print(1 + (i // 2 * 2), end=" ")


def pi():
    n = eval(input("How many terms in the series? "))
    acc = 1
    for x in range(n):
        numerator = 2 + ((x // 2) * 2)
        denominator = 1 + (((x + 1) // 2) * 2)
        f = numerator / denominator
        acc = acc * f
    print(acc * 2)


if __name__ == '__main__':
    pass
