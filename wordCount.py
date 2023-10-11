#! /usr/bin/env python3
# Didi Guillen
# Last updated: 10/11/2023

from os import read, write
from sys import argv
import re

def checkPunc(str_in):
    new_str = ""
    for c in str_in:
        if(bool(re.search("[a-zA-Z]", c))):
            new_str += c
        else:
            continue
    return new_str

words = {}
file1 = open(argv[1], "r")
contents = file1.read()
file1.close()
split_contents = re.split('\s+',contents)
for c in split_contents:
    c = checkPunc(c)
    c = c.lower()
    if c in words.keys():
        value = words[c]
        words[c] = (value+1)
    else:
        words[c] = 1
outfile = open(argv[2], "w+")
outfile.seek(0)
outfile.truncate()
list_words = sorted(list(words.keys()))
for w in list_words:
    val = str(words[w])
    outfile.write(w+": "+val+"\n")
outfile.close()


