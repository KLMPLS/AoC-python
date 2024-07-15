import itertools
x = open("taskfiles/9.txt","r")
x = x.read()
x = x.splitlines()
distances = {}
locations = []
for i in x:
    i = i.split()
    name = [i[0],i[1]]
    name.sort()
    name = name[0] + name[1]
    distances[name] = int(i[2])
    if i[0] not in locations:
        locations.append(f"{i[0]}")
    if i == x[-1].split():
        locations.append(f"{i[1]}")
print(distances)
print(locations)
shortest = 10000000000000000
longest = 0
for i in itertools.permutations(locations,len(locations)):
    z = 0
    current = 0
    while z < len(locations)-1:
        name = [i[z],i[z+1]]
        name.sort()
        name = name[0] + name[1]
        current += distances[name]
        z += 1
    if current < shortest:
        shortest = current

    if current > longest:
        longest = current

print(longest)
print(shortest)