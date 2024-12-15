# Question:- Given an array of integers [nums] and an integer [target], return indices of two numbers such that they add up to the target

Arr = [2, 7, 11, 15]
target = 13

def returnPos(GivenArray, targetValue):
    hashmap = {} # contains  number:index. Empty at start

    for i in range(0, len(GivenArray)):
        y = targetValue - GivenArray[i]
        if y in hashmap:
            return (i, hashmap[y])

        a = hashmap[GivenArray[i]] = i

print(returnPos(Arr, target))

# What we are doing is that we are taking an integer from the array and then subtracting it from the target value
# if the target value after subtraction[targetValue - GivenArray[i]] is present in the hashmap then the index of array
# and the index at which value is present in hashmap. If the value is not present then the value is added to the hashmap.
