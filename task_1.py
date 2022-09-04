while True:
    number_day = int(input('Введите число от 1 до 7: '))
    if number_day <= 5:
        print('Не выходной')
        break
    elif number_day < 8:
        print('Выходной')
        break
