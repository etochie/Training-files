print('''Hello, user!
This is a new car game!
Write help for command list''')
command = ''
started = False
while True: # while True - зацикливает блок, пока не break
    command = input('> ').lower()
    if command == 'help':
        print('''start - to start car
stop - to stop car
quit -  to exit''')
    elif command == 'start':
        if started: #if и так проверяет на наличие True. if started = True - ошибка
            print('Car is already started, what are you doing?')
        else:
            started = True
            print('Car started!')
    elif command == 'stop':
        if not started: # в этом примере лучше обойтись без переменной stopped (только started), потому что при запуске игры машина и так стоит на месте
            print('Car is already staopped, what are you doing?')
        else:
            started = False
            print('Car stopped!')
    elif command == 'quit':
        break
    else:
        print("I don't underastand...")





    #really = input('Really exit? (Y/N)')
    #if really.upper() == 'Y'
    #    break
    #elif really.upper() == 'N'
