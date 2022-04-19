# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SEU SENO, COSSENO E TANGENTE

from math import sin, cos, tan, radians

angulo = int(input('Digite o valor do ângulo a ser analisado: '))
print('-' * 41)
print('==== Analisando o ângulo de {} graus ===='.format(angulo))
print('SENO: {:.2f}'.format(sin(radians(angulo))))
print('COSSENO: {:.2f}'.format(cos(radians(angulo))))
print('TANGENTE: {:.2f}'.format(tan(radians(angulo))))
print('-' * 41)
