from face import Face
from graphics import *

def fibonacci(num_seq):
    fib_list = [0, 1]
    acc = 0
    while not acc == num_seq:
        fib_list.append(fib_list[acc] + fib_list[acc + 1])
        acc = acc + 1
    return fib_list[num_seq]


def annual_rate(principal, rate):
    annually_rate = principal * (1 + rate)
    return annually_rate


def double_investment(principal, rate):
    annually_rate = 0
    number_years = 0
    double_principal = principal * 2
    while not double_principal <= annually_rate:
        number_years = number_years + 1
        annually_rate += annual_rate(principal, rate)
        print(double_principal)
        print(annually_rate)
    return number_years


def syracuse(starting_value):
    num_list = [starting_value]
    acc = 0
    while num_list[acc] != 1:
        if num_list[acc] % 2 == 0:
            syr_even = num_list[acc] / 2

            num_list.append(syr_even)
        else:
            syr_odd = (3 * num_list[acc]) + 1

            num_list.append(syr_odd)
        acc = acc + 1

    return num_list


def is_prime(num):
    if num % 1 == 0 and num % num == 0:
        return True
    return False

def goldbach(num):
    if num % 2 == 0:
        return None
    else:
        pass


def face_smile():
    win = GraphWin('face', 400, 400)
    face_1 = Face(win, Point(200, 200), 100)
    face_1.wink(win)
    win.getMouse()
    win.close()
