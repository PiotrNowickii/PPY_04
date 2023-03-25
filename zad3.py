import random
import getpass

x = input("Wprowadź liczbę rund: ")
mode = input("Wybierz tryb gry: 1 - hot seats, 2 - komputer: ")
k = 0
gameList = []
if mode == "1":
    nameOne = input("Podaj nazwę gracza 1: ")
    nameTwo = input("Podaj nazwę gracza 2: ")
    playerOnePoints = 0
    playerTwoPoints = 0
    while k < int(x):
        k += 1
        print("Round " + str(k) + "!")
        pOneChoice = getpass.getpass(nameOne + ': Wybierz: 1 - Kamien, 2 - papier, 3 - nożyce\n')
        pTwoChoice = getpass.getpass(nameTwo + ': Wybierz: 1 - Kamien, 2 - papier, 3 - nożyce\n')
        if int(pOneChoice) == int(pTwoChoice):
            print("Remis, brak punktów")
            gameList.append("Round " + str(k) + ": Remis")
        elif int(pOneChoice) == 1:
            if playerTwoPoints == 2:
                print("Papier wygrywa z kamieniem, punkt dla gracza " + nameTwo)
                gameList.append("Round " + str(k) + ": Papier wygrywa z kamieniem, punkt dla gracza " + nameTwo)
                playerTwoPoints += 1
            else:
                print("Kamień wygrywa z nożycami, punkt dla gracza " + nameOne)
                gameList.append("Round " + str(k) + ": Kamień wygrywa z nożycami, punkt dla gracza " + nameOne)
                playerOnePoints += 1
        elif int(pOneChoice) == 2:
            if playerTwoPoints == 1:
                print("Papier wygrywa z kamieniem, punkt dla gracza " + nameOne)
                gameList.append("Round " + str(k) + ": Papier wygrywa z kamieniem, punkt dla gracza " + nameOne)
                playerOnePoints += 1
            else:
                print("Nożyce wygrywają z papierem, punkt dla gracza " + nameTwo)
                gameList.append("Round " + str(k) + ": Nożyce wygrywają z papierem, punkt dla gracza " + nameTwo)
                playerTwoPoints += 1
        elif int(pOneChoice) == 3:
            if playerTwoPoints == 2:
                print("Nożyce wygrywają z papierem, punkt dla gracza " + nameOne)
                gameList.append("Round " + str(k) + ": Nożyce wygrywają z papierem, punkt dla gracza " + nameOne)
                playerOnePoints += 1
            else:
                print("Kamień wygrywa z nożycami, punkt dla gracza " + nameTwo)
                gameList.append("Round " + str(k) + ": Kamień wygrywa z nożycami, punkt dla gracza " + nameTwo)
                playerTwoPoints += 1
    print()
    for i in gameList:
        print(i)
    print()
    print("Punkty gracza "+ nameOne + ": " + str(playerOnePoints))
    print("Punkty gracza "+ nameTwo + ": " + str(playerTwoPoints))
    if playerTwoPoints == playerOnePoints:
        print("REMIS")
    elif playerTwoPoints > playerOnePoints:
        print("Wygrywa gracz " + nameTwo + "!")
    elif playerOnePoints > playerTwoPoints:
        print("Wygrywa gracz " + nameOne + "!")
elif mode == "2":
    botPoints = 0
    points = 0
    while k < int(x):
        k += 1
        print("Round " + str(k) + "!")
        choice = input("Wybierz: 1 - Kamien, 2 - papier, 3 - nożyce\n")
        bot_choice = random.randint(1, 3)
        if int(choice) == bot_choice:
            print("Remis, brak punktów")
            gameList.append("Round " + str(k) + ": Remis")
        elif int(choice) == 1:
            if bot_choice == 2:
                print("Papier wygrywa z kamieniem, punkt dla bota.")
                gameList.append("Round " + str(k) + ": Papier wygrywa z kamieniem, punkt dla bota.")
                botPoints += 1
            else:
                print("Kamień wygrywa z nożycami, punkt dla gracza.")
                gameList.append("Round " + str(k) + ": Kamień wygrywa z nożycami, punkt dla gracza.")
                points += 1
        elif int(choice) == 2:
            if bot_choice == 1:
                print("Papier wygrywa z kamieniem, punkt dla gracza.")
                gameList.append("Round " + str(k) + ": Papier wygrywa z kamieniem, punkt dla gracza.")
                points += 1
            else:
                print("Nożyce wygrywają z papierem, punkt dla bota.")
                gameList.append("Round " + str(k) + ": Nożyce wygrywają z papierem, punkt dla bota.")
                botPoints += 1
        elif int(choice) == 3:
            if bot_choice == 2:
                print("Nożyce wygrywają z papierem, punkt dla gracza.")
                gameList.append("Round " + str(k) + ": Nożyce wygrywają z papierem, punkt dla gracza.")
                points += 1
            else:
                print("Kamień wygrywa z nożycami, punkt dla bota.")
                gameList.append("Round " + str(k) + ": Kamień wygrywa z nożycami, punkt dla bota.")
                botPoints += 1
    print()
    for i in gameList:
        print(i)
    print()
    print("Punkty gracza: " + str(points))
    print("Punkty bota: " + str(botPoints) + "\n")
    if botPoints == points:
        print("REMIS")
    elif botPoints > points:
        print("Wygrywa bot...")
    elif points > botPoints:
        print("Wygrywa gracz!")
