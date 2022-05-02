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

Output: Valid email addresses
Spence@abc.com
penn5@ebbb.net
BHood@aZd.edu
C-b@lol.net

Valid email address:
1) email format has to be usernname@domain.extension
2) username has to be alphabetical letters (A-Z, a-z), numbers, or '-' (and '-' cannot be the leading character)
3) domain has to be alphabetical letters (A-Z, a-z)
4) extension has to be one of 'com', 'net', 'edu', and 'gov'

pattern = r'\s([A-Za-z0-9]+[A-Za-z0-9-]+-?@[A-Za-z]*\.(?:net|com|edu|gov))'
'''

import re

with open ("input.txt", 'r') as file:
    for line in file:
        pat = re.compile('[A-Za-z0-9]+[A-Za-z0-9-]+?@[A-Za-z]+\.(?:.net|.com)')
        if re.search(pat, line):
            print("VALID")
