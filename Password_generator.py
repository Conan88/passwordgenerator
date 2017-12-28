#!/usr/bin/python3

import random
import string
import os
import json
import platform

"""
-----------------------------------------------
Password generator for making secure passwords!
-----------------------------------------------
This generator makes a 20 digits password including a random combination of:
0123456789
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
with around 100bits strength
"""
operating_system = platform.system() 

#generates the password
def randompassword():
    return ''.join([random.choice(string.printable.join(string.printable.split())) for _ in range(20)])

#converts words to hex numbers
def word_to_numbers(name):
    return ''.join('{:02x}'.format(ord(c)) for c in name)

#convert hex numbers to words
def numbers_to_words(name): 
    return ''.join([chr(int(''.join(c), 16)) for c in zip(name[0::2],name[1::2])])

#check if the name exists
def check_name(name):
    with open("password.json") as infile:
        data = json.loads(infile.read())
        d = dict(data)
    w = word_to_numbers(name)
    if w in d.keys():
        return True
    else:
        return False

#generates a new password, and saves it to the file
def save_password(name):
    with open("password.json") as infile:
        data = json.loads(infile.read())
        d = dict(data)

    with open("password.json", "w+") as outfile:
        password = randompassword()
        name_as_number = word_to_numbers(name)
        dictionary = {name_as_number:password}
        d = dict(data.items() | dictionary.items())
        json.dump(d, outfile)

#updates the password of an existing key
def update_password():
    with open("password.json") as infile:
        data = json.loads(infile.read())
        d = dict(data)
    w = word_to_numbers(name)
    if w in d.keys():
        with open("password.json", "w+") as outfile:
            password = randompassword()
            name_as_number = word_to_numbers(name)
            dictionary = {name_as_number:password}
            d = dict(data.items() | dictionary.items())
            json.dump(d, outfile)

#returns the password after searching for the key
def get_password(name):
    with open("password.json") as infile:
        data = json.loads(infile.read())
        d = dict(data)
        name_as_number = word_to_numbers(name)
        if name_as_number in d.keys():
            print(numbers_to_words(name_as_number),":",d[name_as_number])

#delete a password
def delete_password(name):
    with open("password.json") as infile:
        data = json.loads(infile.read())
        d = dict(data)
        name_as_number = word_to_numbers(name)
        if name_as_number in d.keys():
            del d[name_as_number]
            with open("password.json", "w+") as outfile:    
                json.dump(d, outfile)
        
#prints a list of all password
def print_all():
    with open("password.json") as infile:
        data = json.loads(infile.read())
        d = dict(data)
        for key in d.keys():
            print(numbers_to_words(key),":",d[key])

#function for making password.json file on linux/mac
def make_file_linux():
    os.system("echo '{}' > password.json")

#function for making password.json file on windows
def make_file_windows():
    os.system("echo {} > password.json")

def check_if_file_exists_linux():
    if os.path.exists("./password.json"):
        return True
    else:
        return False

def check_if_file_exists_windows():
    if os.path.exists("dir password.json"):
        return True
    else:
        return False

if operating_system is "Windows":
    if check_if_file_exists_windows() is False:
        make_file_windows()
else:
    if check_if_file_exists_linux() is False:
        make_file_linux()

print("This is a password generator, that also stores your password in a key value store")
print("Here are your options: ")
print("1.Generate new password.")
print("2.Get a password.")
print("3.See all keys.")
print("4.Delete a key.")
inputUser = int(input("Enter 1, 2, 3 or 4: "))

if inputUser == 1:
    print("")
    name = input("Give the password a name: ")
    check_name(name)
    if check_name(name) == True:
        print("Name already exists!")
        print("1.Update password?")
        print("2.Type in a new name?")
        name_exist_choice = int(input("Enter 1 or 2: "))
        if name_exist_choice == 1:
            update_password()
        if name_exist_choice == 2:
            new_name = input("Type in the new name: ")
            save_password(new_name)
    else:
        save_password(name)
if inputUser == 2:
    print("")
    name = input("What password would you like to get? ")
    if check_name(name) == True:
        get_password(name)
    else:
        print("Name don't exist")
        
if inputUser == 3:
    print_all()

if inputUser == 4:
    name = input("What password would you like to delete? ")
    delete_password(name)

   
   



