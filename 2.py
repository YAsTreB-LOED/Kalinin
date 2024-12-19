a = input("Введите строку 1: ")
b = input("Введите строку 2: ")
def Mas(a: str, b: str)-> str:
    if len(a) >= len(b):
        n = b + a + b
    else:
        n = a + b + a
    return n

print(Mas(a, b))