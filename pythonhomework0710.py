#Рівень 1

"""
#1
a = 17
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#2

print(a//b)
print(a%b)
#// відрізняється тим, що прибирає значення після коми. Округлює число, а % шукає остачу від ділення

#3
a = 2**10
b = 10**3

#4
price = 249.99
count = 3
print(price * count)

#5
a = 7 / 2
b = 7 // 2
c = 7.0 // 2
print(type(a)) #Тип флоат тому що є значення після коми
print(type(b)) #Тип інт тому що значення без ком
print(type(c)) #Тип флоат тому що сім в нас не ціла

#6
name = "Python"
print(name*3)

#7
a = "Привіт, " + "світ!"
print(a)
"""

#Рівень 2
"""
#8
pupils = 28
table = 6
print(pupuls//table)
print(pupils%table)

#9
num = 3725
minuts = (num%3600) // 60
hour = num // 3600
sec = num%60
print(hour, ":", minuts, ":", sec)


#10
num = 150
hour = 150//60
minuts = 150%60
print(minuts)

#11
c = 36.6
f = c*9 / 5 +32
print(f)

#12
a = 12.5
b = 8
s = a*b
p = a+b/2

#13
r = 7
pi = 3.14159
s = pi * (r**2)
l = 2*pi*r

#14
price = 1200
sale = 15
sum_sale = price/100 * sale
final_price = price - sum_sale

#15
salary = 25000
tax = 19.5
final = salary - (salary/100 * tax)

#16
v = 90
t = 2.5
s = v * t

#17
average = 10+11+8 / 3

"""

#Рівень 3
"""

#18
n = 7
if (n % 2)%2 == 0:
    print("0")
if (n % 2)%2 != 0:
    print("1")

#19
n = 473
print(n%10)


#20
n = 473
print(n//100)
print(n//10)
print(n//1)

#21
n = 859
summ = 0
for i in str(n):
    summ = summ+int(i)
print(summ)


#22
n = 123
new_n = (n % 10) * 100 + (n // 10 % 10) * 10 + (n // 100)
print(new_n)

#23
num = 144
print(num**0.5)

#24
days = 365
sec = ((365 * 24)*60)*60)
"""
#Рівень 4
"""
#25
x = "5"
y = "3"
print(x+y)
print(int(x) + int(y))
#Різниця у тому, що рядки додаються не математично, як 2+2=22.

#26
print(int(9.99))
#Дробова частина пропала, бо int має лише цілі числа, тож округлив це число

#27
x = True+True+True
y = True*10
print(type(x))
print(type(y))
#Інт у двох ситуаціях бо True = 1, False = 0


#28
a = 5
b = 10

b = b-a
a = a+b
print(a)
print(b)

#29
deposit = 10000
years = 3
rate = 12
summ = deposit * (1 + rate) ** years
print(summ)
"""
#30
num = 20
num1 = 2**20
stri = "-"
print(stri*20)
print("Результат : ", str(num1))

