# Is Anagram

# Given two strings s and t , write a function
# to determine if t is an anagram of s.

# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false


def is_anagram(s, t):
    if len(s) != len(t):
        return False

    letter_counts = {}

    for letter in s:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    for letter in t:
        if letter in letter_counts:
            letter_counts[letter] -= 1

    for value in letter_counts.values():
        if value != 0:
            return False

    return True
