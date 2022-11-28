def powersum(power, *args):
    '''Возвращает сумму аргументов, возведенных в указанную степень.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

