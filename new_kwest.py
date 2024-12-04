# m = [0, 2, -2, 10, 4]

# def number_of_letters(h: list, n: int)-> int:
#     """Что-то делает"""
#     if type(h) == type([0, 1]) and type(n) == type(0):
#         storage = []
#         for i in range(len(h)):
#             storage.append(h[i] * n)
#         return storage

# storage = number_of_letters(m, int(input()))

# print(storage)





# m = [0, 2, -2, 10, 4]

# def number_of_letters(h: list, n: int)-> int:
#     """Что-то делает"""
#     if type(h) == type([0, 1]) and type(n) == type(0):
#         storage = []
#         count = 0
#         T_F = 0
#         for i in range(len(h)):
#             if h[i] % n == 0:
#                 count += 1
#                 if count - 1 == n:
#                     T_F = True
#             else:
#                 T_F = False
#                 break
#         return T_F

# T_F = number_of_letters(m, int(input()))

# print(T_F)





# m = [0, 2, -2, 10, 4]

# def number_of_letters(h: list)-> int:
#     """Что-то делает"""
#     if type(h) == type([0, 1]):
#         storage = []
#         count = 0
#         for i in range(len(h)):
#             if h[i] % 10 == 0 and h[i] != 0:
#                 storage.append(i)
#         return storage

# storage = number_of_letters(m)

# print(storage)
