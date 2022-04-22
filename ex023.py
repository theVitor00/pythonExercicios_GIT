# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS.
# EX: 1834
# UNIDADE: 4
# DEZENA: 3
# CENTENA: 8
# MILHAR: 1

num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 1000

print('Analisando o número {} ...'.format(num))
print('UNIDADE: {}'.format(u))
print('DEZENA: {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR: {}'.format(m))





