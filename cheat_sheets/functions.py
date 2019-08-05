msg = 'Hello world! Good luck!'
msg2 = 'HeLLo WOrLd!!!' # для title


print(msg)

print(msg.upper())# upper - верхний регистр

print(msg.lower())# lower - нижний регистр

print(msg2.title())# title - возвращает копию строки,
# в которой каждое новое слово начинается с заглавной буквы
# и продолжается строчными

print(msg.find('o')) # find - поиск, вывод индекса

print(msg.find('Good')) # индекс начала выражения

print(msg.replace('Good luck!', 'How are you?')) # replace - замена




