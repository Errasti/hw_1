def simpleOrNot(number):
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    if counter == 2:
        return print("Простое число")
    else:
        return print("Составное число")


flag = True
while flag:
    n = int(input("Введите число от 0 до 100 000 : "))
    if 0 < n < 100000:
        flag = False
simpleOrNot(n)

