Arr = [2,3,45,1,10,100,71,55,45,0,-1, 3, 4]

#Question-1 Find the minimum element of the Array and then also find the second-lowest element of the Array

minelem = Arr[0]
minelemtwo = minelem

for i in range(0, len(Arr)):
    if Arr[i] < minelem:
        minelemtwo = minelem
        minelem = Arr[i]

print(minelem, minelemtwo)

#Question-2 Find the first largest element of the Array and then also find the second-largest element of the Array.

maxelem = Arr[0]
maxelemtwo = maxelem

for i in range(0, len(Arr)):
    if maxelem < Arr[i]:
        maxelem = Arr[i]

    if maxelemtwo < Arr[i] & Arr[i] != maxelem:
        maxelemtwo = Arr[i]

print(maxelem, maxelemtwo)
