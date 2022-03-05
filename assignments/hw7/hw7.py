"""
Name: Iva Karalic
hw.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    read_file = open(in_file_name, "r")
    write_file = open(out_file_name, "w")
    lines = read_file.readlines()
    total = 0
    for each_line in lines:
        split_space = each_line.split()
        for i in range(len(split_space)):
            total = total + 1
            print(total, split_space[i], end="\n", file=write_file)
    read_file.close()
    write_file.close()


def hourly_wages(in_file_name, out_file_name):
    input_file = open(in_file_name, 'r')
    output_file = open(out_file_name, 'w')
    for raise_wage in input_file:
        pay_list = raise_wage.split(" ")
        pay_rate = (pay_list[2])
        pay_rate = float(pay_rate)
        hour_work = (pay_list[3])
        hour_work = float(hour_work)
        new_rate = pay_rate + 1.65
        bonus_pay = new_rate * hour_work
        new_pay = "{} {} {:.2f}".format(pay_list[0], pay_list[1], bonus_pay)
        print(new_pay, file=output_file)

def calc_check_sum(isbn):
    check_sum = isbn
    check_val = check_sum.replace("-", "")
    check_index = 10
    check_total = 0
    for check in check_val:
        check = int(check)
        check_prt = check * check_index
        check_total = check_total + check_prt
        check_index = check_index - 1
    return check_total


def send_message(file_name, friend_name):
    file1 = open(file_name, "r")
    file2 = open(str(friend_name) + ".txt", "w")
    for i in file1:
        print(i, file=file2, end="")


def send_safe_message(file_name, friend_name, key):
    in_file = open(file_name, 'r')
    file_name = "{}.txt".format(friend_name)
    out_file = open(file_name, 'w')
    for message in in_file:
        new_message = encode(message[:-1], key)
        print(new_message, file=out_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    in_file = open(file_name, 'r')
    key = open(pad_file_name, 'r')
    key_format = key
    file_name = "{}.txt".format(friend_name)
    out_file = open(file_name, 'w')
    read = in_file.read()
    new_message = encode_better(read, key_format)
    print(new_message[:-1], file=out_file)

if __name__ == '__main__':
    pass
