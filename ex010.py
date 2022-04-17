# ESCREVA CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES PODE COMPRAR
# DÓLAR = 3.27R$

dinheiro = float(input('Quanto dinheiro você tem na carteira: R$ '))
print('Com R${:.2f} é possível comprar US${:.2f}'.format(dinheiro, dinheiro / 3.27))
