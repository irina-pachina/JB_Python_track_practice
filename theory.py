#  input().split()

# LIST COMPREHENSION

# numbers = [1, 2, 3] # [int(n) for n in input()]
# sum_numbers = [sum(numbers[:i + 1]) for i in range(len(numbers))]
# print(sum_numbers)

# long_cities = [city for country in country_list for city in country if len(city) >= 6]

# students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]
# best_students = [i[0] for i in students if i[1] == "A" ]
# print(best_students)

# numbers = [1, 2, 3] # [int(n) for n in input()]
# average = [(numbers[i] + numbers[i+1]) / 2 for i in range(len(numbers)-1)]
# print(average)

# text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
#         ["Ephemeral", "lasts", "one", "day", "only"],
#         ["Accolade", "is", "an", "expression", "of", "praise"]]
# number = 1
# new_list = [word for sentence in text for word in sentence if len(word) == number]
# print(new_list)

# n = 3  # int(input())
# matches = [input() for _x in range(n)]
# print(matches)
# won_match = [x.split()[0] for x in matches if x.endswith("win")]
# print(won_match)
# print(len(won_match))

# ========================================

# print("Enter cells:")
# cells = "XOOOXOXXO" # "XOXXOOXOX"  # input()
#
# print("---------")
# print("|", cells[0], cells[1], cells[2],"|")
# print("|", cells[3], cells[4], cells[5],"|")
# print("|", cells[6], cells[7], cells[8],"|")
# print("---------")
#
# matrix = [[x for x in cells[0:3]], [x for x in cells[3:6]], [x for x in cells[6:9]]]
# print(matrix)
#
# counter = 0
# answer = ""
# for i in range(3):
#     if matrix[i][0] == matrix[i][1] == matrix[i][2]:
#         answer = matrix[i][0] + " wins"
#         counter += 1
# for i in range(3):
#     if matrix[0][i] == matrix[1][i] == matrix[2][i]:
#         answer = matrix[0][i] + " wins"
#         counter += 1
# if matrix[1][1] == matrix[2][2] == matrix[0][0]:
#     answer = matrix[1][1] + " wins"
#     counter += 1
# if matrix[1][1] == matrix[0][2] == matrix[2][0]:
#     answer = matrix[1][1] + " wins"
#     counter += 1
#
# if abs(cells.count("X") - cells.count("O")) > 1 or counter > 1:
#     answer = "Impossible"
#     print(answer)
# else:
#     print(answer)
#
# if answer == "" and "_" not in cells:
#     print("Draw")
# else:
#     print("Game not finished")

# ========================================
# string = 'That is \n mine'
# print(len(repr(string)))
# print(len(string))

# LEGB rule = Locals, Enclosing(вложенные функции from in to out), Globals, Built-in
# x = "global"
# def outer():
#     x = "outer local"
#     def inner():
#         x = "inner local"
#         def func():
#             x = "func local"
#             print(x)
#         func()
#     inner()
# outer()  # "func local"

# ==========================

# user_city = "Istanbul"
#
# def change_city(new_user_city):
#     global user_city
#     user_city = new_user_city
#
# change_city("Paris")
# print(user_city)

# =====================

# message = "bonjour and welcome to Paris!"
#
# print(message.upper())  # BONJOUR AND WELCOME TO PARIS!
#
# title_message = message.title()
# # `title_message` contains a new string with all words capitalized
# print(title_message)  # Bonjour And Welcome To Paris!
#
# print(message.replace("Paris", "Lyon"))  # bonjour and welcome to Lyon!
# replaced_message = message.replace("o", "!", 2)
# print(replaced_message)  # b!nj!ur and welcome to Paris!
#
# # the source string is unchanged, only its copy is modified
# print(message)  # bonjour and welcome to Paris!

# whitespace_string = "     hey      "
# normal_string = "incomprehensibilities"
#
# # delete spaces from the left side
# whitespace_string.lstrip()  # "hey      "
#
# # delete all "i" and "s" from the left side
# normal_string.lstrip("is")  # "ncomprehensibilities"
#
# # delete spaces from the right side
# whitespace_string.rstrip()  # "     hey"
#
# # delete all "i" and "s" from the right side
# normal_string.rstrip("is")  # "incomprehensibilitie"
#
# # no spaces from both sides
# whitespace_string.strip()  # "hey"
#
# # delete all trailing "i" and "s" from both sides
# normal_string.strip("is")  # "ncomprehensibilitie"

# =====================

# original = input()
# for symbol in ',.!?':
#     original = original.replace(symbol, '')
# print(original.lower())

# =====================

# definition = input()  # 'Coin of the realm is the legal money of the country'
# definition.split()
# # ['Coin', 'of', 'the', 'realm', 'is', 'the', 'legal', 'money', 'of', 'the', 'country']
# definition.split("legal")
# # ['Coin of the realm is the ', ' money of the country']
# definition.split("of", 1)  # resulting list will be equal to maxsplit + 1
# # ['Coin ', ' the realm is the legal money of the country']
# definition.split("of")
# # ['Coin ', ' the realm is the legal money ', ' the country']
# definition.split("hi!")  # wrong separator = list with one element
# # ['Coin of the realm is the legal money of the country']

# " ".join(word_list)  # "dog cat rabbit parrot"
# "".join(word_list)  # "dogcatrabbitparrot"

# long_text = 'first line\nsecond line\rthird line\r\nfourth line'
# long_text.splitlines()
# # ['first line', 'second line', 'third line', 'fourth line']
# long_text.splitlines(keepends=True)
# # ['first line\n', 'second line\r', 'third line\r\n', 'fourth line']
#
# # chaining example
# sent = input()  # "Mary had a little lamb"
# new_sent = sent.lower().split()
# # ["mary", "had", "a", "little", "lamb"]

# =====================

# string = "2020-04-30"
# print(string.replace("-", "\n"))
# list = string.split("-")
# print('\n'.join(list))
#
# # =====================
#
# list = input().split()
# new_list = [x for x in list if x.endswith("s")]  # x[-1] == 's'
# print("_".join(new_list))

# =====================

# n = 3
# for i in range(1,n + 1):
#     number_spaces = int(((n * 2 - 1) - (i * 2 - 1)) / 2)
#     spaces = " " * number_spaces
#     number_hash = int(i * 2 - 1)
#     center = "#" * number_hash
#     print(spaces + center + spaces)
# # for i in range(n):
# #     print((" " * (n - (i + 1))) + ("#" * (2 * i + 1)))

# =====================

# lst = "5 8 8 2 7 3 2 2 4"
# lst = lst.split()
# n = 8
# positions = [str(i) for i in range(len(lst)) if int(lst[i]) == n]
# if positions:
#     print(" ".join(positions))
# else:
#     print("not found")

# =====================

# text = "WWW.GOOGLE.COM uses 100-percent renewable energy sources and www.ecosia.com plants a tree for every 45 searches!"
# words = text.split()
# for word in words:
#     if word.lower().startswith(("https://", "www.", "http://")):
#         print(word)

# =====================

# sequence = "1 22 3"
# lst = sequence.split()
# lst.reverse()
# print(" ".join(lst))

# =====================

# lst = input().split()
# lst.reverse()
# print(" ".join(lst))

# =====================

# words = input().title().split()
# words[0] = words[0].lower()
# print("".join(words))

# =====================

# pets = ['dog', 'cat', 'parrot']
# for pet in pets:
#     print(pet)
# else:
#     print('We need a turtle!')

# =====================

# pancakes = 2
# while pancakes > 0:
#     print("I'm the happiest human being in the world!")
#     pancakes -= 1
#     if pancakes == 0:
#         print("Now I have no pancakes!")
#         break
# else:
#     print("No pancakes...")
# # loop 'else' runs only if the loop is exited normally (without hitting break)
# # 'else' will be chosen if condition in while id false

# =====================

# lst = []
# x = 0
# while 1:
#     x = input()
#     if x == ".":
#         break
#     lst.append(int(x))
#
# print(sum(lst) / len(lst))

# =====================

# lst = []
# x = 0
# while 1:
#     x = input()
#     if x == ".":
#         break
#     lst.append(float(x))
#
# print(min(lst))

# =====================

# string = "noon"
# rev = reversed(string)
# if string == "".join(rev):
#     print("Palindrome")
# else:
#     print("Not palindrome")

# =====================

# string = "normal phrase"
# vowels = "aeiou"
# for x in string:
#     if x in vowels:
#         print("vowel")
#     elif x.isalpha():
#         print("consonant")
#     else:
#         break

# =====================

# lst = []
# x = 0
# while 1:
#     lst = input().split()
#     if lst[0] == "MEOW":
#         break
#     if int(lst[1]) > x:
#         x = int(lst[1])
#         name = lst[0]
#
# print(name)

# =====================

# lst = []
# while 1:
#     x = int(input())
#     lst.append(x)
#     if sum(lst) == 0:
#         break
# squares = [x ** 2 for x in lst]
#
# print(sum(squares))

# =====================

# scores = "C C C I C C C C I I C C C C C C C C C".split()
# lives = 3
# wins = 0
# for x in scores:
#     if x == "C":
#         wins += 1
#     else:
#         lives -= 1
#         if lives == 0:
#             break
#
# print('You won' if lives > 0 else 'Game over')
# print(wins)

# =====================

# def prime(number):
#     for i in range(2, number):
#         if (n % i) == 0:
#             answer = False
#             break
#         else:
#             answer = True
#     return answer
#
#
# n = int(input())
#
# if n > 1 and prime(n):
#     print("This number is prime")
# else:
#     print("This number is not prime")

# =====================

# your_results = [1, 0, 0]
# print(any(your_results))  # True
#
# jam_results = []
# print(any(jam_results))  # False
# print(all(jam_results))  # True
# print(bool(jam_results))  # False
#
# your_results = [True, True, True]
# print(all(your_results))  # True

# =====================

# box = [10, 20, 33]
# if any([candy % 2 for candy in box]):
#     print("It is not a proper gift.")
# else:
#     print("Perfect!")

# =====================

# prime_numbers = [n for n in range(2, 1001) if all(n % i != 0 for i in range(2, n - 1))]
# print(prime_numbers)

# =====================

# tickets = [11, 22, 33, 44, 55]
# winning_tickets = [i >= 44 for i in tickets]
# tickets_bool = any(winning_tickets)

# =====================

# print('%.3f' % (11/3))  # 3.667
# print('%.2f' % (11/3))  # 3.67
#
# print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
# print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
# print('The {film} at {theatre} was {adjective}!'.format(film='Lord of the Rings',
#                                                         adjective='incredible',
#                                                         theatre='BFI IMAX'))
#
# hundred_percent_number = 1823
# needed_percent = 16
# needed_percent_number = hundred_percent_number * needed_percent / 100
# print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
# # 16% from 1823 is 291.68
# print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
# # Rounding 291.68 to 1 decimal place is 291.7
#
# float_number = float(input())
# decimal_count = int(input())
# print(f'%.{decimal_count}f' % float_number)
#
#
# income = int(input())
# if income in [0, 15527]:
#     percent = 0
#     calculated_tax = income
# elif income in [15528, 42707]:
#     percent = 15
#     calculated_tax = int(income * percent / 100)
# elif income in [42708, 132406]:
#     percent = 25
#     calculated_tax = int(income * percent / 100)
# else:
#     percent = 28
#     calculated_tax = int(income * percent / 100)
# print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")

# =====================

# print("apple" in "pineapple")  # True
# print("milk" not in "yogurt")  # True
# # empty string is considered to be a substring of any string
# print('' not in "lemon")  # False
#
# email = "my_email_address@something.com"
# print(email.startswith("www."))          # False
# print(email.endswith("@something.com"))  # True
# print(email.startswith("email", 2))  # False
# print(email.startswith("email", 3))  # True
# # substring does include the character with the start index but does not include the element with the end index
# print(email.endswith("@", 5, 8))  # False
# print(email.endswith("@", 5, 9))  # True
#
# best = "friend"
# print(best.find("i"))   # 2
# print(best.find("end"))  # 3 (index of the first character of the substring is returned)
# print(best.find("u"))   # -1
# print(best.index("u"))  # ValueError
#
# magic = "abracadabra"
# # search backward from the end of the string
# print(magic.rfind("ra"))  # 9
# print(magic.rindex("a"))  # 10
#
# print(magic.count("abra"))  # 2
# print(magic.count("a"))     # 5

# =====================

# instructions = " make a wish Simon says"
# def what_to_do(instructions):
#     if instructions.startswith("Simon says") or instructions.endswith("Simon says"):
#         action = instructions.replace("Simon says", "").strip()
#         print(f"I {action}")
#     else:
#         print("I won't do it!")
#
# what_to_do(instructions)

# =====================

# email = "good.email@example.com"
# def check_email(string):
#     at_position = string.find("@")
#     if string.count(" ") > 0:
#         return False
#     elif "@" not in string:
#         return False
#     elif string[at_position + 1] == ".":
#         return False
#     elif string.count(".", at_position) == 0:
#         return False
#     else:
#         return True
#
#
# print(check_email(email))

# =====================

# import random
#
# n = int(input())
#
# random.seed(n)
# print(random.randint(-100, 100))

# =====================

# abs_integer = abs(-10)  # 10
# abs_float = abs(-10.0)  # 10.0
#
# round_integer = round(10.0)      # 10, returns integer when ndigits is omitted
# round_float = round(10.2573, 2)  # 10.26
#
# pow_integer = pow(2, 10)  # 1024
# pow_float = pow(2.0, 10)  # 1024.0
#
# largest = max(1, 2, 3, 4, 5)   # 5
# smallest = min(1, 2, 3, 4, 5)  # 1
#
# import math
#
# # math.fabs() and math.pow() always return floats
#
# fabs_integer = math.fabs(-10)  # 10.0
# fabs_float = math.fabs(-10.0)  # 10.0
#
# pow_integer = math.pow(2, 10)  # 1024.0
# pow_float = math.pow(2.0, 10)  # 1024.0
#
# result = math.sqrt(100)  # 10.0
#
# # math.floor(a) returns the nearest integer less than or equal to a;
# # math.ceil(a) returns the nearest integer greater than or equal to a
#
# r = 3.5
# circumference = 2 * math.pi * r  # длина окружности

# =====================

# import math
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# p = (a + b + c) / 2
# s = math.sqrt((p * (p - a) * (p - b) * (p - c)))

# =====================

# import math
#
# a = int(input())
# b = int(input())
#
# if b <= 1:
#     print(round(math.log(a), 2))
# else:
#     print(round(math.log(a, b), 2))

# =====================
# # скрипт .py, чтобы запускать из командной строки с аргументами
# import sys  # first, we import the module
#
# args = sys.argv  # we get the list of arguments
#
# if len(args) != 3:
#     print("The script should be called with two arguments, the first and the second number to be multiplied")
# else:
#     first_num = float(args[1])
#     second_num = float(args[2])
#
#     product = first_num * second_num
#
#     print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))

# =====================

# args = ["first", "2", "3", "4","5"]
# int_args =[int(i) for i in args[1:]]
# print(int_args)

# =====================

# # parser.add_argument("-i1", "--ingredient_1")  # optional(- or --) argument
# #                                               # or
# # parser.add_argument("ingredient_1")           # positional argument
#
# import argparse
#
# parser = argparse.ArgumentParser(description="This program prints recipes \
# consisting of the ingredients you provide.")
#
# parser.add_argument("-i1", "--ingredient_1", choices=["pasta", "rice", "potato",
#                     "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
#                     help="You need to choose only one ingredient from the list.")
# parser.add_argument("-i2", "--ingredient_2", choices=["pasta", "rice", "potato",
#                     "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
#                     help="You need to choose only one ingredient from the list.")
# parser.add_argument("-i3", "--ingredient_3", choices=["pasta", "rice", "potato",
#                     "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
#                     help="You need to choose only one ingredient from the list.")
# parser.add_argument("-i4", "--ingredient_4", choices=["pasta", "rice", "potato",
#                     "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
#                     help="You need to choose only one ingredient from the list.")
# parser.add_argument("-i5", "--ingredient_5", choices=["pasta", "rice", "potato",
#                     "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
#                     help="You need to choose only one ingredient from the list.")
#
# # optional parameter, является флагом, этот action показывает, что если указать "соль", то salt = True
# parser.add_argument("--salt", action="store_true",
#                     help="Specify if you'd like to use salt in your recipe.")
# # а перец флагом не будет, нужно указывать значение --pepper True, чтобы изменить
# parser.add_argument("--pepper", default="False",
#                     help="Change to 'True' if you'd like to use pepper in your recipe.")
#
# args = parser.parse_args()
#
# ingredients = [args.ingredient_1, args.ingredient_2, args.ingredient_3,
#                args.ingredient_4, args.ingredient_5]
# if args.salt:
#     ingredients.append("salt")
# if args.pepper == "True":
#     ingredients.append("pepper")
#
# print(f"The ingredients you provided are: {ingredients}")
#
#
# def find_a_recipe(ingredients):
#     ...
#     # processes the input and returns a recipe depending on the provided ingredients
#
# # Вызов из CLI:
# # python recipe_book.py -i1 rice -i2 onion -i3 garlic -i4 carrot -i5 tomato_sauce --salt
# # The ingredients you provided are: ['rice', 'onion', 'garlic', 'carrot', 'tomato_sauce', 'salt']
# # <The description of the available recipe>

# =====================

# # пустые кортежи
# empty_tuple1 = ()
# empty_tuple2 = tuple()
#
# single_tuple = ('cat',)
#
# double_tuple = 'Saturday', 'Sunday'
#
# # a list turned into a tuple
# bakers_dozen = tuple([12, 1])
# print(bakers_dozen == (12, 1))  # True
#
# # a tuple from a string
# sound = tuple('meow')
# print(sound)  # ('m', 'e', 'o', 'w')

# =====================

# capitals = ['Philadelphia', 'Rio de Janeiro', 'Saint Petersburg']
#
# capitals[0] = 'Washington, D.C.'
# capitals[1] = 'Brasília'
# capitals[2] = 'Moscow'
# print(capitals)  # ['Washington, D.C.', 'Brasília', 'Moscow']
#
# # Tuples don't support item assignment
# former_capitals = tuple(capitals)
# # former_capitals[0] = 'Washington, D.C.'  # TypeError

# =====================

# # create an empty list
# dragons = []
#
# # add element by one
# dragons.append('Rudror')
#
# # "extend" adds all the elements from another iterable to the end of a list
# numbers = [1, 2, 3, 4, 5]
# numbers.extend([10, 20, 30])
# print(numbers)  # [1, 2, 3, 4, 5, 10, 20, 30]
#
# # "append" adds another iterable as 1 element
# numbers = [1, 2, 3, 4, 5]
# numbers.append([10, 20, 30])
# print(numbers)  # [1, 2, 3, 4, 5, [10, 20, 30]]
#
# # merge two lists
# numbers_to_four = [0, 1, 2, 3, 4]
# numbers_from_five = [5, 6, 7, 8, 9]
# numbers = numbers_to_four + numbers_from_five
# print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # create pattern
# one = [1]
# ones = one * 7
# print(ones)  # [1, 1, 1, 1, 1, 1, 1]
#
# # delete element
# dragons.remove('Rudror')  # only the first instance of that element is removed
# del numbers[1]  # [0, 2, 3, 4, 5, 6, 7, 8, 9]
# # "pop" w/o arguments removes and returns the last element in the list
# dragons = ['Rudror', 'Targiss', 'Coporth']
# last_dragon = dragons.pop()
# print(last_dragon)  # 'Coporth'
# print(dragons)      # ['Rudror', 'Targiss']
# # with argument - index
# first_dragon = dragons.pop(0)
# print(first_dragon)  # 'Rudror'
# print(dragons)       # ['Targiss']
#
# # list.insert(position, element)
# # position - index of the element before which the new element is going to be inserted
# years = [2016, 2018, 2019]
# years.insert(1, 2017)           # [2016, 2017, 2018, 2019]
# years.insert(0, 2015)           # [2015, 2016, 2017, 2018, 2019]
# years.insert(len(years), 2020)  # [2015, 2016, 2017, 2018, 2019, 2020]
#
# # Membership testing
# catalog = ['yogurt', 'apples', 'oranges', 'bananas', 'milk', 'cheese']
# print('bananas' in catalog)  # True
# print('lemon' in catalog)  # False
# print('lemon' not in catalog)  # True
#
# # info about elements
# grades = [10, 5, 7, 9, 5, 10, 9]
# print(grades.count(5))  # 2
# print(grades.index(7))   # 2

# =====================

# import random
# # random number from 0 to 1:
# print(random.random())  # 0.5557276751294531
#
# # random.seed(x) - w/o argument it is current system time
# random.seed()
#
# # random.uniform(a, b) – float number in the range between a and b:
# print(random.uniform(3, 100))  # 35.94079523197162
# # same but integer
# print(random.randint(35, 53))  # 52
# # element from non-empty sequences
# print(random.choice('Voldemort'))  # m
# # from a range between a and b with a step c
# print(random.randrange(3, 100, 5))  # 18
# print(random.randrange(1, 5))       # 2
# print(random.randrange(100))        # 44
# # random.shuffle(seq, [random]) – shuffles a sequence, doesn't work with immutable datatypes
# tiny_list = ['a', 'apple', 'b', 'banana', 'c', 'cat']
# random.shuffle(tiny_list)
# print(tiny_list)  # ['apple', 'banana', 'a', 'cat', 'b', 'c']
# # random.sample(population, k) - k length list from a population sequence
# print(random.sample(range(100), 3))  # [24, 33, 91]

# =====================

# #sets
# empty_set = set()
# print(type(empty_set))   # <class 'set'>
#
# empty_dict = {}
# print(type(empty_dict))  # <class 'dict'>
#
# flowers = {'rose', 'lilac', 'daisy'}
# # the order is not preserved
# print(flowers)  # {'daisy', 'lilac', 'rose'}
#
# letters = set('philharmonic')
# print(letters)  # {'h', 'r', 'i', 'c', 'o', 'l', 'a', 'p', 'm', 'n'}
#
# # double letters are counted as one element - helps to avoid repetitions
# states = ['Russia', 'USA', 'USA', 'Germany', 'Italy']
# print(len(states))  # the length equals 4
# print(set(states))  # {'Russia', 'USA', 'Italy', 'Germany'}
#
# # Membership testing
# nums = {1, 2, 2, 3}
# print(1 in nums, 4 not in nums)  # True True
#
# # add
# nums = {1, 2, 2, 3}
# nums.add(5)
# print(nums)  # {1, 2, 3, 5}
#
# # update
# another_nums = {6, 7}
# nums.update(another_nums)
# print(nums)  # {1, 2, 3, 5, 6, 7}
#
# # we can also add a list
# text = ['how', 'are', 'you']
# nums.update(text)
# print(nums)  # {'you', 1, 2, 3, 5, 6, 7, 'are', 'how'}
#
# # or a string
# word = 'hello'
# nums.add(word)
# print(nums)  # {1, 2, 3, 'how', 5, 6, 7, 'hello', 'you', 'are'}
#
# # delete
# nums.remove(2)
# print(nums)  # {1, 3, 5}
# nums.discard(3)
# print(nums)  # {1, 5}
# # different behaviour with absent element
# empty_set = set()
# empty_set.discard(2)  # nothing happened
# empty_set.remove(2)   # KeyError: 2
# # delete all elements
# nums.clear()
#
# # Frozenset - set is a mutable data type, but frozenset is not
# empty_frozenset = frozenset()
# frozenset_from_set = frozenset({1, 2, 3})
# print(frozenset_from_set)  # frozenset({1, 2, 3})
#
# text = {'hello', 'world'}
# nested_text = {'!'}
# nested_text.add(text)  # TypeError: unhashable type: 'set'
# some_frozenset = frozenset(text)
# nested_text.add(some_frozenset)
# print(nested_text)  # {'!', frozenset({'world', 'hello'})}

# =====================

# # set operator requires both arguments to be sets, while the method only demands this from the first one
# # UNION
# democrats = {'Kennedy', 'Obama'}
# republicans = {'Trump', 'Lincoln'}
# presidents = democrats.union(republicans)
# # or
# also_presidents = democrats | republicans
# print(presidents == also_presidents)  # True
#
#
# ghostbusters = {'Peter', 'Raymond', 'Egon'}
# soldiers = {'Winston'}
# secretaries = {'Janine'}
# # add in the same set
# ghostbusters |= soldiers
# ghostbusters.update(secretaries)
# print(ghostbusters)  # {'Peter', 'Raymond', 'Egon', 'Winston', 'Janine'}
#
# # INTERSECTION
# light_side = {'Obi-Wan', 'Anakin'}
# dark_side = {'Palpatine', 'Anakin'}
# both_sides = light_side.intersection(dark_side)
# print(both_sides)  # {'Anakin'}
# # or
# print(light_side & dark_side)  # {'Anakin'}
#
# creatures = {'human', 'rabbit', 'cat'}
# pets = {'rabbit', 'cat'}
# creatures.intersection_update(pets)
# print(creatures)  # {'rabbit', 'cat'}
# # or
# beasts = {'crocodile', 'cat'}
# creatures &= beasts
# print(creatures)  # {'cat'}
#
# # DIFFERENCE
# painters = {'Klimt', 'Michelangelo', 'Picasso'}
# ninja_turtles = {'Michelangelo', 'Leonardo'}
# print(painters.difference(ninja_turtles))  # {'Klimt', 'Picasso'}
# # or
# print(painters - ninja_turtles)  # {'Klimt', 'Picasso'}
#
# criminals = {'Al Capone', 'Blackbeard', 'Bonnie and Clyde'}
# gangsters = {'Al Capone'}
# pirates = {'Blackbeard'}
# criminals.difference_update(gangsters)
# criminals -= pirates
# print(criminals)  # {'Bonnie and Clyde'}
#
# # sets are within a container
# languages = [{'c', 'c++', 'python'}, {'python', 'javascript'}, {'python', 'java'}]
# the_best = set.intersection(*languages)
# print(the_best)  # {'python'}

# =====================

# class River:
#     all_rivers = []
# # __init__ это конструктор, для того, чтобы у всех инстансов класса были одни и те же свойства
# # когда объявляется инстанс, обязательно присваивать значения этим свойствам, если есть конструктор
#     def __init__(self, name, length):
#         self.name = name
#         self.length = length
#         # add current river to the list of all rivers
#         River.all_rivers.append(self)
#
# # self - это инстанс класса(объект), он передается в метод первым параметром
#     def get_info(self):
#         print("The length of the {0} is {1} km".format(self.name, self.length))
#
#
# volga = River("Volga", 3530)
# seine = River("Seine", 776)
# nile = River("Nile", 6852)
#
# for river in River.all_rivers:
#     print(river.name)

# =====================


# class Ship:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#         self.cargo = 0
#
#     def sail(self, destination):
#         print(f"The {self.name} has sailed for {destination}!")
#
#
# black_pearl = Ship("Black Pearl", 800)
# destination = input()
# black_pearl.sail(destination)

# =====================

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def dist(self, point2):
#         d = ((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2) ** 0.5
#         return d
#
#
# p1 = Point(1.5, 1)
# p2 = Point(1.5, 2)
#
# print(p1.dist(p2))  # 1.0

# =====================

# class PiggyBank:
#     def __init__(self, dollars, cents):
#         self.dollars = dollars
#         self.cents = cents
#
#     def add_money(self, deposit_dollars, deposit_cents):
#         self.dollars += deposit_dollars
#         self.cents += deposit_cents
#         if self.cents > 99:
#             add_doll = self.cents // 100
#             self.dollars += add_doll
#             self.cents -= add_doll * 100
#
#
# my_savings = PiggyBank(1, 1)
# my_savings.add_money(0, 99)
# print(my_savings.dollars, my_savings.cents)

# =====================

# class Patient:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#
#     def __repr__(self):
#         return "Object of the class Patient. name: {}, last_name: {}, age: {}".format(self.name, self.last_name,
#                                                                                       self.age)
#
#     def __str__(self):
#         return "{} {}. {}".format(self.name, self.last_name, self.age)

# =====================

# class Puppy:
#     n_puppies = 0  # number of created puppies
#
#     def __new__(cls):
#         if cls.n_puppies <= 9:
#             cls.n_puppies += 1
#             return object.__new__(cls)

# =====================

# class ComplexNumber:
#     def __init__(self, real_part, im_part):
#         self.real_part = real_part
#         self.im_part = im_part
#
#     def __add__(self, other):
#         """Addition of complex numbers."""
#         real = self.real_part + other.real_part
#         imaginary = self.im_part + other.im_part
#         return ComplexNumber(real, imaginary)
#
#     def __mul__(self, other):
#         """Multiplication of complex numbers."""
#         real = (self.real_part * other.real_part -
#                 self.im_part * other.im_part)
#         imaginary = (self.real_part * other.im_part +
#                      other.real_part * self.im_part)
#         return ComplexNumber(real, imaginary)
#
#     # __iadd__()
#     # __isub__()
#     # __imul__()
#     # __itruediv__()
#     # __ipow__()
#
#     def __iadd__(self, other):
#         """Addition with assignment (+=) (augmented assignment)."""
#         self.real_part += other.real_part
#         self.im_part += other.im_part
#         return self
#
#     # __eq__(): equality( ==)
#     # __ne__(): inequality( !=)
#     # __lt__(): less than( <)
#     # __gt__(): greater than( >)
#     # __le__(): less or equal( <=)
#     # __ge__(): greater or equal( >=)
#
#     def __eq__(self, other):
#         """Compare two complex numbers for equality (==)."""
#         return ((self.real_part == other.real_part) and
#                 (self.im_part == other.im_part))
#
#
# z1 = ComplexNumber(1, 1)
# z2 = ComplexNumber(-1, 2)
#
# z3 = z1 + z2
# print(z3.real_part, z3.im_part)  # 0 3
#
# z4 = z1 * z2
# print(z4.real_part, z4.im_part)  # -3 1
#
# z1 += z2
# print(z1.real_part, z1.im_part)

# =====================

# birds = {"pigeon": 12, "sparrow": 5, "red crossbill": 1}
# prices = {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
# empty_dict = {}
# another_empty_dict = dict()
#
# # note that the future dictionary keys are listed without quotes, and keys should look like variables, not integers/strings/etc
# prices_with_constr = dict({'espresso': 5.0}, americano=8.0, latte=10, pastry='various prices')
# print(prices_with_constr)  # {'espresso': 5.0, 'americano': 8.0, 'latte': 10, 'pastry': 'various prices'}
#
# # a nested dictionary example
# my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
#            'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}
#
# # another nested dictionary example
# # note that keys of the outer dictionary are numbers
# digits = {1: {'Word': 'one', 'Roman': 'I'},
#           2: {'Word': 'two', 'Roman': 'II'},
#           3: {'Word': 'three', 'Roman': 'III'},
#           4: {'Word': 'four', 'Roman': 'IV'},
#           5: {'Word': 'five', 'Roman': 'V'}}
#
# my_pet = {}
#
# # add 3 keys and their values into the dictionary
# my_pet['name'] = 'Dolly'
# my_pet['animal'] = 'dog'
# my_pet['breed'] = 'collie'
#
# print(my_pet)  # {'name': 'Dolly', 'animal': 'dog', 'breed': 'collie'}
#
# # get
# my_pets = {'dog': {'name': 'Dolly', 'breed': 'collie'},
#            'cat': {'name': 'Fluffy', 'breed': 'maine coon'}}
#
# print(my_pets['cat'])  # {'name': 'Fluffy', 'breed': 'maine coon'}
# print(my_pets['cat']['breed'])  # maine coon

# # 3rd method to create dict: dict.fromkeys(keys, value)
# planets = {'Venus', 'Earth', 'Jupiter'}
# # initializing by default with None
# planets_dict = dict.fromkeys(planets)
# print(planets_dict)  # {'Jupiter': None, 'Venus': None, 'Earth': None}
#
# # initializing with a value
# value = 'planet'
# planets_dict = dict.fromkeys(planets, value)
# print(planets_dict)  # {'Earth': 'planet', 'Venus': 'planet', 'Jupiter': 'planet'}
#
# # changing the value of 'Jupiter'
# planets_dict['Jupiter'] = "giant " + planets_dict['Jupiter']
# print(planets_dict)
# # {'Earth': 'planet', 'Venus': 'planet', 'Jupiter': 'giant planet'}
#
# satellites = ['Moon', 'Io','Europa']
# # initializing with an empty list
# planets_dict = dict.fromkeys(planets, [])
# print(planets_dict)  # {'Jupiter': [], 'Venus': [], 'Earth': []}
#
# planets_dict['Earth'].append(satellites[0])
# planets_dict['Jupiter'].append(satellites[1])
# planets_dict['Jupiter'].append(satellites[2])
# print(planets_dict)
# # {'Jupiter': ['Moon', 'Io', 'Europa'], 'Venus': ['Moon', 'Io', 'Europa'], 'Earth': ['Moon', 'Io', 'Europa']}
# # because the fromkeys method assigns the same object to all keys
#
# # adding items = update
# testable = {'September': '16°C', 'December': '-10°C'}
# another_dictionary = {'June': '21°C'}
#
# # adding items from another dictionary
# testable.update(another_dictionary)
# print(testable)  # {'September': '16°C', 'December': '-10°C', 'June': '21°C'}
#
# # adding a key-value pair
# testable.update(October='10°C')
# print(testable)
# # {'September': '16°C', 'December': '-10°C', 'June': '21°C', 'October': '10°C'}
#
# # update value in existing key
# testable = {'September': '16°C', 'December': '-10°C'}
# testable.update(December='-20°C')
# print(testable)  # {'September': '16°C', 'December': '-20°C'}
#
# # Get a value from the dictionary by a key
# print(testable['September'])  # 16°C
#
# # 'get' method does not throw an error when there's no such key
# print(testable.get('September'))  # 16°C
# print(testable.get('June'))  # None
# # define the default value when None
# print(testable.get('June', 'no temperature'))
#
# # Remove the key from the dictionary and return the value
# return_value = testable.pop('December')
# print(return_value)  # -10°C
# print(testable)  # {'September': '16°C'}
# # If the key was not found need to define default value to avoid KeyError
# return_value = testable.pop('July', 'no temperature')
# print(return_value)  #  no temperature
#
# # Remove and return the last item (key, value) added to the dictionary
# testable = {'September': '16°C', 'December': '-10°C'}
# return_value = testable.popitem()
# print(return_value)  # ('December', '-10°C')
# print(testable)  # {'September': '16°C'}
# # not working for empty dicts
# testable = {}
# return_value = testable.popitem()
# # KeyError: 'popitem(): dictionary is empty'
#
# # Delete (remove from a dictionary) a value by its key
# testable = {'September': '16°C', 'December': '-10°C', 'July': '23°C'}
# del testable['September']
# print(testable)  # {'December': '-10°C', 'July': '23°C'}
#
# # deletes the whole dictionary
# del testable
#
# # Remove all the items and return an empty dictionary
# testable = {'September': '16°C', 'December': '-10°C', 'July': '23°C'}
# testable.clear()
# print(testable)   # {}
#
# # Differences in removal methods
# testable = {'December': '-10°C', 'July': '23°C'}
# another_testable = testable
# testable = {}
# print(testable)  # {}
# print(another_testable)  # {'December': '-10°C', 'July': '23°C'}
#
# testable_2 = {'December': '-10°C', 'July': '23°C'}
# another_testable_2 = testable_2
# testable.clear()
# print(testable)  # {}
# print(another_testable)  # {}

# groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
# dict_kg = dict.fromkeys(groups)
# number = int(input())
# count = 0
# for key in dict_kg:
#     if count >= number:
#         break
#     dict_kg[key] = int(input())
#     count += 1
# print(dict_kg)

# groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
# dict_kg = dict.fromkeys(groups)
# number = int(input())
# for i in range(number):
#     dict_kg[groups[i]] = int(input())
# print(dict_kg)

# hand = ["Ace", "4", "9", "Jack", "10", "7"]
# # for _i in range(6):
# #     hand.append(input())
#
# dict_cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
# count = 0
# for n in hand:
#     if n in dict_cards:
#         print(dict_cards[n])
#         count += dict_cards[n]
# print(count / 6)

# or
# dict_cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
# ranks_hand = [dict_cards.get(input()) for i in range(6)]
# print(sum(ranks_hand) / 6)

# a_dict = [
#     {"day": "Monday", "distance": 2000},
#     {"day": "Tuesday", "distance": 3000},
#     {"day": "Wednesday", "distance": 3500},
#     {"day": "Thursday", "distance": 2500},
#     {"day": "Friday", "distance": 2500},
#     {"day": "Saturday", "distance": 1000},
#     {"day": "Sunday", "distance": 5600}]
# count = 0
# for item in a_dict:
#     count += item["distance"]
# print(int(count / len(a_dict)))

# double_alphabet = {}
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# for char in ascii_lowercase:
#     double_alphabet[char] = char * 2
# print(double_alphabet)

# =====================

# lambda x: 'even' if x % 2 == 0 else 'odd'
# # invoke
# (lambda x, y: (x + y) % 2)(1, 5)
# # or assign a function object to a variable
# # but not recommended by styleguides
# func = lambda x, y: (x + y) % 2
# func(1, 10)
#
# def create_function(n):
#     return lambda x: n * x
# doubler = create_function(2)
# tripler = create_function(3)
# doubler(2)  # 4
# tripler(2)  # 6

# =====================

# def locate(place, planet="Earth"):
#     print(place, "on", planet)
# locate("Berlin")                     # Berlin on Earth
# locate("Breakfast", planet="Pluto")  # Breakfast on Pluto
# locate("Craters", "Mercury")         # Craters on Mercury
#
# def add_player(player, team=None):
#     if team is None:
#         team = []
#     team.append(player)
#     return team

# def add_viewer(name, fan_list=None):
#     if fan_list is not None:
#         fan_list.append(name)
#         return fan_list
#     else:
#         non_fans = []
#         non_fans.append(name)
#         return non_fans
# print(add_viewer("Harry", ["Mark", "Joshua"]))
# print(add_viewer("Molly"))

# =====================

# # map(function, iterable)
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def doubler(x):
#     return 2*x
# doubled_numbers = map(doubler, numbers)
# print(list(doubled_numbers))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# # or
# doubled_numbers = map(lambda x: 2*x, numbers)
# print(list(doubled_numbers))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#
# # can be more than one iterable argument
# x_list = [1, 2, 3]
# y_list = [4, 5, 6]
# z_list = [7, 8, 9]
# s = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))
# print(s)  # [12, 15, 18]
#
# # filter(boolean_function, iterable)
# odd_numbers = filter(lambda x: x % 2, numbers)
# print(list(odd_numbers))  # [1, 3, 5, 7, 9]
#
# def my_product(list_1, list_2):
#     return list(map(lambda x, y: x * y, list_1, list_2))

# =====================

# # file
# my_file = open('my_file.txt')
# file_utf8 = open('my_file.txt', encoding='utf-8')
#
# print(my_file.read())
# # Dog
# # Cat
# # Rabbit
# # Sea turtle
# # Penguin
#
# # считываем по 3 байта пока не дойдем до конца строки
# print(my_file.readline(3))
# print(my_file.readline(3))
# print(my_file.readline(3))
# print(my_file.readline(3))
# print(my_file.readline(3))
# print(my_file.readline(3))
# # Dog
# #
# #
# # Cat
# #
# #
# # Rab
# # bit
#
# print(my_file.readlines())
# # ['Dog\n', 'Cat\n', 'Rabbit\n', 'Sea turtle\n', 'Penguin']
#
# for line in my_file:
#     print(line)
# # Dog
# #
# # Cat
# #
# # Rabbit
# #
# # Sea turtle
# #
# # Penguin
#
# my_file.close()

# =====================

# sums = open("sums.txt")
# for line in sums:
#     numbers = [int(x) for x in line.split()]
#     print(sum(numbers))
# sums.close()

# =====================

# names = ['Kate', 'Alexander', 'Oscar', 'Mary']
# # 'w' mode can create file if it isn't exist and overwrite if exists
# file = open('test_file.txt', 'w', encoding='utf-8')
# for name in names:
#     file.write(name + '\n')
# # or (the same result)
# names = ['Kate\n', 'Alexander\n', 'Oscar\n', 'Mary\n']
# file.writelines(names)
# file.close()
#
# # 'a' mode appends in the end of file
# name_file = open('names.txt', 'a', encoding='utf-8')
# name_file.write('Rachel\n')
# name_file.close()

# =====================

# # context manager
# n_files = 1000000
# files = []
# for i in range(n_files):
#     with open('test.txt') as f:
#         files.append(f)
# # with context manager don't need to close the file
#
# with open('tarantino.txt', 'r', encoding='utf-8') as in_file, \
#      open('tarantino_lowercase.txt', 'w', encoding='utf-8') as out_file:
#     for line in in_file:
#         out_file.write(line.lower())

# =====================
import json


# movie_dict = {
#   "movies": [
#     {
#       "title": "Inception",
#       "director": "Christopher Nolan",
#       "year": 2010
#     },
#     {
#       "title": "The Lord of the Rings: The Fellowship of the Ring",
#       "director": "Peter Jackson",
#       "year": 2001
#     },
#     {
#       "title": "Parasite",
#       "director": "Bong Joon Ho",
#       "year": 2019
#     }
#   ]
# }
# # json.dump() writes to a file-like object
# with open("movies.json", "w") as json_file:
#     json.dump(movie_dict, json_file)
# # json.dumps() creates a string
# json_str = json.dumps(movie_dict, indent=4)
#
# # Decoding JSON from a file
# with open("movies.json", "r") as json_file:
#     movie_dict_from_json = json.load(json_file)
# print(movie_dict_from_json == movie_dict)  # True
#
# # from string
# print(movie_dict == json.loads(json_str))  # True

# str_json = '{"users": [{"name": "John","last_name": "Doe","age": 33},{"name": "Juin","last_name": "D","age": 32}]}'
# dict_json = json.loads(str_json)
# print(dict_json)
# print(len(dict_json["users"]))

# =====================

#    a          b
# truthy AND truthy = b
# truthy AND falsy = b
# falsy AND truthy = a
# falsy AND falsy = a

# truthy OR truthy = a
# truthy OR falsy = a
# falsy OR truthy = b
# falsy OR falsy = b

#   a    not a
# truthy False
# falsy   True

# def print_list(lst):
#     print(lst or 'empty list')
# # If lst is empty, the lst[0] > 0 expression is invalid
# # but it does not cause an exception because it never gets evaluated
#     if lst and lst[0] > 0:
#         print(lst)
#
#
# print(bool(True), bool(False))    # True False
# print(bool(None))                 # False
# print(bool([]), bool([2, 3, 9]))  # False True

# =====================

# # def func(positional_args, defaults, *args):
# #     pass
#
# def will_survive(*names):
#     for name in names:
#         print("Will", name, "survive?")
#
#
# def recipe(*args, sep=" or "):
#     return sep.join(args)
# print(recipe("meat", "fish"))               # meat or fish
# print(recipe("meat", "fish", sep=" and "))  # meat and fish
#
# # * operator unpacks an iterable
# print(*"fun")        # f u n
# print(*[5, 10, 15])  # 5 10 15
#
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
# small_numbers = [1, 2, 3]
# large_numbers = [9999999, 1111111]
# print(add(*small_numbers))  # 6
# print(add(*large_numbers))  # 11111110

# =====================

# slicing
# sequence[start:stop:step]  # from start to stop-1, by step
# sequence[:end]    # element from the 1st element to end-1
# sequence[start:]  # elements from start to the last element
# sequence[:]       # the full copy of the sequence
# sequence[::step]  # every element with a given step

# # copy of sequence
# sheep = ['Dolly', 'Polly', 'Molly']
# cloned_sheep = sheep[:]  # ['Dolly', 'Polly', 'Molly']
#
# # When the step value is negative, the elements are returned in reverse order
# pets = ['dog', 'cat', 'parrot', 'gecko']
# print(pets[-2:])   # ['parrot', 'gecko']
# print(pets[:-2])   # ['dog', 'cat']
# print(pets[::-1])  # ['gecko', 'parrot', 'cat', 'dog']
# # start index should be greater than the end index if step is negative
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[7:2:-1])  # [8, 7, 6, 5, 4]
# print(numbers[2:7:-1])  # []
# # can chain slicing
# string = "no clouds here to spy on pets"
# print(string[::5][::-1])  # python

# email = "someone@yougotmail.com"
# print(email[:email.index('@')])
# print(email[:email.find("@")])
# print(email.split('@')[0])
# print((email[-16::-1])[::-1])

# numbers = [8, 11, 15, 15, 15, 12]
#
# def last_indexof_max(numbers):
#     index = 0
#     for i,n in enumerate(numbers):
#         print(n, i)
#         if n >= numbers[index]:
#             index = i
#             print(index)
#     return index

# =====================

# def recursive_factorial(n):
#     # Base case
#     if n == 0:
#         return 1
#     # Recursive case
#     else:
#         return n * recursive_factorial(n - 1)

# =====================

# vowels = {'a', 'e', 'i', 'o', 'u'}
#
# def find_apostrophe(word, start):
#     i = word.find("'", start)
#
#     if i == -1:  # there are no apostrophes in the given word
#         return -1
#
#     if i == 0:  # found apostrophe is the first symbol in the word, it doesn't meet the conditions
#         return find_apostrophe(word, 1)  # keep searching further
#
#     elif i == len(word) - 1:  # the apostrophe is the last symbol, doesn't meet the conditions
#         return -1  # we have reached the end of the word and haven't found a correct apostrophe
#
#     else:
#         previous_char = word[i - 1]
#         if previous_char in vowels:
#             return i
#
#         else:  # the found apostrophe does not meet the conditions, we keep searching further
#             return find_apostrophe(word, i + 1)

# =====================
import re

#
# regexp = 'burrito'
# string = 'boorrito'
# result1 = re.match(regexp, string)  # None
#
# result2 = re.match('hedge', 'hedgehog')
# print(result2 is None)  # False
#
# # match() is working only for substring located in the beginning of the string
# result = re.match('hog', 'hedgehog')  # None
# # because the beginning of the string doesn't match the template 'hog'
#
# # empty template doesn't need anything to match the string
# result3 = re.match('', 'not an empty string')  # match
#
# # . matches any single character, except for the newline character \n
# regexp = 'python .'
# re.match(regexp, 'python 3')
#
# # ? previous character can occur once or zero times
# regexp = 'regexp?'
# word1 = re.match(regexp, 'regex')  # match
# word2 = re.match(regexp, 'regexp')  # match
#
# # .? string can contain either any single character or nothing
# regexp = '.? points? to gryffindor'
# re.match(regexp, '1 point to gryffindor')
#
# # Escaping through backslashes
# # backslash "cancels" the special meaning of the following character
# re.match("\?", "?")  # match, '?' is the matching string
# re.match("\\?", "?")  # match, '?' is the matching string
# re.match("\\.", ".")  # match, '.' is the matching string
# re.match("?", "?")  # SyntaxError is caused by a "dangling metacharacter" in the regexp,
# an unescaped question mark not preceded by any character
#
# re.match("who let the dogs out?!", "who let the dogs out?!")  # no match
# re.match("who let the dogs out\?!", "who let the dogs out?!")  # match
# re.match("woof\.", "woof!")  # no match
# re.match("woof\.", "woof.")  # match
#
# # Escaping with r prefix - raw string notation prefix
# # tells Python to cancel the usage of escape sequences and treat all backslashes in their literal meaning
# re.match(r"\\", "\\")  # match: regexp consists of a regexp escape and a backslash
# re.match(r"\\.", ".")  # no match: no backslash in the string
# re.match(r"\\?", "?")  # match is an empty string: the question mark in regexp is unescaped
# re.match(r"\?", "?")  # match, as in the example above, \ is the regexp escape character
# re.match(r"\t", "\t")  # match, \t is the regexp escape sequence
#
# # re.escape - return string with all needed escapes
# template = "hyperskill.org"
# escaped_template = re.escape(template)  # 'hyperskill\\.org'

# # sets
# template = '[bd]a[td]'
# re.match(template, 'bat')  # match
# re.match(template, 'cat')  # no match: 'c' is not in the first set
#
# re.match('c[]at', 'cat')  # sre_constants.error: unexpected end of regular expression
#
# # metacharacters in sets is interpreted as regular characters
# template = 'Hodor[?.]'
# re.match(template, 'Hodor?')  # match
# re.match(template, 'Hodor!')  # no match
# # except backslashes = they serve as the starting symbol of escape sequences
# template = r'=[\]]'
# re.match(template, '=]')  # match
# template = r'=[)]]'
# re.match(template, '=]')  # no match
# re.match(template, '=)]')  # match (the only string this template can match)
# template = r'¯[\\]_'
# re.match(template, r'¯\_(ツ)_/¯')  # match because pattern in the beginning of the string
# template = r'¯[\t]_'
# re.match(template, '¯\_(ツ)_/¯')  # no match
# re.match(template, '¯\t_')  # match
#
# # Ranges
# re.match('ja[a-z].', 'jazz')  # match
# re.match('[A-Z]ill', 'kill')  # no match: [A-Z] matches only uppercase letters
# re.match('[0-9]', '7')   # match
# re.match('[1-9]', '07')  # no match
# re.match('love [a-zA-Z]', 'love U')  # match: [a-zA-Z] matches both uppercase and lowercase
# re.match('love [a-z!A-Z]', 'love !')  # match: [a-zA-Z!] matches letters and !
# re.match('[-1-9]1', '-1')  # match
# re.match('[1-9-]1', '-1')  # match
#
# # Exclusion of characters, ^ symbol must be in the beginning of the set
# re.match('[^A-Z]ond', 'Bond')  # no match
# re.match('Bon[^A-Z]', 'Bond')  # match

# print(re.match(r'M[rs]\.? Smith', 'Mr. Smith'))
# print(re.match('[A-Fa-f0-9][A-Fa-f0-9]?', '9'))

# # Shorthands for sets
# # \w == [a-zA-Z0-9_]
# # \d == [0-9]
# # \s == [ \t\n\r\f\v]
# re.match('\w\scamels?', '1 camel')  # match
# re.match('\w\scamels?', 'a\tcamel')  # match
# re.match('\d\scamels?', '8\ncamels')  # match
#
# # Negated shorthands
# # \W == [^a-zA-Z0-9_]
# # \D == [^0-9]
# # \S == [^ \t\n\r\f\v]
# re.match('\D\S\W', 'A1-')  # match
# re.match('\D\S\W', '1 A')  # no match
#
# # Escaping of shorthands
# # no need to use escaping, the same result:
# re.match('\w', 'X')
# re.match('\\w', 'X')
# re.match(r'\w', 'X')
# # If you need to escape
# re.match(r'\\w', r'\w')  # match
# re.match(r'\\w', r'\k')  # no match, because \\w isn't a shorthand here
#
# # Shorthands in sets
# re.match('attach[é\w]', 'attaché')  # match
# re.match('attach[é\w]', 'attache')  # match
# re.match('Stra[\wß][\wß]?e', 'Straße')  # match
# re.match('Stra[\wß][\wß]?e', 'Strasse')  # match
# # [\D\S] matches all possible characters
# re.match('[\D\S]', '0')  # match, 0 is not a whitespace character
# re.match('[\D\S]', '\n')  # match, \n is not a digit
# re.match('[\D\S]', 'a')  # match, 'a' is not a digit and not a whitespace character
# # [^\d\s] matches everything that does not fall into the categories of whitespaces and digits at the same time
# re.match('[^\d\s]', '0')  # no match, 0 is a digit
# re.match('[^\d\s]', '\t')  # no match, \t is a whitespace character
# re.match('[^\d\s]', 'a')  # match, 'a' is not a digit and not a whitespace
# # combinations
# re.match('[\Wa-c]', 'a')  # match, 'a' is in the set
# re.match('[\Wa-c]', 'z')  # no match: 'z' is alphanumeric and is not in the a-c range
# re.match('[\Wa-c]', '?')  # match, ? is not alphanumeric
#
# # Boundary shorthands
# # \b == end of word, matches an empty string between an alphanumeric character
# # (any character matching\w) and a non-alphanumeric character (\W) or absence of characters
# # use it to make sure that your regular expression will match only a separate word
# re.match(r'\b', 'Hello?')  # match (an empty string between the absence of a character and a letter)
# re.match(r'\b', '')  # no match (no alphanumeric character)
# re.match(r'Hail\b', 'Hail Mary!')  # match
# re.match(r'Hail\b Caesar', 'Hail Caesar')  # match (but \b is useless here)
# # need escaping
# re.match('Hail\b', 'Hail Mary!')  # no match, \b is a Python escape character
# re.match(r'Hail\b', 'Hail Mary!')  # match, \b is a regexp shorthand
#
# # \B matches the absence of the word boundary
# re.match(r'Hail\b', 'Hailey')  # no match
# re.match(r'Hail\B', 'Hailey')  # match
#
# # \A == matches only an empty string at the start of the string == ^
#
# # \Z matches an empty string at the end of the string == $
# re.match('Hail\Z', 'Hail!')  # no match
# re.match('Hail\Z', 'Hail')  # match
# re.match("Bring cash$", "Bring cash$")  # no match: $ in regexp means "the end of the string"
# re.match("Bring cash$", "Bring cash")  # match: h is the last character in the string

# print(re.match(r'[-\w~]', '?,'))  # no match

# # quantifiers
# # + == one or more occurrences
# template = "wo+w!"  # matches "wow!" with one or more 'o'
# re.match(template, "wow!")            # match: one 'o' character encountered
# re.match(template, "wooooooooooow!")  # match: many (11) 'o' characters encountered
# template = ".+Jack Sparrow"  # matches the string "Jack Sparrow" with some preceding characters
# re.match(template, "Captain Jack Sparrow")  # match: there are some characters before "Jack"
# re.match(template, "Jack Sparrow")          # no match: the string starts with "Jack"
# template = "Louis [IXV]+"
# re.match(template, "Louis III")  # match
# re.match(template, "Louis XVI")  # match
# re.match(template, "Louis ")     # no match
#
# # * == like + but also matches the absence of the previous character
# template = "go*d"
# re.match(template, "good")  # match: double 'o' occured
# re.match(template, "god")   # match: one 'o' occured
# re.match(template, "gd")    # match: no 'o' occured,
# template = ".*no.*"  # matches 'no' with any or no preceding/following sequences of characters
# re.match(template, "no")                             # match: 'no' is the whole string
# re.match(template, "no rest for the wicked")         # match: 'no' at the start of the string
# re.match(template, "I'm no superman")                # match: 'no' inside the string
#
# # {n} == fixed number of repetitions
# template = "\w{5}"  # matches a sequence of exactly 5 alphanumeric characters
# re.match(template, "doggy")  # match: 5 letters sequence
# re.match(template, "dog")    # no match: there're only 3 alphanumeric characters
# re.match(template, "a dog")  # no match: space doesn't match \w
#
# # {n,m} == matches at least n and no more than m instances of the previous (quantified) character
# template = "\d{5,10}"  # matches any sequence of digits with length from 5 to 10
# re.match(template, "1234567890")  # match: 10 digits
# re.match(template, "1234")        # no match: only 4 digits
# template = "i'm just a po{2,}r boy"  # there should be at least 2 'o' in the string
# re.match(template, "i'm just a pooooooooor boy")  # match: 9 'o'
# re.match(template, "i'm just a por boy")          # no match
# template = "i need no sy{,3}mpathy"  # there should be no more than 3 'y'
# re.match(template, "i need no syyympathy")   # match: 3 'y'
# re.match(template, "i need no smpathy")      # match: zero occurrences match the quantifier too
#
# # +?, *?, {n,m}? == ? character makes quantifiers "lazy", i.e. matches as few occurrences of the quantified character as possible
# # by default quantifiers are "greedy", i.e. match the longest possible string
# template = "<p>.*?</p>"
# re.match(template, "<p>paragraph</p><p>another paragraph</p>")
# # the template first matches the substring "<p>paragraph</p>"

# print(re.match("[-\w]{5,}$", "126480~3"))
# print(re.match(r"[-a-z0-9.=_]{6,30}@hyperskill\.org$", "mainadmin@hyperskill,org"))
# print(re.match(r'<[a-z]+>.*?</[a-z]+>?', '<start></start><start></start>'))
# print(re.match(r"[-a-z0-9.=_]{6,30}@hyperskill\.(org|com|ru)$", "mainadmin@hyperskill.cot"))

# # () groups symbols
# re.match(r"(h[ao]){2}", "hoha")  # a match
# re.match(r"(h[ao]){2}", "haa")  # no match
# re.match(r"ha(\?!)?", "ha?!")  # a match
# re.match(r"ha(\?!)?", "ha")  # a match
# re.match(r"ha(\?!)?", "ha?")  # no match
#
# # nested groups
# re.match(r"(([A-Z]\d){2}\.)+", "A0C3.B8K5.")  # a match
# re.match(r"(([A-Z]\d){2}\.)+", "A0C3.")  # a match
# re.match(r"(([A-Z]\d){2}\.)+", "A0.C3B8K5")  # no match
#
# # method groups() returns substrings that match template's groups
# match = re.match(r"([Pp]ython) (\d)", "Python 3")
# print(match.groups())  # ('Python', '3')
#
# # method group() return matching substring for particular group by its number (count from 1)
# print(match.group(2))  # ('3')
#
# #group enumeration
# match = re.match(r"((\w+) group) ((\w+) group)", "first group second group")
# match.group(1)  # "first group"
# match.group(2)  # "first"
# match.group(3)  # "second group"
# match.group(4)  # "second"
#
# # in case of repeated group method returns only last match
# re.match(r"(Python (\d) ){2,}", "Python 2 Python 3 ").group(2)  # The output is "3"
#
# # group() w/o index returns whole matching substring
# re.match(r"b.d", "bad").group()  # "bad"
#
# # | equals 'or'
# re.match(r"python|java|kotlin", "python")  # a match
#
# # to mark the borders of the OR operator, we need to use groups
# re.match(r"(python|kotlin) (course|lesson)", "lesson")  # no match
# re.match(r"(python|kotlin) (course|lesson)" "python lesson")  # match
#
# match = re.match(r"(Value|Name|Type)Error", "TypeError")
# print(match.group(1)) if match else print("None")

# template = r"([\d]{1,}\) [a-zA-Z ]+)+"
# string = "1) cabbage 2) carrot 3) apple 10) orange juice"
# print(re.match(template, string))

# # indexes from span attribute of the Match object, end() returns index+1
# start = re.match(r"100%?", "100").start()  # 0
# end_1 = re.match(r"100%?", "100").end()  # 3
# end_2 = re.match(r"100%?", "100%").end()  # 4
# span = re.match(r"100%?", "100%").span()  # (0, 4)
#
# # flags
# lower = r'where is the money, Lebowski\?'
# upper = r'WHERE IS THE MONEY, Lebowski\?'
# string = 'Where Is the money, lebowski?'
# result_lower = re.match(lower, string, flags=re.IGNORECASE)  # match
# result_upper = re.match(upper, string, flags=re.IGNORECASE)  # match
#
# dot_template = 'new line .'
# no_flag = re.match(dot_template, 'new line \n')  # None
# with_flag = re.match(dot_template, 'new line \n', flags=re.DOTALL)  # match
#
# result = re.match('FLAG ME.', 'flag me\n', flags=re.IGNORECASE + re.DOTALL)  # match

# # iterator can be created with iter() method
# my_list = [1, 2, 3]
# my_iterator = iter(my_list)
# print(next(my_iterator))
# print(next(my_iterator))
#
# # 'for' loop creates iterator from iterable object too
# for item in my_list:
#     print(item)
#
# # zip() takes several iterables and returns an iterator of tuples
# # iteration will stop as soon as the shortest iterable is exhausted
# short_list = [1, 2]
# long_list = [10, 20, 30]
# for a, b in zip(short_list, long_list):
#     print(a, b)
# # 1 10
# # 2 20
#
# # enumerate() returns elements of an iterable along with their indexes one by one
# months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# for i, month in enumerate(months_list):
#     print(i + 1, month)

import itertools

# # itertools.chain() makes from few iterables one iterator
# list_1 = [1, 2, 3]
# list_2 = [4, 5]
# for i in itertools.chain(list_1, list_2):
#     print(i)
#
# # itertools.product()  returns the elements of Cartesian product one by one, i.e. all possible mixes of elements
# first_list = ['Hi', 'Bye', 'How are you']
# second_list = ['Jane', 'Anton']
# for first, second in itertools.product(first_list, second_list):
#     print(first, second)
# # Hi Jane
# # Hi Anton
# # Bye Jane
# # Bye Anton
# # How are you Jane
# # How are you Anton
#
# # itertools.combinations() returns all possible combinations of r items from an iterable containing n elements
# my_iterator = itertools.combinations(range(1, 1000000), 2)
# for i in range(3):
#     print(next(my_iterator))
# # (1, 2)
# # (1, 3)
# # (1, 4)

# flower_names = ['rose', 'tulip', 'sunflower', 'daisy']
# for r in range(1, 4):
#     for i in itertools.combinations(flower_names, r):
#         print(i)

# main_courses = ['beef stew', 'fried fish']
# price_main_courses = [28, 23]
# desserts = ['ice-cream', 'cake']
# price_desserts = [2, 4]
# drinks = ['cola', 'wine']
# price_drinks = [3, 10]
# for first, second in zip(itertools.product(main_courses, desserts, drinks), itertools.product(price_main_courses, price_desserts, price_drinks)):
#     sum = 0
#     for i in second:
#         sum += i
#     if sum <= 30:
#         print(" ".join(first), sum)

# # sorting
# strings = ['aa', 'b', 'aaa', 'q', 'qq']
# strings.sort()
# print(strings)  # ['aa', 'aaa', 'b', 'q', 'qq']
#
# numbers = [3, 2, 5, 4, 1]
# print(sorted(numbers))  # [1, 2, 3, 4, 5]
# numbers.sort(reverse=True)
# print(numbers)  # [5, 4, 3, 2, 1]
# print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]
#
# # key
# names = ['Mary', 'James', 'Tom', 'Katarina', 'John']
# names.sort(key=len)
# print(names)  # ['Tom', 'Mary', 'John', 'James', 'Katarina']
#
# nums = [7, 4, 1, 5]
# print(sorted(nums, key=lambda x: x % 2))  # [4, 7, 1, 5]
#
# def my_sorted(x):
#     return x - int(x)
#
# numbers = [1.5, 3.2, 4.3]
# print(sorted(numbers, key=my_sorted))  # [3.2, 4.3, 1.5]
#
# # reverse
# initial_list = [1, 2, 3, 4, 5]
# initial_list.reverse()
# print(initial_list)   # [5, 4, 3, 2, 1]
#
# numbers = [1, 2, 3, 4, 5]
# for number in reversed(numbers):
#     print(number)

# passwords = ['0vbno0re', 'ad12', 'fgghut', '4qp', 'qwerty']
# passwords.sort(key=len)
# for i in passwords:
#     print(i, len(i))