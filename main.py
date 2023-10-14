# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#26072023

           ###################################     Lesson   5   #################################
           ###################################     Lesson   5   #################################
           ###################################     Lesson   5   #################################
          ###################################     Lesson   5   #################################
          ###################################     Lesson   5   #################################
          ###################################     Lesson   5   #################################
          ###################################     Lesson   5   #################################

############   Modul 2 Lesson 5 exerсise 9
# Створіть ітератор, який перебирає всі паліндроми (слова, які читаються однаково зліва направо та зправа наліво)
# з заданого списку слів.
#   Приклад можливо подивитись у презентації до уроку

#
# class PalindromeIterator:
#     """  Створіть ітератор, який перебирає всі паліндроми з заданого списку слів.    """
#     def __init__(self, words):
#         self.words = words
#         self.current_index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.current_index < len(self.words):
#             word = self.words[self.current_index]
#             self.current_index += 1
#             if word == word[::-1]:
#                 return word
#         raise StopIteration
#
#
# words = ['потоп', 'привет', 'radar', 'python', 'шалаш', 'ушу']
# palindrome_iterator = PalindromeIterator(words)
# for bb_ in palindrome_iterator:
#     print(bb_)
#


# Вывод:
# level
# deified
# radar
# racecar


############   Modul 2 Lesson 5 exerсise 8
# Напишіть генератор, який видає послідовність простих чисел.
# Приклад можливо подивитись у презентації до уроку
#
# def prime_numbers():
#     """ генератор, який видає послідовність простих чисел.  """
#     yield 2
#     primes = [2]
#     num = 3
#     while True:
#         is_prime = True
#         for prime in primes:
#             if num % prime == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num
#             primes.append(num)
#         num += 2
#
#
# for bb_ in prime_numbers():
#     if bb_ > 50:
#         break
#     print("Прості числа:  ", bb_)
#

#         ##############    etalon    ######################
# def prime_numbers():
#     """ генератор, який видає послідовність простих чисел.  """
#     yield 2 # первое простое число
#     primes = [2] # список простых чисел
#     num = 3 # начинаем с 3
#     while True:
#         is_prime = True
#         for prime in primes:
#             if num % prime == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num
#             primes.append(num)
#         num += 2 # пропускаем четные числа

# Пример использования
# for prime_num in prime_numbers():
#     if prime_num > 50: # ограничение на вывод
#         break
#     print("Прості числа:  ", prime_num) # выводит все простые числа до 100
#


############   Modul 2 Lesson 5 exerсise 7
# Створіть ітератор, який перебирає всі парні числа з заданого діапазону.
#Приклад можливо подивитись у презентації до уроку

#
# class EvenNumber:
#     """  ітератор, який перебирає всі парні числа з заданого діапазону. """
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         self.current = self.start
#         return self
#
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         else:
#             while self.current % 2 != 0:
#                 self.current += 1
#             result = self.current
#             self.current += 2
#             return result
#
#
# even_number = EvenNumber(1, 10)
# for bb_ in even_number:
#     print(bb_)
#


        #####################   1    #########################
#
# def even_numbers(start, stop):
#     """  ітератор, який перебирає всі парні числа з заданого діапазону. """
#     for num in range(start, stop):
#         if num % 2 == 0:
#             yield num
#
#
# for bb_ in even_numbers(1, 17):
#     print(bb_)
#




############   Modul 2 Lesson 5 exerсise 6
# Напишіть генератор, який фільтрує непарні числа з заданої послідовності.
# Приклад можливо подивитись у презентації до уроку
#
# def odd_numbers(subseq):
#     """  генератор, який фільтрує непарні числа з заданої послідовності.   """
#     for num in subseq:
#         if num % 2 != 0:
#             yield num
#
#
# my_subseq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for bb_ in odd_numbers(my_subseq):
#     print(bb_)
#




############   Modul 2 Lesson 5 exerсise 5
# Реалізуйте ітератор для перебору всіх ключів словника. #   Приклад можливо подивитись у презентації до уроку

# class KeysIterator:
#     """ ітератор для перебору всіх ключів словника.  """
#     def __init__(self, dictionary):
#         self.keys = list(dictionary.keys())
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < len(self.keys):
#             key = self.keys[self.current]
#             self.current += 1
#             return key
#         else:
#             raise StopIteration
#
#
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'e':4}
# for key in KeysIterator(my_dict):
#     print(key)

############   Modul 2 Lesson 5 exerсise 4
# Напишіть генератор, який видає послідовність квадратів чисел від 1 до N.
#Приклад можливо подивитись у презентації до уроку
#
# def squares_generator(N):
#     """      генератор, який видає послідовність квадратів чисел від 1 до N.  """
#     for i in range(1, N+1):
#         yield i**2
#
#
# for bb_ in squares_generator(10):
#     print(bb_)


############   Modul 2 Lesson 5 exerсise 3
# Створіть ітератор який буде приймати рядок та кожен виклик методу next() буде повертати наступний символ рядку.
#  Приклад можливо подивитись у презентації до уроку


#
# class StringIterator:
#     """
#     Створіть ітератор який буде приймати рядок та кожен виклик методу next() буде повертати наступний символ рядку.
#     """
#     def __init__(self, string):
#         self.string = string
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.string):
#             raise StopIteration
#         result = self.string[self.index]
#         self.index += 1
#         return result
#
#
# string = "Create an iterator"
# iterator = StringIterator(string)
# for bb_ in iterator:
#     print(bb_)
#


############   Modul 2 Lesson 5 exerсise 2
# Напишіть генератор, який повертає послідовність чисел Фібоначчі.
#Приклад можливо подивитись у презентації до уроку

# def fibonacci_generator(n):
#     """  генератор, який повертає послідовність чисел Фібоначчі.      """
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
#
# for bb_ in fibonacci_generator(10):
#     print(bb_)
#

############   Modul 2 Lesson 5 exerсise 1
# Змініть функцію even_odd_generator так, щоб вона генерувала послідовність чисел від 1 до n з рядками "Fizz"
# для чисел, які діляться на 3, "Buzz" для чисел, які діляться на 5, і "FizzBuzz"
# для чисел, які діляться як на 3, так і на 5.
# Приклад можливо подивитись у презентації до уроку

#
# def even_odd_generator(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             yield "FizzBuzz"
#         elif i % 3 == 0:
#             yield "Fizz"
#         elif i % 5 == 0:
#             yield "Buzz"
#         else:
#             yield i
#
# for bb_ in even_odd_generator(25):
#     print(bb_)
#

         ###################################     Lesson   4    #################################
###################################     Lesson   4    #################################
###################################     Lesson   4    #################################
###################################     Lesson   4    #################################
###################################     Lesson   4    #################################
###################################     Lesson   4    #################################
###################################     Lesson   4    #################################
############   Modul 2 Lesson 4 exerсise 7
# Створіть декоратор **`rate_limit`**, який обмежує кількість викликів декорованої функції протягом певного періоду часу.
# Декоратор повинен приймати два параметри `max_calls` та `period`. Перший парметр - максимальна кількість
# допустимих викликів функції. Другий параметр - кількість секунд у рамках яких ми можемо зробити `max_calls`
# викликів. Вам допоможе модуль `datetime` для вирішення цієї задачі.
#                                   (приклад є у презентації)

#
# import time
# from datetime import datetime, timedelta
#
# def rate_limit(max_calls, period):
#     def decorator(func):
#         calls = []
#         def wrapper(*args, **kwargs):
#             now = datetime.now()
#             calls_within_period = [call for call in calls if now - call < timedelta(seconds=period)]
#             if len(calls_within_period) >= max_calls:
#                 time_to_wait = (calls_within_period[-1] + timedelta(seconds=period) - now).total_seconds()
#                 print(f"Rate limit exceeded.  {time_to_wait:.2f} seconds before retrying.")
#                 time.sleep(time_to_wait)
#             result = func(*args, **kwargs)
#             calls.append(datetime.now())
#             return result
#         return wrapper
#     return decorator
#
# @rate_limit(max_calls=2, period=5)
# def print_hello():
#     print("Привет")
#
# print_hello()
# print_hello()
# print_hello()
#

# Вывод:
#
#
# Hello
# Hello
# Rate limit exceeded. Waiting 5.00 seconds before retrying.
# Hello
#

#
# Декоратор rate_limit принимает два параметра: max_calls и period. Возвращает он другой декоратор, который принимает декорируемую функцию и возвращает обертку. Обертка создаёт список calls для хранения временных меток вызовов функции. При вызове обертки с аргументами args и kwargs, обертка проверяет, сколько вызовов функции было сделано в течение последних period секунд. Если количество вызовов превышает max_calls, то обертка ждет оставшееся время до конца периода и печатает сообщение о том, что лимит вызовов превышен. Затем обертка вызывает декорируемую функцию и сохраняет текущую временную метку в список calls.
#
# Пример использования:
#
# python

############   Modul 2 Lesson 4 exerсise 6
# Реалізувати декоратор кешування memoize, який кешує результати
# декорованої функції для покращення продуктивності при повторних викликах з тими самими аргументами.
# Тобто він повинен запамʼятовувати аргументи з якими функція визивалась і результат роботи функції з цими аргументами.
# І у випадку, якщо ми вже маємо результат для цих аргументів, просто повернути закешований результат,
# замість виклику функції.
#
# def memoize(func):
#     cache = {}
#     def wrapper(*args):
#         if args in cache:
#             return cache[args]
#         else:
#             result = func(*args)
#             cache[args] = result
#             return result
#     return wrapper
#
#
# @memoize
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         #print(fibonacci)
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(15))
# print(fibonacci(15))
#

# Вывод:
#
#
# 55
# 55
#



# Декоратор memoize принимает декорируемую функцию и возвращает обертку. Обертка создаёт словарь cache для хранения кэшированных результатов. При вызове обертки с аргументами args, обертка проверяет, есть ли уже результат выполнения функции с этими аргументами в кэше. Если есть, то обертка возвращает закэшированный результат. Если нет, то обертка вызывает декорируемую функцию с этими аргументами, сохраняет результат в кэше и возвращает его.
#
# Пример использования:
#
# python
#print(fibonacci(10)) # Cached result is returned, no function call is made

############   Modul 2 Lesson 4 exerсise 5
# Створіть декоратор retry який приймає першим аргументом число -  кількість разів, яку потрібно буде
# повторити виконання функції у разі викидання нею помилки.
#                            (приклад можно знайти у презентації)
#
# import time
#
# def retry(nom_retries):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(nom_retries):
#                 try:
#                     result = func(*args, **kwargs)
#                     return result
#                 except Exception as e:
#                     print(f"Attempt {i+1} failed with error: {e}")
#                     time.sleep(1)
#             raise Exception(f"All {nom_retries} attempts failed")
#         return wrapper
#     return decorator
#
# @retry(nom_retries=5)
# def my_function():
#     if time.time() % 2 == 0:
#         return "Success"
#     else:
#         raise Exception("Random error")
#
# result = my_function()
# print(result)
#


   #########################    1    ##########################
#
# import time
#
# def retry(num_retries):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num_retries):
#                 try:
#                     result = func(*args, **kwargs)
#                     return result
#                 except:
#                     print("Error occurred. Retrying...")
#                     time.sleep(1)
#             raise Exception("Function execution failed after %d retries" % num_retries)
#         return wrapper
#     return decorator
#
#
# # Декоратор retry принимает число num_retries и возвращает декоратор, который принимает декорируемую функцию и возвращает
# # обертку. Обертка пытается выполнить декорируемую функцию и возвращает её результат. Если при выполнении функции возникает
# # ошибка, обертка ждёт 1 секунду и повторяет попытку выполнения функции. Если после num_retries попыток выполнение функции
# # не удалось, обертка выбрасывает исключение.
# #
# # Пример использования:
# #
# # python
# @retry(num_retries=3)
# def my_function():
#     if time.time() % 2 == 0:
#         return "Success"
#     else:
#         raise Exception("Random error")
#
# result = my_function()
# print(result)
#
# #
# # Вывод:
# #
# #
# # Error occurred. Retrying...
# # Error occurred. Retrying...
# # Success


############   Modul 2 Lesson 4 exerсise 4
# Реалізувати декоратор timeit, який вимірює час виконання декорованої функції і виводить його. Для отримання часу
# роботи скористуйтесь модулем time і функцією time.time()

#
# import time
#
#
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print("Execution time:", end_time - start_time, "seconds")
#         return result
#
#     return wrapper
#
#
# @timeit
# def my_function():
#     time.sleep(1)
#
# my_function()
#

#Декоратор timeit принимает декорируемую функцию и возвращает обертку, которая измеряет время выполнения декорируемой функции
# и выводит его. Обертка также возвращает результат выполнения декорируемой функции.


# Вывод:
#
# Execution
# time: 1.0001230239868164
# seconds

############   Modul 2 Lesson 4 exerсise 3
# Створіть простий декоратор логування log_func, який буде прінтити будь
# яке повідомлення перед визовом декорованої функції, та після.

# def log_func(message):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(message)
#             result = func(*args, **kwargs)
#             print(message)
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# @log_func("***  Starting function...")
# def my_function():
#     print("Hello, World!!!")
#
#
# my_function()
#

# Декоратор log_func принимает сообщение в качестве аргумента и возвращает функцию - декоратор.Функция - декоратор принимает
# декорируемую функцию и возвращает обертку, которая выводит  сообщение перед и после вызова  декорируемой функции.Обертка
# также  возвращает результат выполнения декорируемой функции.
# Пример
# использования:
#
# python


# Вывод:
#
# Starting
# function...
# Hello, world!
# Starting
# function...

############   Modul 2 Lesson 4 exerсise 2
# Створіть контекстний менеджер DividerContext, який буде прінтити символ, який ми до нього передамо як розділитель
# для основного блоку коду до та після його виконання. Реалізувати контекстний менеджер потрібно 2 способами,
# за допомогою декоратора contextmanager та за допомогою класу.
# (приклад можно знайти у презентації)

#
#
# from contextlib import contextmanager
#
# print("1 способ: за допомогою декоратора contextmanager.")
#
# @contextmanager
# def DividerContext(symbol):
#     print(symbol * 15)
#     yield
#     print(symbol * 15)
#
#
# with DividerContext("*"):
#     print("Hello, world!")
#
# print("2 способ: за допомогою класу.")
#
# class DividerContext:
#     def __init__(self, symbol):
#         self.symbol = symbol
#
#     def __enter__(self):
#         print(self.symbol * 20)
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(self.symbol * 20)
#
#
# with DividerContext("*"):
#     print("Hello, world!")
#

############   Modul 2 Lesson 4 exerсise 1
# Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду. Контекстний менеджер повинен виводити
# час, що минув, при виході з контексту. Використовуйте контекстний менеджер для вимірювання часу виконання
# певного фрагменту коду. Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора
# contextmanager та за допомогою класу.

# Решение:
#
# Используем
# модуль
# time
# для
# измерения
# времени
# выполнения
# кода.
#
# Способ
# 1: с
# помощью
# декоратора
# contextmanager
#
# python


# from contextlib import contextmanager
# import time
#
# print("1 способ: за допомогою декоратора contextmanager.")
#
# @contextmanager
# def Timer():
#     start = time.time()
#     yield
#     end = time.time()
#     print(f"Function Time: {end - start} seconds")
#
# with Timer():
#     time.sleep(1)
#
#
# print("2 способ: за допомогою класу.")
# # import time
#
# class Timer:
#     def __enter__(self):
#         self.start = time.time()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         end = time.time()
#         print(f"Function Time: {end - self.start} seconds")
#
# with Timer():
#     time.sleep(1)



############   Modul 2 Lesson 3 exerсise 8
# Створіть клас Book який має такі атрибути к рік видання, назву, автор та кількість сторінок. Створіть статік
# метод який буде приймати список книжок та рік, та повертати кількість книжок з цього списку
# які були опубліковані у цьому році.

#
# class Book:
#     """   """
#     books = []
#
#     def __init__(self, year, title, author, pages):
#         self.year = year
#         self.title = title
#         self.author = author
#         self.pages = pages
#         Book.books.append(self)
#
#     @staticmethod
#     def count_books_published_in_year(list_book, year):
#         count = 0
#         for book in list_book:
#             if book.year == year:
#                 count += 1
#         return count
#
# book1 = Book(2023, "Назва книги 1", "Автор 1", 223)
# book2 = Book(2023, "Назва книги 2", "Автор 2", 251)
# book3 = Book(2022, "Назва книги 3", "Автор 3", 1178)
# book4 = Book(2023, "Назва книги 4", "Автор 4", 1178)
# book5 = Book(2022, "Назва книги 5", "Автор 5", 1178)
#
# books_published_in_current_year = Book.count_books_published_in_year(Book.books, 2023)
# print("кількість книжок зі списку, які були опубліковані у цьому році: ", books_published_in_current_year)
#
#
#

############   Modul 2 Lesson 3 exerсise 7
# Створіть клас Student, який представляє студента. Реалізуйте атрибут класу для відстеження кількості студентів.
# Для цього змінюйте значення атрибуту класу у методі __init__ . Та створіть клас метод для виведення загальної
# кількості студентів.
#
# class Student:
#     total_students = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.total_students += 1
#
#     @classmethod
#     def total_all_students(cls):
#         print("Усього студентів:", cls.total_students)
#
#
#
# student1 = Student("Марченко", 20)
# student2 = Student("Наконечна", 19)
# student3 = Student("Сила", 18)
# Student.total_all_students()
#


############   Modul 2 Lesson 3 exerсise 6
# Створіть клас Circle, який представляє коло. Реалізуйте методи для обчислення площі та довжини кола.
# Використовуйте аттрибут класу для зберігання значення π (pi).

# class Circle:
#     """
#     клас Circle, який представляє коло. Реалізовані методи для обчислення площі та довжини кола.
#     """
#     pi = 3.1415926
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return Circle.pi * self.radius ** 2
#
#     def circumference(self):
#         return 2 * Circle.pi * self.radius
#
#
# circle = Circle(10)
# print(circle.area())
# print(circle.circumference())
#


############   Modul 2 Lesson 3 exerсise 5
# Розробіть клас Library для представлення бібліотеки. А також класс Book для представлення книги. Класс Library повинен
# мати атрибут books зі списком книжок. Кожна книга в бібліотеці має атрибути, такі як назва, автор і рік видання.
# Додайте метод add_book, який додає нову книгу до бібліотеки. Реалізуйте метод __str__,
# який виводить список книг у бібліотеці. Створіть об'єкт Library і додайте кілька книг. Виведіть список книг у бібліотеці.

#
# class Book:
#     """    класс Book для представлення книги     """
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def __str__(self):
#         return f"{self.title} by {self.author}, {self.year}"
#
# class Library:
#     """     клас Library для представлення бібліотеки.     """
#     books = []
#     def add_book(self, book):
#         self.books.append(book)
#
#     def __str__(self):
#         book_list = ""
#         for book in self.books:
#             book_list += str(book) + "\n"
#         return book_list
#
# library = Library()
# book1 = Book("Леся Українка", "Ф.С.Кислий", 1986)
# book2 = Book("Мері Поппінс", "Памела Треверс", 2016)
# book3 = Book("Пригоди Тома Сойєра", "Марк Твен", 1984)
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# print(library)
#

        #########################    1      ###############################

# class Book:
#     """    класс Book для представлення книги     """
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def __str__(self):
#         return f"{self.title} ({self.author}, {self.year})"
#
#
# class Library:
#     """     клас Library для представлення бібліотеки.     """
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def __str__(self):
#         return "\n".join(str(book) for book in self.books)
#
# library = Library()
# book1 = Book("Леся Українка", "Ф.С.Кислий", 1986)
# book2 = Book("Мері Поппінс", "Памела Треверс", 2016)
# book3 = Book("Пригоди Тома Сойєра", "Марк Твен", 1984)
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# print(library)
#



# Результат:
#
# The
# Catcher in the
# Rye(J.D.Salinger, 1951)
# To
# Kill
# a
# Mockingbird(Harper
# Lee, 1960)
# 1984(George
# Orwell, 1949)
#



############   Modul 2 Lesson 3 exerсise 4
# Створіть клас Student для представлення студента. Додайте атрибути, такі як ім'я, прізвище і список оцінок.
# Реалізуйте метод __len__, який повертає кількість оцінок студента. Створіть список студентів
# і відсортуйте його за кількістю оцінок.

#
# class Student:
#     """
#     клас Student для представлення студента. Клас на такі атрибути: ім'я, прізвище і список оцінок.
#     Реалізован метод __len__, який повертає кількість оцінок студента
#     """
#     def __init__(self, first_name, last_name, grades):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.grades = grades
#
#     def __len__(self):
#         return len(self.grades)
#
#
# students = [Student("Олександр", "Марченко", [4, 5, 5]), Student("Віктор ", "Smith", [5, 3, 4, 4]), Student("Тарас", "Сила", [4,4])]
# sort_students = sorted(students, key=lambda x: len(x))
#
# for student in sort_students:
#     print(student.first_name, student.last_name, student.grades)
#
#


# Результат:
#
# Bob
# Johnson[4]
# John
# Doe[4, 3, 5]
# Jane
# Smith[5, 5, 4, 3]

############   Modul 2 Lesson 3 exerсise 3
# Розробіть клас Vehicle для представлення транспортного засобу. Додайте атрибути, такі як назва, швидкість і вартість.
# Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю. Створіть список транспортних засобів
# і відсортуйте його за швидкістю.


# class Vehicle:
#     """
#     клас Vehicle для представлення транспортного засобу  / назва, швидкість і вартість.
#     """
#     def __init__(self, name, speed, cost):
#         self.name = name    # назва
#         self.speed = speed  # швидкість
#         self.cost = cost    # вартість
#
#     def gt(self, other):
#         if self.speed > other.speed:
#             return True
#         else:
#             return False
#
# vehicles = [Vehicle("Car1", 220, 25000), Vehicle("Car2", 180, 5000), Vehicle("Car3", 160, 3100), Vehicle("Car4", 160, 2500)]
# sort_vehicles = sorted(vehicles, key=lambda x: x.speed)
#
# for vehicle in sort_vehicles:
#     print(vehicle.name, vehicle.speed, vehicle.cost)

# Результат:
#
# Bike
# 80
# 5000
# Boat
# 60
# 35000
# Car
# 120
# 25000
#


############   Modul 2 Lesson 3 exerсise 2
# Розробіть клас BankAccount для представлення банківського рахунку. Додайте методи для зняття
# та поповнення коштів на рахунку. Використовуйте магічний метод __str__ для виведення інформації про рахунок.

# class BankAccount:
#     """
#     Клас BankAccount для представлення банківського рахунку. Додани методи для зняття
#     та поповнення коштів на рахунку. Використовується магічний метод __str__ для виведення інформації про рахунок.
#     """
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self, money):
#         self.balance += money
#
#     def withdraw(self, money):
#         if self.balance >= money:
#             self.balance -= money
#         else:
#             print("Недостатньо коштів.")
#
#     def __str__(self):
#         return "Баланс: " + str(self.balance)
#
# account = BankAccount(5000)
# print(account)
# account.deposit(500)
# print(account)
# account.withdraw(200)
# print(account)
# account.withdraw(1500)
# print(account)
#
# Результат:
#
# Balance: $1000
# Balance: $1500
# Balance: $1300
# Insufficient
# funds
# Balance: $1300

############   Modul 2 Lesson 3 exerсise 1
# Створіть клас Rectangle для представлення прямокутника. Додайте методи для обчислення площі
# та периметра прямокутника. Створіть об'єкт Rectangle і викличте ці методи.
#
# class Rectangle:
#     """
#     Клас Rectangle для представлення прямокутника. Метод для обчислення площі
#     та Метод для обчислення периметра прямокутника
#     """
#     def __init__(self, width, height):
#         self.height = height
#         self.width = width
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# my_rect = Rectangle(10, 10)
# print("обчислення площі :", my_rect.area())
# print("Метод для обчислення периметра прямокутника:", my_rect.perimeter())
#


# Результат:
#
# Area: 50
# Perimeter: 30



# moduL 2 Lesson 1  exp 1
# Створити програму - гру "Поле чудес".
#
# Зареєструватись на github, та створити окремий репозиторій для цього завдання

# Створити програму - гру "Поле чудес".
#
# Зареєструватись на github, та створити окремий репозиторій для цього завдання
#
# 1. Програма буде брати зі списку слів одне рандомне слово.
# 2. Програма буде отримувати від користувача число - кількість спроб вгадати
# 3. Далі програма буде чекати від користувача або букву, або ціле слово.
# 4. Якщо користувач пише слово, програма повинна перевіряти чи це не те саме число, якщо так то говорити що користувач вгадав слово, або писати що слово не правильне.
# 5. Якщо користувач ввів літеру, програма повинна перевірити чи є ця літера у нашому слові, та якщо є, виводити наше слово, де зірочками будуть закриті всі літери, які користувач ще не вгадав, або "Такої літери немає"
# 6. Якщо кількість спроб закінчиться, потрібно сказати користувачю, що він програв та закінчити роботу програми.
#
# Приклад:
# Програмою обрано слово "apple"
# Вхід: 10 (10 спроб вгадати слово)
# Вхід: "a"
# Вихід: "a****"
# Вхід: "d"
# Вихід: "Такої літери немає"
# Вхід: "l"
# Вихід: "a**l*"
# Вхід: "e"
# Вихід: "a**le"
# Вхід: "apple"
# Вихід: "Вітаю, ви вгадали слово"
#
# Код програми залейте до вашого репозиторію та надішліть посилання у відповідь.


import random


def field_of_dreams():
    """   Гра: "Поле чудес".    """
    list_words = ["house", "school", "lesson", "python", "program"]
    word = random.choice(list_words)
    my_count = int(input("Слова на англійській мові. Введіть, будь ласка, кількість спроб для того щоб вгадати: "))
    guessed_word = ["*" for ww in word]

    while my_count > 0:
        print("".join(guessed_word))
        user_input = input("Введіть, будь ласка, букву чи слово: ")
        if user_input == word:
            print("Поздоровляю, ВИ вгадали слово: ", word)
            return
        elif len(user_input) > 1:
            print("Не вірне слово")
            my_count -= 1
        else:
            if user_input in word:
                for i in range(len(word)):
                    if word[i] == user_input:
                        guessed_word[i] = user_input
                if "*" not in guessed_word:
                    print("Поздоровляю, ВИ вгадали слово: ", word)
                    return
            else:
                print("Такої літери немає")
                my_count -= 1

    print("Ви, нажаль, цю гру програли. Ви не вгадали слово: ", word)

field_of_dreams()



# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
   # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
