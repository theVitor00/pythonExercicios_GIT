# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando...')
print('O seu primeiro nome é: {}'.format(nome.split()[0]))
print('O seu último nome é: {}'.format(nome.split()[-1]))

# outra solução para mostrar o último nome de uma string é usar o .format(variavel[len(variavel) - 1])
