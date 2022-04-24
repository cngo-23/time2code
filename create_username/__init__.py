'''
Firstname Lastname EmployeeID StartDate
Kasey Cook 1 10/13/2000
Alya Ellis 2 10/14/2000
Raisa Grimes 3 10/15/2000
Kareem Dalby 4 10/16/2000
Karter Cook 5 10/17/2000
Kavan Cook 6 10/18/2000
Abubakar Parsons 7 10/19/2000
Hope Ortega 8 10/20/2000
Ty Neale 9 10/21/2000
Harun Wu 10 10/22/2000

output: a new file with username at the last column, the username is the first letter of the user and the lastname
(e.g. Kasey Cook -> kcook). If there's collision for usernames, the new one should add the next available integer to its end
(e.g. kcook, kcook2, kcook3) (we skip 1 to avoid confusion)
'''

names = {}
result = []

with open("input.txt", 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()
        line = line.split(' ')
        firstname = line[0][0]
        lastname = line[1]
        userID = firstname.lower() + lastname.lower()
        if userID not in names:
            names[userID] = 1
        else:
            names[userID] += 1
            userID = userID + str(names[userID])
        info = ""
        with open("output.txt", 'a') as output:
            for word in line:
                info += word + " "
            output.write(info + " " + userID + "\n")



