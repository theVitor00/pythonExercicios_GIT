# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA EM CENTÍMETROS E EM MILÍMETROS

num = float(input('Digite um valor em metros: '))
dm = num * 10
cm = num * 100
mm = num * 1000
dam = num / 10
hm = num / 100
km = num / 1000



print('{} em Metros equivale a {}Dm, {}Cm e a {}Mm, '.format(num, dm, cm, mm))
print('{}Dam, {}Hm e {}Km'.format(dam, hm, km))
