counter = 0
with open("hw2.txt","r") as f:
    for line in f:
        counter += 1
        line_w = line.split()
        print(line, 'Длинна  ', len(line_w))
    print('Строк', counter)
    