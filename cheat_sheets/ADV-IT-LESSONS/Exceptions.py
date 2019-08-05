import sys

filename = 'namelist.txt'

while True:
    try:
        print('TRY')
        myfile = open(filename, mode='r')
    except Exception:
        print('EXCEPT')
        print('Error found!')
        filename = input('Enter correct file name: ')
    else:
        print('ELSE')
        for line in myfile:
            print(line.strip())
        sys.exit()


