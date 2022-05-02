from datetime import datetime

with open("input.txt", 'r') as file:
    for line in file:
        time,date = line.strip().split()
        d = datetime.strptime(f'{time} {date}', "%H:%M:%S %m/%d/%Y")
        print(d)