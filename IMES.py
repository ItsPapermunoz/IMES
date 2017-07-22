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
    os.system("pause")


def fetch():
    os.system("cls")
    filename = input("Please enter file name...") + ".txt"
    print("Fetching file...")
    os.system("pause")
    try:
        file = open("{}".format(filename), "r")
        print("File fetched!")
        return filename
    except FileNotFoundError:
        print("File does not exist...")
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
        char = 0
    elif char == "A" or char == "a":
        char = 1
    elif char == "B" or char == "b":
        char = 2
    elif char == "C" or char == "c":
        char = 3
    elif char == "D" or char == "d":
        char = 4
    elif char == "E" or char == "e":
        char = 5
    elif char == "F" or char == "F":
        char = 6
    elif char == "G" or char == "g":
        char = 7
    elif char == "H" or char == "h":
        char = 8
    elif char == "I" or char == "i":
        char = 9
    elif char == "J" or char == "j":
        char = 10
    elif char == "K" or char == "k":
        char = 11
    elif char == "L" or char == "l":
        char = 12
    elif char == "M" or char == "m":
        char = 13
    elif char == "N" or char == "n":
        char = 14
    elif char == "O" or char == "o":
        char = 15
    elif char == "P" or char == "p":
        char = 16
    elif char == "Q" or char == "q":
        char = 17
    elif char == "R" or char == "r":
        char = 18
    elif char == "S" or char == "s":
        char = 19
    elif char == "T" or char == "t":
        char = 20
    elif char == "U" or char == "u":
        char = 21
    elif char == "V" or char == "V":
        char = 22
    elif char == "W" or char == "w":
        char = 23
    elif char == "X" or char == "x":
        char = 24
    elif char == "Y" or char == "y":
        char = 25
    elif char == "Z" or char == "z":
        char = 26
    elif char == "0":
        char = "A"
    elif char == "1":
        char = "B"
    elif char == "2":
        char = "C"
    elif char == "3":
        char = "D"
    elif char == "4":
        char = "E"
    elif char == "5":
        char = "F"
    elif char == "6":
        char = "G"
    elif char == "7":
        char = "H"
    elif char == "8":
        char = "I"
    elif char == "9":
        char = "J"
    return char


def new_file(x, y, z):
    try:
        file = open("{}".format(x), "r")
        file.close()
        os.remove("{}".format(x))
        new_file(x,y,z)
    except FileNotFoundError:
        file = open("{}".format(x), "w")
        file.write("THIS FILE HAS BEEN ENCRYPTED USING IMES\n")
        file.write(z + "\n")
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
        test = int(x)
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
    if filename == None:
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
        if replaced == code:
            code += code
            code_changed += 1
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
    data = str(replaced) + str(code_changed)
    imes_file = "IMES {}".format(filename)
    new_file(imes_file,etext, data)


def find_char(x):
    i = 0
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
        z = file.readline()
        y = file.read()
        file.close()
        return z, y
    else:
        print("File is Not encrypted!")
        os.system("pause")
def decrypt():
    filename = fetch()
    code = get_code()
    original_code = len(code)
    code = original_code
    code_changed = 0
    replaced = 0
    trash = ""
    is_int = False
    decrypt_code = []
    if filename == None:
        return
    data, txt = check_encrypted(filename)
    replaced, code_changed, trash = data
    replaced = int(replaced)
    code_changed = int(code_changed)
    e_char_ls = find_char(txt)
    e_char_ls.reverse()
    e_char = None
    for char in e_char_ls:
        is_int = check_int(char)
        if is_int is True:
            debug = char
            debug = int(debug)
        else:
            decrypt_code.append(char)
            continue
        if replaced != 0:
            e_char = debug - code
            replaced -= 1
        else:
            if code_changed == 0:
                code = code * original_code
                code_changed = original_code
                replaced = original_code
                e_char = debug - code
                replaced -= 1
            else:
                code = code / 2
                code_changed -= 1
                replaced = original_code
                e_char = debug - code
                replaced -= 1
        if e_char < 0:
            e_char += 26
        decrypt_code.append(e_char)
    print(decrypt_code)

# Main Code
decrypt()
