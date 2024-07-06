task = open("taskfiles/5.txt", "r")
task = task.read()
task = task.splitlines()
vowels = 'aeiou'
letters = [chr(i)*2 for i in range(97,123)]
forbiden = ["ab","cd","pq","xy"]
print(letters)
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
