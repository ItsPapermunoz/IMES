# Imports

import os

# Variables

__author__ = "Rodrigo 'ItsPaper' Muñoz"
__authoremail__ = "Rodrigo.mcuadrada@gmail.com"
__version__ = "Beta"

# Functions


def welcome():
    # Prints basic program info
    print("Welcome to IMES: Itspaper's Message Encryption System!")
    print("Made by: {}. You are using Version: {}".format(__author__, __version__))


def grab_file():
    # Prompts the user for input on file name and returns text of file!
    filename = input("Please enter file name...") + ".txt"
    try:
        with open(filename, "r") as file:
            text = file.read
        return filename, text
    except FileNotFoundError:
        return False, False


def contact_us():
    print("Thank you for sending me your feedback at {}.".format(__authoremail__))


def replace(char):
    # Replaces given argument string with a given number or letter
    if char == " ":
        return 0
    elif char.isalpha():
        return ord(char.lower()) - 96
    elif char.isnumeric() and int(char) < 10:
        return chr(int(char) + 65)
    else:
        return char

def replace_code(code):
    key = []
    for char in code:
        encoded_char = replace(char)
        key.append(encoded_char)
    return key


def prompt_code():
    code = input("Please enter a keyword to be used as encryption code!")
    while len(code) < 1:
        code = input("Code must be at least 1 Character")
    return code


def check_int(char):
    # This Function Checks if character is a number or a letter.
    try:
        int(char)
        y = True
    except ValueError:
        y = False
    finally:
        return y


def encryption():
    filename, text = grab_file()
    print(text)
    if filename is False:
        return 1
    original_code = prompt_code()
    code_length = len(original_code)
    key = replace_code(original_code)
    i = 0
    etext = ""
    for char in text:
        echar = replace(char)
        is_int = check_int(echar)
        if is_int:
            echar += key[i]
            if i < code_length:
                i += 1
            else:
                n = 0
                for instance in key:
                    key_replace = instance + code_length
                    while key_replace > 26:
                        key_replace -= 26
                    key[n] = key_replace
                    n += 1
                i = 0
        etext += str(echar) + " "
    print(etext)
encryption()
