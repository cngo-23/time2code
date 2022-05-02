'''
input: you are given a log with the following content
time date pid action
2:12:00	9/12/2020 000001 start
3:22:15	9/13/2020 000002 start
4:42:45	9/14/2020 000003 start
5:44:55	9/15/2020 000002 end
6:42:45	9/16/2020 000001 end
7:32:25	9/17/2020 000004 start
8:41:45	9/18/2020 000005 start
9:42:45	9/19/2020 000006 start
10:22:45 9/20/2020 000004 end
11:41:41 9/21/2020 000007 start
12:42:05 9/22/2020 000005 end
13:52:45 9/23/2020 000008 start
14:52:15 9/24/2020 000006 end
15:02:25 9/25/2020 000008 end
16:42:45 9/26/2020 000003 end
17:22:35 9/27/2020 000007 end

output: print out the time spent for each process (identified by pid)
'''

from datetime import datetime

result = {}

with open("input.txt", 'r') as file:
    for line in file:
        time, date, pid, status = line.strip().split()
        d = datetime.strptime(f'{date} {time}', "%m/%d/%Y %H:%M:%S")
        if status == "start":
            result[pid] = d
        else:
            diff = d - result[pid]
            print(diff)