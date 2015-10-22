#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class
"""

import sys

from basic.util import times

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

def count_words(filename):
    """helper method for the other 2, return dict"""
    # read file into words
    times.seg_start('count words start')
    f = open(filename, 'rU')
    word_count = {}
    for line in f:
        words = line.split()
        for word in words:
            word = word.lower()
            if word in word_count:    # 0.069 for 640k
            #if word_count.get(word): # 0.03s for 250k text, 0.084 for 640k
                word_count[word] += 1
            else:
                word_count[word] = 1
    times.seg_stop('count words stop')
    return word_count

def print_words(filename):
    "count words"
    #sort dict and print
    word_count = count_words(filename)
    for word in sorted(word_count.keys()):
        print word, word_count[word]


def print_top(filename):
    word_count = count_words(filename)
    word_count_pairs = word_count.items()
    times.seg_start('sorting start')
    word_count_pairs = sorted(word_count_pairs, key = lambda pair: pair[-1], reverse=True)
    times.seg_stop('sorting stop')
    for i in range(3):
        print word_count_pairs[i][0], word_count_pairs[i][1]
    times.last_seg()

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)
  times.start(5)
  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)
  times.end()
if __name__ == '__main__':
  main()
