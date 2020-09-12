my_list = [14, 18, 20, 2, 5, 3, 8, 10]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num -1]]
print(more_then)