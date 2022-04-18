# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA EM .C PARA .F

celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * (9 / 5) + 32)

print('{:.1f} graus Celsius equivale a {:.1f} graus Fahrenheit'.format(celsius, fahrenheit))
