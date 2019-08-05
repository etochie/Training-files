# Калькулятор v2 (+ colorama)


from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

print(Back.RED)

what = input(" Что делаем? (+, -): ")

print(Back.CYAN)

a = float( input("Введите первое число: "))  # !!! input - тип данных str (строка), поэтому используем тайпкастинг в
# вещественное float
b = float( input("Введите второе число: "))

print(Back.GREEN)

if what == "+":
	c = a + b
	print("Результат: " + str(c))
elif what == "-":  # elif - если выполняется блок if, блок elif не будет выполняться в любом случае
	c = a - b
	print("Результат: " + str(c))
else:
	print("Выбрана неверная операция!")

input()
