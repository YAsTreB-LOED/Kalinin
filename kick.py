def t(a):
    for i in range(1,a + 1):
        print(' ' * a, '*' * i, '*' * (i - 1), sep = '', end = '\n')
        a -= 1
t(70)


