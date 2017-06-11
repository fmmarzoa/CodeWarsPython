# https://www.codewars.com/kata/alphabetic-anagrams/python
from math import factorial


def calc_prev_perms(word):
    rtn = 0
    if len(word):
        glyphs = sorted(set(word))
        fact = factorial(len(word))
        rtn = (fact // len(word)) * glyphs.index(word[0])
        rtn += calc_prev_perms(word[1:])
    return rtn


def list_position(word):
    """Return the anagram list position of the word"""
    return calc_prev_perms(word) + 1
