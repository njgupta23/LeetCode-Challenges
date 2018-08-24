# Excel Sheet Column Number
 

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# Example 1:

# Input: "A"
# Output: 1
# Example 2:

# Input: "AB"
# Output: 28
# Example 3:

# Input: "ZY"
# Output: 701


def titleToNumber(s):
     
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {}
    for i in range(len(alpha)):
        d[alpha[i]] = i+1
    
    num = 0
    exp = len(s)-1
    
    for char in s:
        num += d[char]*(26**exp)
        exp -= 1
    
    return num
