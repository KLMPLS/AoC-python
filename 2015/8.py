x = open("taskfiles/8.txt","r")
x = x.read()
x = x.splitlines()
ans = 0
ans_2 = 0
for i in x:
    z = 0
    ans += 2
    i = [*i]
    i.pop(0)
    i.pop(-1)
    print(i)
    while z < len(i):
        print(i[z])
        if z+1 < len(i):
            if i[z] == "\\" and i[z+1] == "\\":
                ans += 1
                z += 1
            elif i[z] == "\\" and i[z+1] == "x":
                ans += 3
                z += 3
            elif i[z] == "\\" and i[z+1] == '"':
                ans += 1
                z += 1
        z += 1
    z = 0
    ans_2 += 4
    while z < len(i):
        if i[z] == "\\":
            ans_2 += 1
        elif i[z] == '"':
            ans_2 += 1
        z += 1
print(ans)
print(ans_2)