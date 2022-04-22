# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM A PALAVRA 'SANTO'

cidade = str(input('Digite o nome de uma cidade: '))
cidade = cidade.split()
print('A cidade começa com o nome \'Santo\'? - {}'.format('Santo' in cidade[0]))
