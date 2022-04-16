# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSIVES
# SOBRE ELE

x = input('Digite algo: ')
print('\nO VALOR DIGITADO FOI - {}.\n'.format(x))
print('{}'.format('-' * 40))

print('É Alfanumérico? - {}'.format(x.isalnum()))
print('É Alfabético? - {}'.format(x.isalpha()))
print('É ASCII? - {}'.format(x.isascii()))
print('É Dígito? - {}'.format(x.isdigit()))
print('É Minúsculo - {}'.format(x.islower()))
print('É Decimal? - {}'.format(x.isdecimal()))
print('É Identificador? - {}'.format(x.isidentifier()))
print('É Numérico? - {}'.format(x.isnumeric()))
print('É "Imprimível"? - {}'.format(x.isprintable()))
print('É Espaço? - {}'.format(x.isspace()))
print('É Título - {}'.format(x.istitle()))
print('É Maiúsculo? - {}'.format(x.isupper()))