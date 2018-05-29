def add(x, y):
    '''add func'''
    return x + y

def subtract(x, y):
    '''subtract func'''
    return x - y

def multiply(x, y):
    '''multuply func'''
    return x * y

def divide(x, y):
    '''divide func'''
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y
