task = open("taskfiles/6.txt", "r")
task = task.read()
task = task.splitlines()


board = [[0 for x in range(1000)] for y in range(1000)]
def fill(x_begin, y_begin, x_end, y_end, what):
    sdf = what
    for y in range(y_begin, y_end+1):
         for x in range(x_begin, x_end+1):
             if what == "?":
                 sdf = abs(board[y][x] - 1)
             board[y][x] = sdf


def fill_part2(x_begin, y_begin, x_end, y_end, what):
    sdf = what
    for y in range(y_begin, y_end+1):
         for x in range(x_begin, x_end+1):
            if board[y][x] + sdf >= 0:
                board[y][x] += sdf



for i in task:
    z = i.split()
    if z[0] == "on":
        to_fun = 1
    elif z[0] == "off":
        to_fun = 0
    elif z[0] == "toggle":
        to_fun = "?"
    else:
        print("what the fuck is a kilometer")
    fill(int(z[1]), int(z[2]), int(z[3]), int(z[4]), to_fun)

ans_p1 = 0
for i in board:
    ans_p1 += i.count(1)
print(ans_p1)
board = [[0 for x in range(1000)] for y in range(1000)]

for i in task:
    z = i.split()
    if z[0] == "on":
        to_fun = 1
    elif z[0] == "off":
        to_fun = -1
    elif z[0] == "toggle":
        to_fun = 2
    else:
        print("what the fuck is a kilometer")
    fill_part2(int(z[1]), int(z[2]), int(z[3]), int(z[4]), to_fun)


ans_p2 = 0
for i in board:
    ans_p2 += sum(i)
    print(i)
print(ans_p2)
