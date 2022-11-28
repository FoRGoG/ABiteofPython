poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей веселый тон -
           используюй Python!
'''

f = open('../exeptions/poem.txt', 'w') # открываем для записи (writing)
f.write(poem) # записываем текст в файл
f.close() # закрываем файл

f = open('../exeptions/poem.txt') # если не указан режим, по умолчанию
# подразумевается режим чтения ('r'eading)
while True:
    line = f.readline()
    if len(line) == 0: # Нулевая длина обозначает конец файла (E0F)
        break
    print(line, end='')

f.close() # закрываем файл