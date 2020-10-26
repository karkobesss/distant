import random
#1
a = int(input('введите первое число:'))
b = int(input('введите второе число: '))
mass1 = []
i = 0
while i < 10:
    mass1.append(random.randint(a, b))
    i += 1
#2
mass2 = []
n = 0
while n < 10:
    mass2.append(chr(random.randint(97, 122)))
    n += 1
#3
mass3 = []
d = 0
while d < 5:
    p = int(input('ВВод: '))
    try:
        assert 0 < p < 10
        mass3.append(p)
    except:
        print("Что-то пошло не так")
    d += 1
print(mass3)
#4
mass4 = mass1[4:7]
#5
mass5 = mass2[int(input('от: ')):int(input('до: '))]
#6
mass6 = mass4 + mass5
#7
v = 0
mass7 = []
while v < 5:
    mass7.append(mass2[mass3[v]])
    v += 1
print(mass7)
#8
try:
    mass1.remove(5)
except:
    print('5 нет в списке')
try:
    mass2.remove('г')
except:
    print('г нет в списке')
#9
n = 0
while n < 3:
    n += 1
    mass6.insert(2, n)
#10
mass2[3] = mass6[5]
#11
mass4.append("!")
print(mass6)
print(mass4)
