# Bem vindo ao jogo cara, ou coroa!
import random
print('Bem vindo ao jogo cara ou coroa!!\n')

a = str(input('Escolha "cara" ou "coroa":'))
i = random.choice(['cara','coroa'])

if a==i:
    print('\nVoce venceu!')
else:
    print('\nVocê perdeu, tente novamente!')
print('\nObrigado por utilizar o programa!')