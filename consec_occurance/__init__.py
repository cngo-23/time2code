'''
Given a string 'aaabbccaddde' count consecutive characters and output the 3 most common occurrences.
If there is a tie, then take the first letter.
'''

# Test Cases
# - aaabbccadde
# - aabbccee
# - a
# - empty
# - AabB
results = {}

with open("intput.txt", 'r') as file:
    for line in file:
        for letter in line:
            if letter not in results:
                results[letter] = 1
            else:
                results[letter] += 1

sorted_letters = sorted(results.items(), key = lambda x: x[1])
for i in sorted_letters[:3]:
    print(i)


