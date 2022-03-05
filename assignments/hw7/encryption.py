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

def encode_better():
    message = input("Enter a message: ")
    keyword = input("Enter a keyword: ")
    new_message = ""
    key_len = len(keyword)  # gets length of keyword to loop through it
    acc = 0
    for character in message:
        accu = acc % key_len  # doesn't allow it to ge out of range of slice
        mess_val = ord(character)
        key_char = keyword[accu]  # pulls the character of the keyword
        key_val = ord(key_char)
        mess_dif = mess_val - 65
        difference = key_val - 65
        mod_dif = (mess_dif + difference) % 58
        new_int = mod_dif + 65
        new_char = chr(new_int)
        new_message = new_message + new_char
        acc = acc + 1  # accumulator part
    print(new_message)