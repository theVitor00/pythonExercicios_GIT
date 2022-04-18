# FAÇA UM PROGRAMA QUE LEIA A LARGURA E ALTURA DE UMA PAREDE EM METROS. CALCULE A SUA ÁREA E A QUANTIDADE
# DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M QUADRADOS

a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))

area = l * a
litros = area // 2

print('A parede tem uma área total de {:.2f}.'.format(area))
print('Serão necessários {:.2f} litros de tinta para pintá-la'.format(litros))
