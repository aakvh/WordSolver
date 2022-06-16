#!/usr/bin/env python3

import pickle
import sys

with open('wordlist', 'rb') as f:
    lst = pickle.load(f)

if len(sys.argv) != 2:
    print('Wrong input!!')
    sys.exit()

char = sys.argv[1].upper().split(' ')

def wordsolver():
    #char = input('give me the list;\n')
    matched = []
    for i in lst:
        if all([c in i for c in char]):
            matched.append(i)
    for i in matched:
        print(i.capitalize())

if __name__ == '__main__':
    wordsolver()
