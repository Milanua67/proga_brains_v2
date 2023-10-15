# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#26072023


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
