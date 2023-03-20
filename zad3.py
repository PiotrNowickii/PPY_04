import random

x = input("Wprowadź liczbę rund: ")
mode = input("Wybierz tryb gry: 1 - hot seats, 2 - komputer")
if mode == "1":


if mode == "2":
    k = 0
    while(True):
        k += 1
        print("Round " + str(k) + "!")
        choice = input("Wybierz: 1 - Kamien, 2 - papier, 3 - nożyce")
        bot_choice_list = ["1", "2", "3"]
        bot_choice = random.sample(bot_choice_list, 1)
