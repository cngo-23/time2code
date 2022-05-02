'''
input: a file and a number N
output: print out the last N lines of the file
'''

# Edge Cases
# What if N is less than file
# Empty file name
# What is a new line

k = 20
results = []
with open("random.txt", 'r') as file:
    for line in file:
        results.append(line)
    if k > len(results):
        k = len(results)
    for i in (results[-k:]):
        print(i)

