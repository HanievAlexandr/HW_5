# Задание 5.1

# Користувач вводить рядок.Ваше завдання-перевірити,чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# - починатися з цифри
# - містити великі літери,
# - пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього
# підкреслення "_".
# - бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього
# підкреслення "_".
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо,
# або False - якщо ні.


# import string
# import keyword
# my_str = input("Enter, please a string: ")
# # Представим, что введеная пользователем строка корреткна
# value = True
# # проверяем, что бы имя переменной не начиналось с цифры или не относилось к keyword
# if my_str[0].isdigit() or my_str in keyword.kwlist:
#     value = False
# # проверяем, что б имя переменной не содержало спецсимволов, включая пробел(кроме '_')
# # в string.punctuation заменяю '_' на ' '
# # также проверяем на наличие заглавных букв
# for p in my_str:
#     if p in string.punctuation.replace('_', ' '):
#         value = False
#     if p.isupper():
#         value = False
# # также проверяем, чтобы символ '_' встречался в имени не больше одного раза
# if my_str.count('_') > 1:
#     value = False
# print(value)

########################################################################

# Задание 5.2
# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього
# хоче. Тобто, потрібно робити запит до користувача на продовження роботи калькулятора
# після кожного обчислення - якщо користувач ввів yes (можна просто y),
# то нове обчислення, інакше - закінчення роботи.

# print("Welcome to сalculator ")
# while True:
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))
#     operation = int(input("Choose the operation \n1 == addition\n2 == subtraction\n3 == multiplication\n4 == division\n"
#                           "5 == pow\n6 == div\n7 == mod\n"))
#     if operation == 1:
#         r = number1 + number2
#     elif operation == 2:
#         r = number1 - number2
#     elif operation == 3:
#         r = number1 * number2
#     elif operation == 4:
#         if number2 != 0:
#             r = number1 / number2
#         else:
#             r = ("Attention, Division by zero!")
#     elif operation == 5:
#         r = number1 ** number2
#     elif operation == 6:
#         if number2 != 0:
#             r = number1 // number2
#         else:
#             r = ("Attention, Division by zero!")
#     elif operation == 7:
#         if number2 != 0:
#             r = number1 % number2
#         else:
#             r = ("Attention, Division by zero!")
#     print("Answer:", r)
#     user_choice = input("Press 'y' for continue\n")
#     if user_choice == "y":
#         continue
#     else:
#         break
# print("GoodBye")

# Задание 5.3 hashtag
#Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# - ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# - підсумкова довжина hashtag має бути не більше 140 символів.
# - кожне слово починається з великої літери.
# - якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок
# до 140 символів.

# import string
#
# print("Hello!")
# text = input("Enter, please a string: ")
# # обрезаем длину хештега, если она будет больше 140 символов
# str1 = text[:141]
# # переводим первую букву каждого слова в верхний регистр
# str2 = str1.title()
# # убираем в хештеге пробелы
# str3 = str2.replace(' ', '')
# # проверяем, что бы в хештеге не было спецсимволов из списка 'sytrin.punctuatiopn'
# for p in string.punctuation:
#     if p in str3:
#         str3 = str3.replace(p, '')
# print(f'#{str3}')






