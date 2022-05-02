

## time date pid status
## can there be multiple starts?
## do we have to encounter days?
import datetime
results = {}

with open ("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        times, dates, pid, status = line.split(' ')
        print(times)
        print(dates)
        d = datetime.strptime(f'{times} {dates}', "%H:%M:%S %m/%d/%Y")
        if status == 'start':
            results[pid] = d
        else:
            diff = d - results[pid]
            #print(pid + ' ' + str(diff))


'''
process = defaultdict(list)
with open(filename, 'r') as file:
    file.readline()
    for line in file:
        time, date, pid, status = line.strip().split()
        d = datetime.strptime(f'{time} {date}', "%H:%M:%S %m/%d/%Y")
        if status == 'start':
            process[pid] = d
        else:
            diff = d - process[pid]
            print(pid + ' ' + str(diff))
'''
