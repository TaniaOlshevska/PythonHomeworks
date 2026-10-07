import random
num = random.randint(1,100)
predict = int(input("Введіть число: "))
count = 0

while predict != num:
    count += 1
    if predict > num:
        print("Рандомне число менше " , predict)
        predict = int(input("Введіть число: "))
    elif predict < num:
        print("Рандомне число більше " , predict)
        predict = int(input("Введіть число: "))

if predict == num:
    print("Вітаю! Ви вгадали")
    print(count)
    

