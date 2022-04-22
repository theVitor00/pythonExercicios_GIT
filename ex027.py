# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE

nome = str(input('Digite seu nome completo: '))
print('Analisando...')
print('O seu primeiro nome é: {}'.format(nome.split()[0]))
print('O seu último nome é: {}'.format(nome.split()[-1]))
