a = input("Введіть a: ")
b = input("Введіть b: ")
c = input("Введіть c: ")
if a.isdigit() and b.isdigit() and c.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)
    D = (b**2) - (4*a*c)
    if D>0:
        x1 = (-b+(D**0.5))/2*a
        x2 = (-b-(D**0.5))/2*a
        print(x1)
        print(x2)
    elif D == 0:
        x = -b/2*a
        print(x)
    else:
        print("D<0, error")
else:
    print("Помилка, введіть числа")


