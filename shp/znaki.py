# +, -, *, /, **, %, унарный минус, округление, число Пи

a = 5
b = 10
print("a = 5, b = 10")
c = a + b # так же -, *, /
print("Сложение  a + b = " + str(c) )

d = a ** 2 # возведение в степень
print ("Возведение в степень a^2 = " +str(d))

# Унарный минус
a = 10
a = -a
print (a)

b = 5
b = -b
b = -b
print(b)

#Округление
e = 5.65
print( round(e))

#Принудительное округление
import math
f = 9.65
print( math.floor(f)) #math.FLOOR - в меньшую сторону
print( math.ceil(f)) #math.CEIL - в большую сторону
