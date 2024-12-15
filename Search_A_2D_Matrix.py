''' Question:- You are given an m x n integer matrix with the following properties
1. Each row is sorted in a non-descending order
2. The first integer of each row is greater than the last integer of the previous row.

Given the integer [target], return [true] if [target] is in the [matrix] or [false] otherwise.
'''

matrix1= [[2,3,5,7], [10,11,16,20], [23,30,34,60]]

def Binarysearch(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    l, r= 0, m*n-1

    while l <= r:
        mid = (l+r)//2
        i, j = mid // n, mid % n

        if target == matrix[i][j+1]:
            return True
        elif target < matrix[i][j+1]:
            r = mid - 1
        else:
            l = mid + 1
    return False

print(Binarysearch(matrix1, target=24))

# Here we are doing a binary search to find out the middle element and comparing the target with it.