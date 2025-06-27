# x = int(input("первое число = "))
# y = int(input("второе число = "))
# print(x ** y)

# f = 0
# for i in range(100,999):
#     a = i // 100
#     b = i % 100 // 10
#     c = i % 10
#     if a == b or a == c or b == c:
#         f += 1
# print(f + 10)# в 111, 222, 333 и тд тоже есть две одинаковые цифры, поэтому + 10

# f = 0
# for i in range(100,9999):
#     a = i % 1000 // 100
#     b = i % 100 // 10
#     c = i % 10
#     d = i // 1000
#     if a != b and a != c and b != c and a != d and b != d and c != d:
#         f += 1
# print(f)

b = int(input('Число =  '))
a = 0
i = 0
while b > 0:
    f = b % 10
    if f != 3 and f != 6:
        a = a + f * 10 ** i
        i = i + 1
    b = b // 10
print(a)