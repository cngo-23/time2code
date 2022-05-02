'''
input: a file with a list of random passwords
gyb6-qhdv-uk0d
wt52-e75r-fc5r
z80c-ddc4-eu2p
968s-r9Ir-1h9j
awgr_lnp1-4ejo
3yti-bydt-82e7
wt52-e75r-fc5r
l1q6-2doi-dei7
y3ti-p21i-y911-y911
7b2x-iv9gi-k4b
uamh-9m r-atoa
0w1a-0rSi-ibwq

output: valid distinct passwords
gyb6-qhdv-uk0d
z80c-ddc4-eu2p
3yti-bydt-82e7
l1q6-2doi-dei7

password format:
must be in form 'xxxx-xxxx-xxxx' where x is numbers or lower case letters
'''

import re
pattern= '^([a-z0-9]{4}\-){2}[a-z0-9]{4}$'
result = {}

with open("passwords.txt", 'r') as file, open("output.txt", 'a') as output:
    for line in file:
        line = line.strip()
        pattern = re.compile('^([a-z0-9]{4}\-){2}[a-z0-9]{4}$')
        if re.search(pattern, line):
            if line not in result:
                result[line] = 1
            else:
                result[line] += 1
for x,y in result.items():
    if y <= 1:
        print(x)

