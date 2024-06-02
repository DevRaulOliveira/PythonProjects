import random
print('Bem vindo ao jogo, adivinhe o numero!')
def num(x):
    num_x = random.randint(1,x)
    num_y = 0
    while num_y != num_x:
        num_y = int(input(f'Adivinhe o numero de 0 a {x}: '))
        if num_y < num_x:
            print('Desculpe, tente de novo. Numero muito baixo.')
        elif num_y>num_x:
            print('Desculpe, tente de novo. Numero muito alto.')
    print('Parabéns, voce acertou!')

num(10)