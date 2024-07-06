x = open("taskfiles/1.txt","r")
x = x.read()
floor = 0
once = 0
for z,i in enumerate(x):
    if i == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1 and once == 0:
        print("first occurance of floor -1:",z)
        once = 1
print("final floor:",floor)
