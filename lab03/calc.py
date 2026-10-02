def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        print('деление на ноль')
    return a / b



x = float(input("Первое число: "))
y = float(input("Второе число: "))
print("Результат:", div(x, y))