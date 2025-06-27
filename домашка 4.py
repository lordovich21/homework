a = int(input("начало = "))
b = int(input("конец = "))
for i in range(a,b + 1):
    if i % 7 == 0:
        print(i)
else:
    pass

# a = int(input("начало = "))
# b = int(input("конец = "))
# for i in range(a, b + 1):
#     print("первое = ", i)
# for i in range(b, a, -1):
#     print("второе = ",i)
# for i in range(a, b + 1):
#     if i % 7 == 0:
#         print("третье = ",i)
# c = 0
# for i in range(a, b + 1):
#     if i % 5 == 0:
#         c = (i + 1)
# print("четвертое = ",(c // 5))

# a = int(input("начало = "))
# b = int(input("конец = "))
# for i in range(a, b + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizz Buzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 != 0 and i % 3 != 0:
#         print(i)
#     else:
#         print("ошибка")