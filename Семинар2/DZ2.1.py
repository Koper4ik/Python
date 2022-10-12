x = input('Введите число ')

def summa(x):                            #Функция нахождения суммы чисел в заданном числе
    if float(x) < 0:                            #Проверка на знак перед числом
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма чисел равна {summa(x)}')