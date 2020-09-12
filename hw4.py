from random import randint
l_list = [randint(-10, 10) for i in range(20)]
k_list = [el for el in l_list if l_list.count(el) == 1]
print(f"Исходный файл\n{l_list}\nНе повторяется\n{k_list}")