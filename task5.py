from random import randint

n = randint(0, 1000)
counter = 0

while counter < 11:
    userInput = int(input("Введи число: "))
    if userInput == n:
        print("ТЫ УГАДАЛ!")
        break
    elif userInput > n:
        print("Меньше!")
        counter += 1
    elif userInput < n:
        print("Больше!")
        counter += 1

if counter == 11:
    print("К сожалению ты проиграл!")


