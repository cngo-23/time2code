'''
Input: A file with following content
Firstname Lastname Email
Suhayb Spence Spence@abc.com
Abdur Penn penn5@ebbb.net
Kai Gilbert k-gil@goooo .edu
Leanne Rasmussen -lrasmussen@xyz.gov
Aydin Moore amoore-@efg.con
Dennis Bartlett 66dbartlett@hell0.com
Jeremy Shaffer j_saffer@this.com
Brenden Hood BHood@aZd.edu
Carlton Burrows C-b@lol.net
Derry Figueroa Figueroa-2$php.com
 
'''

'''
- What's a valid email
- both mix of letters?
- .com .net .gov?
'com', 'net', 'edu', and 'gov'
'''
domains = ['com', 'net', 'edu',  'gov']
results = []
with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip().split(" ")
        email = str(line[2])
        if (email[-3:]) in domains:
            if '@' in email:
                host, domain = email.split('@')
                results.append(email)
                
for site in results:
    print(site)


