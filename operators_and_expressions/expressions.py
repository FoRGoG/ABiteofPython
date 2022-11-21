# length = 5
# breadth = 2
#
# area = length * breadth
# print('Площадь равна', area)
# print('Периметр равен', 2 * (length + breadth))

number = 23
guess = int(input('Введите целое число: '))

if guess == number:
    print('Поздравляю, вы угадали')
elif guess < number:
    print('Нет, число больше этого.')
else:
    print('Нет, загаданное число немного меньше этого.')