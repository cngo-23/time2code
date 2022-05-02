result = {}

with open("input.txt", 'r') as file:
	for line in file:
		line = line.strip().split()
		for word in line:
			if word not in result:
				result[word] = 1
			else:
				result[word] += 1

sorted_words=sorted(result.items(), key=lambda x:x[1], reverse=True)

counter = prev = 0
answer = ""
output = []

for x,y in sorted_words:
	if counter < 3 or prev == y:
		answer = str(x) + " " + str(y)
		counter += 1
		prev = y
		print(answer)
		output.append(answer)
	else:
		break

print(output)
