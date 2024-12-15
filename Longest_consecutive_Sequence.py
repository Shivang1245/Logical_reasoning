# Question:- Given an unsorted array of integers [nums], return the length of the longest consecutive elements sequence

Arr = [100, 4, 200, 1, 3, 2]

def longestConsecutive(arr):
    s = set(arr)
    longest = 0
    for num in s:
        if num-1 not in s:
            current = 1
            while num+1 in s:
                current +=1
                num+=1

            longest = max(longest, current)
    return longest

print(longestConsecutive(Arr))

# Time complexity is O(n)