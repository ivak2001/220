"""
Name: Iva Karalic
hw2.py

Problem: Using import math to solve problems

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound? "))
    acc = 0
    for x in range(0, upper_bound + 1, 3):
        acc = acc + x
    print(acc)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print()


def triangle_area():
    a = eval(input("Enter side a length: "))
    b = eval(input("Enter side b length: "))
    c = eval(input("Enter side c length: "))
    s = (a + b + c) / 2
    x = s * (s - a)(s - b)(s - c)
    result = math.sqrt(x)
    print("area is", result)


def sum_squares():
    lower = eval(input("Enter lower range: "))
    upper = eval(input("Enter upper range: "))
    acc = 0
    for i in range(lower, upper + 1):
        acc = acc + i * i
    print(acc)


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    acc = 1
    for i in range(exponent):
        acc = acc * base
    print(acc)


if __name__ == '__main__':
    pass
