## Questions: return the top 10 words from a file.
# meaning return words that show 10 or more times

# ignore words that are under 10 times

# only words
# does upper and lowercase matter?
# numbers

results = {}

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip().split()
        for word in line:
            ## assume we only care for word, can be upper or lowercase
            if word.lower() not in results:
                results[word.lower()] = 1
            else:
                results[word.lower()] += 1

## if order does not matter we just can look for values greater than 10 and print
for x, y in results.items():
    if y >= 10:
        output = str(x) + " " + str(y)
        print(output)

