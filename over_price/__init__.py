'''
Input: a file with the following content
apple 10/02/2020 $3.99
banana 10/02/2020 $4.05
milk 10/03/2020 $3.88
apple 10/02/2020 $4.99
apple 10/02/2020 $4.09
banana 10/02/2020 $4.15
milk 10/03/2020 $3.88
banana 10/02/2020 $3.85
banana 10/02/2020 $3.95
milk 10/03/2020 $4.01

Output: the percentage for each item that its price is over $4
'''
result = {}

with open ("file.txt", 'r') as file:
    for line in file:
        item, date, cost = line.strip().split()
        total = flag = 0
        total = 1
        if float(cost[1:]) > 4.00:
            flag = 1
        if item not in result:
            result[item] = [total, flag]
        else:
            result[item][0] += total
            result[item][1] += flag
    for item in result:
        print(f'{item}: {float(result[item][1] / result[item][0] * 100):.2f}%')


'''

apple: 66.7%
banana: 50.0%
milk: 33.3%

items = {}
with open("file.txt", 'r') as f:
    for line in f:
        total = over = 0
        name, date, cost = line.strip().split()
        total = 1
        if float(cost[1:]) > 4.00:
            over = 1
        if name not in items:
            items[name] = [total, over]
        else:
            items[name][0] += total
            items[name][1] += over
for item in items:
    print(f'{item}: {float(items[item][1] / items[item][0] * 100):.1f}%')
'''