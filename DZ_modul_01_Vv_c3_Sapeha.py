'''Задание 1
Пользователь вводит с клавиатуры три цифры. Необходимо создать число, содержащее эти цифры.
Например, если с клавиатуры введено 1, 5, 7, тогда нужно сформировать число 157.'''

# x=int(input('Введите первую цифру'))
# y=int(input('Введите вторую цифру'))
# z=int(input('Введите третью цифру'))
# print('Вы получаете число', (x),(y),(z))

'''Задание 2
Пользователь вводит с клавиатуры число, состоящее 
из четырех цифр. Требуется найти произведение цифр. 
Например, если с клавиатуры введено 1324, тогда результат произведения 1*3*2*4 = 24.'''

# n=int(input('Введите число состоящее из четырех цифр  '))
# a=int(n//1000)
# b=int(n//100%10)
# c=int(n//10%10)
# d=int(n%10)
# print('Произведение цифр:', d*c*b*a)

'''Задание 3
Пользователь вводит с клавиатуры количество метров. 
Требуется вывести результат перевода метров в сантиметры, дециметры, миллиметры, мили.'''

# x=int(input('Введите количество метров'))
# print('Сантиметры',(x*100))
# print('Дациметры',(x*10))
# print('Миллиметры',(x*1000))
# print('Мили',(x*0.000621))

'''Задание 4
Напишите программу, вычисляющую площадь треугольника. Пользователь с клавиатуры вводит размер 
основания треугольника и размер высоты.'''

# a=int(input("Введите размер основания треугольника"))
# h=int(input('Введите размер высоты треугольника'))
# S=1/2*a*h
# print('Площадь треугольника',S,'м2')

'''Задание 5
Пользователь с клавиатуры вводит четырёхзначное 
число. Необходимо перевернуть число и отобразить 
результат. Например, если введено 4512, результат 2154'''

# n=int(input('Введите число состоящее из четырех цифр  '))
# a=str(n//1000)
# b=str(n//100%10)
# c=str(n//10%10)
# d=str(n%10)
# print('Результат:', d+c+b+a)
