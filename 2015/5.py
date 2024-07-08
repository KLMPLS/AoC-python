task = open("taskfiles/5.txt", "r")
task = task.read()
task = task.splitlines()
vowels = 'aeiou'
letters = [chr(i)*2 for i in range(97,123)]
forbiden = ["ab","cd","pq","xy"]
part_one = 0
for line in task:
    smth = True
    for forbid in forbiden:
        if forbid in line:
            smth = False
    if smth:
        vowels_count = 0
        for char in vowels:
            if char in line:
                vowels_count += line.count(char)
        if vowels_count >= 3:
            for letter_x2 in letters:
                if letter_x2 in line:
                    part_one += 1
                    print(line)
                    break
print(part_one)

part_two = 0
for line in task:
    z = 0
    while z != len(line):
        to_check = line[z:z+2]
        print(to_check)
        if to_check in line[z+2:]:
            print(line)
            for h,i in enumerate(line[:len(line)-2]):
                if i == line[h+2]:
                    print(line)
                    part_two += 1
                    break
            break
        z += 1
print(part_two)