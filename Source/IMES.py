# Imports

import os

# Variables

__author__ = "Rodrigo 'ItsPaper' Muñoz"
__authoremail__ = "Rodrigo.mcuadrada@gmail.com"
__version__ = "Alpha"

# Functions


def welcome():
    print("Welcome to IMES: Itspaper's Message Encryption System!")
    print("Made by: {}. You are using Version: {}".format(__author__, __version__))


def fetch():
    os.system("cls")
    filename = input("Please enter file name...") + ".txt"
    print("Fetching file...")
    os.system("pause")
    try:
        file = open("{}".format(filename), "r")
        file.close()
        print("{} fetched!".format(filename))
        os.system("pause")
        return filename
    except FileNotFoundError:
        print("{} does not exist...".format(filename))
        os.system("pause")


def contact_us():
    print("Thank you for sending me your feedback at {}.".format(__authoremail__))


def grab_text(x):
    file = open("{}".format(x))
    txt = file.read()
    file.close()
    return txt


def replace(char):
    if char == " ":
        return 0
    elif char.isalpha():
        return ord(char.lower()) - 96
    elif char.isnumeric() and int(char) < 10:
        return chr(int(char) + 65)


def new_file(x, y):
    try:
        file = open("{}".format(x), "r")
        file.close()
        os.remove("{}".format(x))
        new_file(x, y)
    except FileNotFoundError:
        file = open("{}".format(x), "w")
        file.write("THIS FILE HAS BEEN ENCRYPTED USING IMES\n")
        file.write(y)
        file.close()


def get_code():
    os.system("cls")
    code = input("Please enter encryption code...")
    if code == "":
        os.system("cls")
        code = input("Code must be at least one Character long...")
    return code


def check_int(x):
    # This Function Checks if character is a number or a letter.
    try:
        int(x)
        y = True
    except ValueError:
        y = False
    finally:
        return y


def encrypt():
    filename = fetch()
    code = get_code()
    original_code = len(code)
    code = original_code
    code_changed = 0
    replaced = 0
    if filename is None:
        return
    txt = grab_text(filename)
    etext = ""
    for char in txt:
        # For Each Character in text file replace character
        x = replace(char)
        y = check_int(x)
        if y is True:
            x += code
            while x > 26:
                x -= 26
        etext += str(x) + " "
        """Replaces each character in the text
        with its corresponding number from the alphabet +
        the number of letters in the code"""
        replaced += 1
        if replaced == original_code:
            code = code + original_code
            code_changed += 1
            replaced = 0
            """After the amount of replaced letters is the same
            of the number of letters in the code the number of letters
            in the code doubles"""
            if code_changed == original_code:
                """If the code has changed the same number of times
                than the number of letters in the original_code
                then the code goes back to its original form..."""
                code = original_code
                code_changed = 0
                replaced = 0
    imes_file = "IMES {}".format(filename)
    new_file(imes_file, etext)


def find_char(x):
    e_char = ""
    txt = []
    for char in x:
        if char == " ":
            txt.append(e_char)
            e_char = ""
            continue
        e_char += char
    return txt


def check_encrypted(x):
    file = open("{}".format(x), "r")
    x = file.readline()
    if x == "THIS FILE HAS BEEN ENCRYPTED USING IMES\n":
        y = file.read()
        file.close()
        return True, y
    else:
        print("File is Not encrypted!")
        os.system("pause")
        return False, False


def decrypt_char(char):
    if char == 1:
        dchar = "A"
    elif char == 2:
        dchar = "B"
    elif char == 3:
        dchar = "C"
    elif char == 4:
        dchar = "D"
    elif char == 5:
        dchar = "E"
    elif char == 6:
        dchar = "F"
    elif char == 7:
        dchar = "G"
    elif char == 8:
        dchar = "H"
    elif char == 9:
        dchar = "I"
    elif char == 10:
        dchar = "J"
    elif char == 11:
        dchar = "K"
    elif char == 12:
        dchar = "L"
    elif char == 13:
        dchar = "M"
    elif char == 14:
        dchar = "N"
    elif char == 15:
        dchar = "O"
    elif char == 16:
        dchar = "P"
    elif char == 17:
        dchar = "Q"
    elif char == 18:
        dchar = "R"
    elif char == 19:
        dchar = "S"
    elif char == 20:
        dchar = "T"
    elif char == 21:
        dchar = "U"
    elif char == 22:
        dchar = "V"
    elif char == 23:
        dchar = "W"
    elif char == 24:
        dchar = "X"
    elif char == 25:
        dchar = "Y"
    elif char == 26:
        dchar = "Z"
    elif char == "A":
        dchar = "0"
    elif char == "B":
        dchar = "1"
    elif char == "C":
        dchar = "2"
    elif char == "D":
        dchar = "3"
    elif char == "E":
        dchar = "4"
    elif char == "F":
        dchar = "5"
    elif char == "G":
        dchar = "6"
    elif char == "H":
        dchar = "7"
    elif char == "I":
        dchar = "8"
    elif char == "J":
        dchar = "9"
    elif char == 0:
        dchar = " "
    else:
        dchar = str(char)
    return dchar


def decrypt():
    filename = fetch()
    code = get_code()
    original_code = len(code)
    code = original_code
    replaced = 0
    code_changed = 0
    decrypt_code = []
    if filename is None:
        return
    is_encrypted, txt = check_encrypted(filename)
    if is_encrypted is False:
        return
    txt = find_char(txt)
    for instance in txt:
        is_int = check_int(instance)
        if is_int is False:
            decrypt_code.append(instance)
            continue
        else:
            char = int(instance)
        char -= code
        replaced += 1
        if replaced == original_code:
            code += original_code
            code_changed += 1
            replaced = 0
            if code_changed == original_code:
                code = original_code
                code_changed = 0
                replaced = 0
        if char < 0:
            char += 26
        decrypt_code.append(char)
    dtxt = ""
    for char in decrypt_code:
        dchar = decrypt_char(char)
        dtxt += dchar
    new_filename = input("Please enter the name for the new file...") + ".txt"
    while new_filename == ".txt":
        new_filename = input("Please enter a valid file name...") + ".txt"
    file = open("{}".format(new_filename), "w")
    file.write(dtxt)


def menu():
    os.system("cls")
    welcome()
    print("1.Encrypt File")
    print("2.Decrypt file")
    print("3.Send Feedback to author")
    menusel = input("Please enter the number of the option, or type exit to quit...")
    is_int = check_int(menusel)
    if is_int is True:
        if int(menusel) == 1:
            encrypt()
        elif int(menusel) == 2:
            decrypt()
        elif int(menusel) == 3:
            contact_us()
    elif menusel == "EXIT" or menusel == "exit" or menusel == "Exit":
        exit()
    else:
        print("Option not recognized! Please try again!")
        os.system("pause")


# Main Code

while True:
    menu()
