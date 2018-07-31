# Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321

# Example 2:

# Input: -123
# Output: -321

# Example 3:

# Input: 120
# Output: 21


def reverse(x):
        
    if x >= 0:
        y = [int(num) for num in str(x)]
    else:
        y = [int(num) for num in str(-1*x)]
    
    if y[-1] == '0':
        y = y[:-1]
    
    
    for i in range(len(y)/2):
        save = y[i]
        y[i] = y[-(i+1)]
        y[-(i+1)] = save

    elif x < 0:
        return int('-' + ''.join(str(e) for e in y))
    else: 
        return int(''.join(str(e) for e in y))
