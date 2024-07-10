task = open("taskfiles/7.txt", "r")
task = task.read()
task = task.splitlines()
all_values = {}



while len(task) > 0:
    print(len(task))
    print(all_values)
    for n,i in enumerate(task):
        p = i.split()
        try:
            if p[0] == "NOT":
                if p[1].isdigit():
                    save_v3 = int(p[1])
                else:
                    save_v3 = all_values[p[1]]
                all_values[p[3]] = 65536 + ~save_v3
                task.pop(n)
                continue
            if p[0].isdigit():
                save_v1 = int(p[0])
            else:
                save_v1 = all_values[p[0]]

            if len(p) == 3:
                all_values[p[2]] = save_v1
                task.pop(n)
                continue

            if p[2].isdigit():
                save_v2 = int(p[2])
            else:
                save_v2 = all_values[p[2]]

            if p[1] == "AND":
                all_values[p[4]] = save_v1 & save_v2
            elif p[1] == "OR":
                all_values[p[4]] = save_v1 | save_v2
            elif p[1] == "LSHIFT":
                all_values[p[4]] = save_v1 << save_v2
            elif p[1] == "RSHIFT":
                all_values[p[4]] = save_v1 >> save_v2

            task.pop(n)
        except KeyError:
            continue

print(all_values)

#for part 2 manualy changed the value on the input file thats it