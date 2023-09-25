# Процедурная парадигма - есть процедура, удобная для повторного использования
# Структурная - нет goto, вся программа в рамках трех управляющих конструкций

def mult(num):
    for i in range(1, num + 1):
        for j in range(1, 11):
            print(f'{j} * {i} = {j * i}', end='\t\t')
        print()


num = int(input('Введите число (1..10): '))

if num > 10:
    print('Число больше 10')
elif num < 1:
    print('Число меньше 1')
else:
    mult(num)

