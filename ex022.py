# CONSTRUA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# >> O NOME COM TODAS AS LETRAS MAIÚSCULAS
# >> QUANTAS LETRAS TEM NO TOTAL, SEM CONSIDERAR OS ESPAÇOS
# >> QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Qual é o seu nome completo: '))
print('\nAnalisando seu nome...')
print('{}'.format(nome.upper()))
espaco = nome.count(' ')
print('Seu nome tem {} letras.'.format(nome.count(0, -1) - espaco))
