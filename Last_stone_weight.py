''' Question:- Given an array [nums] of distinct integers, return all the possible permutations. You can return
the answer in any order
'''

nums = [1,2,3,4,5]


def Permutations(arr):
    n = len(arr)
    ans, sol = [], []

    def backtrack():
        if len(sol) == n:
            ans.append(sol[:])
            return

        for x in nums:
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()
    backtrack()
    return ans
print(Permutations(nums))

# We are backtracking all the possible combinations in the case of the given list.