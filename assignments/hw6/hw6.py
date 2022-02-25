"""
Name: Iva Karalic
hw6.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def cash_converter():
    cash = eval(input("Enter an integer: "))
    print('That is $' + '{:.2f}'.format(cash))


def encode():
    message = input("Enter a message: ")
    key = eval(input("Enter a key: "))
    acc = ""
    for i in message:
        answer = ord(i)
        char = answer + key
        new_char = chr(char)
        acc = acc + new_char
    print(acc)


def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area


def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume


def sum_n(number):
    acc = 0
    for i in range(number + 1):
        acc = acc + i
    return acc


def sum_n_cubes(number):
    acc = 0
    for i in range(number + 1):
        acc = acc + (i ** 3)
    return acc


def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")
    acc = ""
    for i in range(len(message)):
        c = message[i]
        k = key[i % len(key)]
        ch = ord(c) + ord(k) - 97
        new_ch = chr(ch)
        acc = acc + new_ch
    print(acc)


if __name__ == '__main__':

    cash_converter()
    encode()
    res = sphere_area(13)
    print(res)
    res = sphere_volume(13)
    print(res)
    res = sum_n(100)
    print(res)
    res = sum_n_cubes(13)
    print(res)
    encode_better()
