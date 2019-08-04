good_credit = True
high_income = True

if good_credit and high_income:
    print('OK')
#and = ОБА параметра True
#or = хотя бы ОДИН ИЗ True

has_criminal_record = True
if (good_credit or high_income) and not has_criminal_record:
    print('OK!!')
else:
    print('In Jail!!!')
#not = проверка на False
#!!! необходимы скобки

###Задание с логическими операторами (and, or) и операторами сравнения(<, >, <=, >=, ==)

name = input('Введите свое имя: ')
if len(name) < 3:
    print('Ошибка! Имя должно содержать минимум 3 символа.')
elif len(name) > 50:
    print('Ошибка! Имя не может содержать больше 50 символов.')
else:
    print('Классное имя!:)')



