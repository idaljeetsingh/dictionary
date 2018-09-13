'''
    Title:          Dictionary
    Author:         Daljeet Singh Chhabra
    Language:       Python
    Date Created:   18-08-2018
    Last Modified:  13-09-2018
'''

import json                                     # Standard JSON Library
import os
from difflib import get_close_matches as gcm    # Library for matching similar words

data = json.load((open("data.json")))           # Importing the data set file into memory


print(type(data))


def look(word):
    word = word.lower()                         # Converting entered word to lowercase for searching
    matches = gcm(word, data.keys())            # Storing similar/matching words into a list

    if word in data:                            # Searching in the data set
        for i in data[word]:
            print("●", i)
        return
    elif word.title() in data:  # if user entered "delhi" this will check for "Delhi" as well.
        for i in data[word.title()]:
            print("●", i)
        return
    elif word.upper() in data:  # if user entered "USA" this will check for "USA" as well.
        for i in data[word.upper()]:
            print("●", i)
        return
    elif len(matches) > 0:
        print("Did you meant \"%s\" ? " % matches[0], end="")
        ch = input()
        ch.lower()
        if ch == 'y' or ch == 'yes' or ch == 'yep':
            for i in data[matches[0]]:
                print("●", i)
            return
        else:
            print(f'Sorry, but currently no such word like {word} exist in the data set...')
            print("Do you want to add it to the Dictionary ? : ")
            ch = input()
            ch.lower()
            if ch == 'y' or ch == 'yes' or ch == 'yep':
                addword(word)
            return
    else:
        print("The word doesn't exist!!!. Please double check it.")
        return


def addword(word):
        print(f"Enter the meaning of word {word}. In case of multiple meanings, separate them with a ';' .\n\n")
        print("Enter meaning: ", end="")
        meaning = input().split(';')
        data.update({word: meaning})
        with open('newDict.json', 'w') as file:
            file.write(json.dumps(data))
        os.remove('data.json')
        os.rename('newDict.json', 'data.json')


def main():
    w = input("Enter a word: ")                 # Input of a word from user
    print(f"\nMeaning of {w}: \n")

    look(w)                                     # Function to search the meaning of entered word


main()
