valorA = float(input('Insira o valor de A:'))

if valorA == 0:
    print('A equacao nao e do segundo grau!')
    exit()

valorB = float(input('Insira o valor de B:'))
valorC = float(input('Insira o valor de C:'))

delta = valorB*valorB - 4 * valorA * valorC

if delta < 0:
    print('O valor do delta e negativo!')
    exit()
