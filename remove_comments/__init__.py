notStart = False

with open("test.py", 'r') as file, open('new_code.py', 'w') as output:
    for line in file:
        line = line.strip()
        #for word in line:
        if len(line) > 0:
            if line[0] == '#':
                pass
            elif line[:3] == '"""' and notStart == False:
                notStart = True

            elif line[:3] == '"""' and notStart == True:
                notStart = False

            elif notStart != True:
                output.write(line + '\n')
                print(line)
            else:
                continue

