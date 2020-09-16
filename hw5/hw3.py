with open("filehw3.txt", "r", encoding='utf-8') as f:
    s = []
    less = []
    line = f.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        s.append(i[1])

print(f"Зарплата меньше 20 000 {less}. Зарплата больше - {sum(map(float, s)) / len(s)} ")
