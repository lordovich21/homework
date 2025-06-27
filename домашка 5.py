# a = int(input("начало = "))
# b = int(input("конец = "))
# c = 0
# d = 0
# f = 0
# for i in range(a,b + 1):
#     if i % 2 == 0:
#         c += i
#     if i % 2 != 0:
#         d += i
#     if i % 9 == 0:
#         f += i
# print("сумма четных = ", c)
# print("сумма нечетных = ", d)
# print("сумма кратных 9 = ", f)
# print(c / (i // 2))
# print(d//(i/2))
# print(f/(i/9))

# a = int(input("введите длину линии = "))
# for i in range(a):
#     for j in range(1):
#         print("%", end=" ")
#     print()

# a = int(input("введите число = "))
# while True:
#     if a == 7:
#         print("Good bye!")
#         break
#     elif a > 0:
#         print("Numberis positive")
#         a = int(input("введите число = "))
#     elif a < 0:
#         print("Numberis negative")
#         a = int(input("введите число = "))
#     elif a == 0:
#         print("Number is equal to zero")
#         a = int(input("введите число = "))
#     else:
#         break

a = int(input("первое число = "))
b = int(input("второе число = "))
c = int(input("третье число = "))
while True:
    if a == 7:
        print("Good bye!")
        exit()
    if b == 7:
        print("Good bye!")
        exit()
    if c == 7:
        print("Good bye!")
        exit()
    if a > b and a > c:
        print("наибольшее = ", a)
    elif b > a > c:
        print("наибольшее = ", b)
    else:
        print("наибольшее = ", c)
    if a < b and a < c:
        print("наименьшее = ", a)
    elif b < a < c:
        print("наименьшее = ", b)
    else:
        print("наименьшее = ", c)
    print("Сумма = ",a + b + c)
    a = int(input("первое число = "))
    b = int(input("второе число = "))
    c = int(input("третье число = "))