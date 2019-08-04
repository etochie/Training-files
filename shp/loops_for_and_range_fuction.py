for item in 'Python':
    print (item) # item рассматривается каждая буква, потому что 'Python' - строка

for item in ['Python', 'Java', 'PHP', 'C#']:
    print (item) # item1 рассматривается как целые строки, потому что они помещены в список и разделены запятыми

for item in range(10): # range - ряд
    print(item)
for item in range(5,10): # с 5 до 10
    print(item)
for item in range(5,10,2): # 2 - шаг ряда (выводится 5, 7, 9)
    print(item)
