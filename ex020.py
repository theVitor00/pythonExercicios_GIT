# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DA APRESENTAÇÃO DE TRABALHO DOS ALUNOS. FAÇA UM PROGRAMA
# QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.

from random import shuffle

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

alunos = [a1, a2, a3, a4]
shuffle(alunos)

print('A ordem de apresentação dos alunos será: {}'.format(alunos))
