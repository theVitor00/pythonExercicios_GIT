# UM PROFESSOR QUER SORTEAR UM DE SEUS 4 ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRMA QUE AJUDE ELE LENDO O NOME DOS
# ALUNOS E SORTEANDO O ESCOLHIDO

from random import choice

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
alunos = [a1, a2, a3, a4]

print('O aluno sorteado foi : {}'.format(choice(alunos)))



