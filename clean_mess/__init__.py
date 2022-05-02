'''
you are given a contact list messed up by someone. each line contains username, phone_num, start_date

input: file with the following content
Tom415-123-456710/09/2019
415-908-9999John10/10/2019
10/10/2019549-000-1234Jack
10/12/2019Mary312-999-1234
Larry415-123-456910/31/2019
415-908-1002Ken10/25/2019
10/29/2019549-000-1231Pam

output: create a new file with the following content (sorted by name)
Username Phone_num Start_date
Jack 549-000-1234 10/10/2019
John 415-908-9999 10/10/2019
'''

import re
name = r'[a-zA-Z]+'
date = r'\d{2}/\d{2}/\d{4}'
phone = r'\d{3}-\d{3}-\d{4}'
results = {}

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        names = re.search(name, line)
        dates = re.search(date, line)
        phones = re.search(phone, line)
        #print(names.group(0), dates.group(0), phones.group(0))
        results[names.group(0)] = [names.group(0), dates.group(0), phones.group(0)]
    sorted_names = sorted(results.items(), key = lambda x: x[0])
with open("output.txt", 'a') as output:
    for x,y in sorted_names:
        output.write((' ').join(y))
        output.write('\n')

