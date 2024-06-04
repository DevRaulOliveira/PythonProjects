import random

print('Bem vindo ao jogo de Pedra, Papel e Tesoura!\n')
def jogar():
    i = input('Escolha "r" para pedra, "p" para papel, "t" para tesoura: ')
    x = random.choice(['r','p','s'])

    if i == x:
        return '\nEmpate\n'
    if w(i,x):
        return '\nVocê venceu!! Parabéns!!!\n'
    
    return '\nO Computador venceu =(\nTente novamente!\n'

def w(j,n):
    if (j == 'r' and n == 'p') or ( j == 'p' and n == 'r') or ( j == 's' and n == 'p'):
        return True
print(jogar())

print('Obrigado por jogar!')