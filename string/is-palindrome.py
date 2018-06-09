# Valid Palindrome

# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.


def isPalindrome(s):

    letters = 'abcdefghijklmnopqrstuvwxyz0123456789'

    lower = s.lower()
    lower_list = []

    for i in range(len(lower)):
        if lower[i] in letters:
            lower_list.append(lower[i])

    for i in range(len(lower_list)/2):
        if lower_list[i] in letters and lower_list[-(i+1)] in letters:
            if lower_list[i] != lower_list[-(i+1)]:
                return False

    return True
