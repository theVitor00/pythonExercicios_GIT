# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOESTRE:
# >> QUANTAS VEZES APARECE A LETRA 'A'
# >> EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ (FIND)
# >> EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

frase = str(input('Digite uma frase: ')).upper().strip()
print('Analisando...')
print('A letra \'A\' aparece {} vezes nessa frase.'.format(frase.count('A')))
print('Ela aparece pela primeira vez na posição {}.'.format(frase.find('A') + 1))
print('E aparece pela última vez na posição {}.'.format(frase.rfind('A') + 1))




