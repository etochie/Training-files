inputfile = "password_list.txt"

name_file = open(inputfile, mode='r', encoding='latin_1')

for num, line in enumerate(name_file, 1):
    if 'yura' in line:
        print(str(num) + ' ' + line.strip())
