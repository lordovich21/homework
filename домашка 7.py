# text = input("Введите текст: ").lower().replace(" ", "")
# if text == text[::-1]:
#     print("Палиндром")
# else:
#     print("Не палиндром")

# text = input("Введите текст: ")
# special_words = input("Введите зарезервированные слова через пробел: ")
# special_words = special_words.split()
# list_of_words = text.split()
# print(list_of_words)
# print(special_words)
# new_text = ""
# for word in list_of_words:
#     if word.lower() in special_words:
#         new_text += word.upper()
#     else:
#         new_text += word
# print(new_text)

text = str(input("введите текст = "))
a = (len(text.split('.'))-1)
b = (len(text.split('!'))-1)
c = (len(text.split('?'))-1)
print(a+b+c)