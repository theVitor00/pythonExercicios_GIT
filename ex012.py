# FAÇA UM PROGRAMA QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE O SEU NOVO PREÇO COM 5% DE DESCONTO

preco = float(input('Digite o valor líquido do produto: '))
valor_final = preco - (preco * (5/100))

print('O produto custa R${:.2f}, mas com o desconto de 5% fica R${:.2f}'.format(preco, valor_final))
