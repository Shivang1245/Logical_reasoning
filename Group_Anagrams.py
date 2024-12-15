# Question:- Find the anagrams in the given list and print them in a collection of list

from collections import defaultdict

anangram = ['cat', 'tac', 'bat', 'tab', 'abc','cab', 'def','fed']

def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = [0] *26
        for c in s:
            key[ord(c) - ord('a')] += 1
        key = tuple(key)
        groups[key].append(s)
    return groups.values()

print(groupAnagrams(anangram))
