# Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", which the length is 3.
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence 
#              and not a substring.


# SLOW SOLUTION:

# def lengthOfLongestSubstring(s):

#     longest = 0
    
#     for i in range(len(s)):
#         seen = set()
#         l = 0
        
#         for j in range(i, len(s)):
#             if s[j] not in seen:
#                 seen.add(s[j])
#                 l += 1
#             else:
#                 break
#         if l > longest:
#             longest = l
            
#     return longest


# FASTER SOLUTION:

def lengthOfLongestSubstring(s):
       
    longest = l = i = 0
    seen = {}
    
    while i < len(s):
        if s[i] not in seen:
            seen[s[i]] = i
            l += 1
            i += 1
            longest = max(l, longest)
        else:
            i = seen[s[i]] + 1
            l = 0
            seen = {}
            
    return longest
