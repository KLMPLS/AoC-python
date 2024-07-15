def look_and_say(n):
    out = ""
    check = n[0]
    num = 0
    for i in n:
        if i == check:
            num += 1
        else:
            out += str(num)+check
            check = i
            num = 1
    out += str(num) + check
    return out

start = "1321131112"
for i in range(50): #change the range depending on how many times
    start = look_and_say(start)
print(start)
