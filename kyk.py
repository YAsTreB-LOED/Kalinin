# arr =  [[1, 3, -1, 4], 
#         [5, -2, 7, 5],
#         [-6, 3, 4, 1],
#         [9, 4, 6, 7]]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         arr[i][j] = arr[i][j] ** 2
# print(arr)


# arr =  [[1, 3, -1], 
#         [5, -2, 7],
#         [-6, 3, 4],
#         [9, 4, 6]]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] < 5:
#             arr[i][j] = 111
# print(arr)


# arr =  [[1, 3, -1, 4], 
#         [5, -2, 7, 5],
#         [-6, 3, 4, 1],
#         [9, 4, 6, 7]]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] < 0:
#             print(i, '|', j, end = '|')


# arr =  [[1, 3, -1, 4], 
#         [5, -2, 7, 5],
#         [-6, 3, 4, 1],
#         [9, 4, 6, 7]]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if i % 2 != 0 and j % 2 != 0:
#             print(arr[i][j], end = '|')


# arr =  [[1, 3, -1, 4], 
#         [5, -2, 7, 5],
#         [-6, 3, 4, 1],
#         [9, 4, 6, 7]]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] % 5 == 0:
#             print(arr[i][j], 'index = ', i, '|', j, end = '|  ')






# def text(r, s):
#     count = 0
#     for i in range(len(r)):
#         if s == r[i]:
#             count += 1
#     return count
# r1 = text(input(), input())
# print(r1)



# def text(r, s):
#     count = 0
#     for i in range(len(r)):
#         if s == r[i]:
#             count += 1
#     return count
# r1 = text(input(), input())
# print(r1)



# def text(r1, r2, r3):
#     storage = 0
#     if r1 > r2 > r3 or r3 > r2 > r1:
#         storage = r2
#     elif r2 > r1 > r3 or r3 > r1 > r2:
#         storage = r1
#     elif r1 > r3 > r2 or r2 > r3 > r1:
#         storage = r3
#     return storage
# r = text(int(input()), int(input()), int(input()))
# print(r)










# def pupupu():
#     for i in range(1,4):
#         print('*' * i)
#     print('*', '**', '***', sep = '\n')
# pupupu()

