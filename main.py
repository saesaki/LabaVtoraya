import math

i=0
while i<5:
    x = int(input('Введите x = '))
    y = int(input('Введите y = '))
    R = abs(int(input('Введите R = ')))
    if (((x+R)**2+(y-R)**2<=R**2) and (0<=y<=2*R)) or ((0<=x<=2*R) and (-R<=y<=0)):
        print('Точка входит')
    else:
        print('Точка не входит')
    i+=1


    a new string of code
