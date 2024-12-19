m = [10, 40, 20, 60, 10, 50, 30, 40]
def Mas(M: list[int])-> list[int]:
    n = ()
    massa1 = 0
    massa2 = 0
    if len(M) > 0:
        for i in range(0, len(M)):
            if i % 2 == 0:
                massa1 += m[i]
            else:
                massa2 += m[i]
    n = (massa1, massa2)
    return n

print(Mas(m))