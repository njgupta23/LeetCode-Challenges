# Reverse string

# Write a function that takes a string as input
# and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".


def rev_str(s):

    l = []

    for char in s:
        l.append(char)

    for i in range(len(l)/2):
        save = l[i]
        l[i] = l[-(i+1)]
        l[-(i+1)] = save

    return "".join(l)
