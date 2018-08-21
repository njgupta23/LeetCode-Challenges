# Group Anagrams

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


def groupAnagrams(strs):
      
    out = []
    d = {}
    
    for word in strs:
        if ''.join(sorted(word)) not in d:
            d[''.join(sorted(word))] = [word]
        else:
            d[''.join(sorted(word))].append(word)
    
    for anagrams in d.values():
        out.append(anagrams)
    
    return out
