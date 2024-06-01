# Calcula variação percentual
import os
os.system('cls') or None

print('Bem vindo ao programa, Calculo de variação percentual')
while True:
    i = int(input('Digite o valor inicial: '))
    if i > 0:
        break

print()

while True:
    z = int(input('Digite o valor final: '))
    if z >= 0:
        break
j = z - i
y = (abs(j)/i)*100

if j < 0:
    print('A variação percentual foi de:-{}',y,'%')
else:
    print('A variação percentual foi de +',y,'%')
print('Obrigado pelo acesso!')