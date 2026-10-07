num = input("Введіть число: ")

if num.lstrip("-").isdigit():
    num = int(num)
    if num > 0 :
        print("Додатне")
    elif num < 0:
        print("Від'ємне")
    else:
        print("Нуль")
else:   
    print("Введіть саме число!")
