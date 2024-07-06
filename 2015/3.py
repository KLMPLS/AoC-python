task = open("taskfiles/3.txt", "r")
task = task.read()
visited_houses = []
x = 0
y = 0
houses_that_recived_presents = 0
for i in task:
    if [x, y] not in visited_houses:
        houses_that_recived_presents += 1
        visited_houses.append([x, y])
    if i == "^":
        y += 1
    elif i == "v":
        y -= 1
    elif i == ">":
        x += 1
    elif i == "<":
        x -= 1
print("houses that recived presents:", houses_that_recived_presents)
santa = [task[i] for i in range(0, len(task), 2)]
robo_santa = [task[i] for i in range(1, len(task), 2)]
x_santa = 0
y_santa = 0
x_robo_santa = 0
y_robo_santa = 0
houses_that_recived_presents_two_santas = 0
visited_houses = []
for i in santa:
    if [x_santa, y_santa] not in visited_houses:
        houses_that_recived_presents_two_santas += 1
        visited_houses.append([x_santa, y_santa])
    if i == "^":
        y_santa += 1
    elif i == "v":
        y_santa -= 1
    elif i == ">":
        x_santa += 1
    elif i == "<":
        x_santa -= 1

for i in robo_santa:
    if [x_robo_santa, y_robo_santa] not in visited_houses:
        houses_that_recived_presents_two_santas += 1
        visited_houses.append([x_robo_santa, y_robo_santa])
    if i == "^":
        y_robo_santa += 1
    elif i == "v":
        y_robo_santa -= 1
    elif i == ">":
        x_robo_santa += 1
    elif i == "<":
        x_robo_santa -= 1
print("wow the two santas did even worse:",houses_that_recived_presents_two_santas)