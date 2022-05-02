'''
Given an array of integers greater than zero, find if there is a way to split the array in two(without
reordering any elements) such that the numbers before the split add up to the numbers after the split.
If so, print the two resulting arrays

split_sum([4, 6, 8, 2]) --> [4, 6] [8, 2]
'''

array = [4, 6, 8, 2, 10, 6, 4]
# array = [4, 6, 8, 2, 10, 6, 4, 2, 1, 6]
#array = [4]
#array = []


a = []
b = []
total = 0

if len(array) <= 1:
    print(array)
    exit()
else:
    halfSum = sum(array) // 2
    for i in array:
        total += i
        if total <= halfSum and len(b) == 0:
            a.append(i)
        else:
            total -= i
            b.append(i)
    if len(a) == 0:
        print([b])
        exit()
    elif total == sum(array):
        print("Could not complete")
    else:
        print([a] + [b])

