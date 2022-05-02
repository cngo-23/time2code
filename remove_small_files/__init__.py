import os

currentCWD = (os.getcwd())
for x, y, z in (os.walk('.')):
    print(x)
    print(y)
    #print(z)