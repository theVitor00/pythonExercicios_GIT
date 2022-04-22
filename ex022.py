# CONSTRUA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# >> O NOME COM TODAS AS LETRAS MAIÚSCULAS
# >> QUANTAS LETRAS TEM NO TOTAL, SEM CONSIDERAR OS ESPAÇOS
# >> QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Qual é o seu nome completo: '))
print('\nAnalisando seu nome...')
print('{}'.format(nome.upper()))
print('{}'.format(nome.lower()))
#espaco = nome.count(' ')
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
nome = nome.split()
print('Seu primeiro nome possui {} letras.'.format(len(nome[0])))


