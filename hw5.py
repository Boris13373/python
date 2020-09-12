from functools import reduce

def l_list(el1, el2):
    return el1*el2


k_list =[ el for el in range(100, 1001, 2)]
print(f"Лист\n{k_list}\nУмножение чисел\n{reduce(l_list, k_list)}")