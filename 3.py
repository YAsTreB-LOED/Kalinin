m = [0, 4, 2, 6, 9]
def Mas(M: list[int])-> list[int]:
    n = M
    if len(M) > 0:
        for i in range(1, len(M)+1):
            n[i - 1] = (n[i - 1] + i) % 10
    return n

print(Mas(m))
