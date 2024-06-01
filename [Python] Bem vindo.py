# Seja bem vindo!
print('Olá, visitante!')
nome = str(input('Qual o seu nome ou apelido?'))
idade = int(input('Qual a sua idade?'))
teste = str(input('Você é programador?'))

if teste == 'sim' or teste == 's' or teste == 'SIM' or  teste =='S':
    prog = str(input('Qual linguagem de programação está aprendendo?'))
    print('Bem vindo programador!')
    print(f'Seja bem vindo, {nome}. Atualmente voce está com {idade} anos! Aprender uma nova linguagem de programação nunca é uma atividade simples, inclusive te desejo uma boa sorte no aprendizado da linguagem {prog}! Fico feliz por você ter aberto esse programa, é um programa simples feito em Python!')
    print('Boa sorte na sua jornada! Obrigado por participar! Bora aprender juntos, fique a vontade para mandar mensagem e seguir nas redes sociais!')
else:
    print('Bem vindo visitante!')
    print(f'Seja bem vindo, {nome}. Atualmente voce está com {idade} anos! Aprender uma nova linguagem de programação nunca é uma atividade simples, inclusive te convido a conhecer esse mundo incrível que está cada vez mais presente no dia a dia. Não é necessário ser excelente em matemática para começar a programar! Basta começar a praticar e ser consistente nos estudos que aos poucos os resultados aparecem!')
    print('Boa sorte na sua jornada! Obrigado por participar! Bora aprender juntos, fique a vontade para mandar mensagem e seguir nas redes sociais!')
