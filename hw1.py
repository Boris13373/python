from sys import argv

def zp():
    try:
        time, rat, prem = map(float, argv[1:])
        print(f"Зарплата {time * rat + prem}")
    except ValueError:
        print("Введите 3 числа")

zp()