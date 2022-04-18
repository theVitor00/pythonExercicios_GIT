# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO COM 15% DE AUMENTO

sal_base = float(input('Digite o salário do funcionário: R$'))
sal_novo = sal_base + (sal_base * (15/100))

print('O funcionário recebia R${:.2f}, mas com o aumento de 15%, passará a receber R${:.2f}'.format(sal_base, sal_novo))
