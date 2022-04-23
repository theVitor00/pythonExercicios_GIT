# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM 'SILVA' NO NOME

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando...')
print('Contém \'Silva\' no nome: {}'.format('SILVA' in nome.upper()))

