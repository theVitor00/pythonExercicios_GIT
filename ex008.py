# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA EM CENTÍMETROS E EM MILÍMETROS

num = int(input('Digite um valor em metros: '))
print('{} em Metros equivale a {}cm e a {}mm.'.format(num, num * 100, num * 1000))