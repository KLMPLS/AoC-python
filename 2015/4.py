import hashlib
i= 0
while True:
    z = f"iwrupvqb{i}"

    z = hashlib.md5(z.encode())


    if str(z.hexdigest())[:6] == '000000':
        print(z.hexdigest())
        break
    i += 1

print(i)
