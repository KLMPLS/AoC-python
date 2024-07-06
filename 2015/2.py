x = open("taskfiles/2.txt", "r")
x = x.read()
x = x.splitlines()
dimensions = []
print(x)
for i in x:
    dimensions += [i.split("x")]
sum_of_all = 0
for i in dimensions:
    l_and_w = int(i[0]) * int(i[1])
    w_and_h = int(i[2]) * int(i[1])
    h_and_l = int(i[0]) * int(i[2])
    sum_of_all += l_and_w * 2 + w_and_h * 2 + h_and_l * 2 + min(l_and_w, w_and_h, h_and_l)
print("ammount of paper needed:",sum_of_all)
sum_of_ribbon = 0
for i in dimensions:
    l = int(i[0])
    w = int(i[1])
    h = int(i[2])
    dims = [l, w, h]
    smth = [l, w, h]
    smth.pop(smth.index(min(dims)))
    sum_of_ribbon += min(dims)*2 + min(smth)*2 + l*w*h
print("the amount needed ribbon:",sum_of_ribbon)