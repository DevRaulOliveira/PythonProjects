# Calculadora básica

import os
os.system('cls') or None

print('Bem vindo ao programa, calculadora básica!')

while True:
    try:
        x = float(input('Insira o primeiro numero: '))
        break  
    except ValueError:
        print('Por favor, insira um número válido.')

while True:
    try:
        y = float(input('Insira o segundo numero: '))
        break  
    except ValueError:
        print('Por favor, insira um número válido.')

while True:
    op = input('Qual operação matemática deseja realizar? (+, -, *, /) ')
    if op in ['+', '-', '*', '/']:
        break 
    else:
        print('Operação inválida. Por favor, insira uma operação válida.')

try:
    if op == '+':
        print('O resultado da soma é:\n', (x + y))
    elif op == '-':
        print('O resultado da subtração é:\n', (x - y))
    elif op == '*':
        print('O resultado da multiplicação é:\n', (x * y))
    elif op == '/':
        if y != 0:
            print('O resultado da divisão é:\n', (x / y))
        else:
            print('Divisão por zero não é permitida.')
except Exception as e:
    print('Ocorreu um erro:', e)

print('\nObrigado por utilizar o programa!\n')