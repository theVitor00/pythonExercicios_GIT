# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDO POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS
# QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0.15 POR KM RODADO.

print('-' * 55)
km = float(input('Quantos quilômetros foram percorridos com o carro: '))
dias = int(input('Por quantos dias ele foi alugado: '))

total = (dias * 60) + (km * 0.15)

print('Você andou {}Km em {} dias.'.format(km, dias))
print('TOTAL A PAGAR: {:.2f}R$'.format(total))
print('-' * 55)


