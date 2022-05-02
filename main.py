'''
Write a function that creates a cypher, write code that will take plaintext and change it by a certain number:

Example inputs (plaintext, shift)

Example Output (bag, 5)---> gfl
'''

# We want to create a cypher
# Code that takes plaintext and changes it by a certain number
# output the result

#bag + 5 = gfl
#ape + 1 = bsf
# + 5 = e
# a + 0 = a
# z + 1 = a

# a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z


def cypher(text, change):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    result = []

    for i in range(len(letters)):
        if letters[i] == text.lower():
            newLocation = i + change
            if newLocation > 26:
                newLocation %= 26
            return(letters[newLocation])
    return text


text = 'z'
change = 1

#print(cypher(text,change))


text = 'ZiZpPy'
change = 1

def cypherEdited(text, change):
    result = ""
    aPosUpper = ord('A')
    zPosUpper = ord('Z')
    aPosLower = ord('a')
    zPosLower = ord('z')
    if change < 1:
        return text
    for i in text:
        if ord(i) >= aPosUpper and ord(i) <= zPosUpper:
            newInt = ord(i) + change
            if newInt > zPosUpper:
                newInt = (newInt % zPosUpper)
        else:
            newInt = ord(i) + change
            if newInt > zPosLower:
                newInt = (newInt % zPosLower)
        result = result + (chr(newInt))
    return result

# print(cypherEdited(text,change))

test1 = "2:12:00, 9/12/2020, 000001 start"
print(test1)
test = test1.rsplit(", ",1)
print(test)
test = test1.rsplit(", ",2)
print(test)

