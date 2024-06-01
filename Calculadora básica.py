# Calculadora

print('Bem vindo ao programa, calculadora básica!')
x = float(input('Insira o primeiro numero:'))  
y = float(input('Insira o segundo numero: '))
op = input('Qual operação matematica deseja realizar? ').lower()

while True:
    try:
        if op == '+' or op == 'soma' or op == 'som' or op == 'sum' or op == 'adc' or op =='adição' or op =='adicao':
            print('O resultado da soma é:\n', (x+y))
            break
        if op == '-' or op == 'sub' or op =='subtração' or op == 'menos' or op =='minus':
            print('O resultado da subtração é:\n',(x-y))
            break
        if op == '*' or op == 'mult' or op == 'multiplicacao' or op == 'vezes' or op =='x':
            print('O resultado da multiplicação é:\n',(x*y))
            break
        if op == '/' or op == 'div' or op =='divide' or op == 'divisao' or op == 'divisão':
            print('O resultado da divisão é:\n',(x/y))
            break
    except ZeroDivisionError:
        print('Divisão por 0 não é permitida. Reinicie o programa')
        break
    except ValueError:
        print('Digito inválido, tente novamente. Reinicie o programa.')
        break
    except Exception:
        print('Erro, reinicie o programa')
        
print('\nObrigado por utilizar o programa!\n')
