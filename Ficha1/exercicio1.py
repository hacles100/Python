salario = int(input('Caro colaborador, digite o seu salario:'))

salario1 = 0
salario2 = 0
salario3 = 0
salario4 = 0

if salario <= 18000:
    salario1 = salario * 1.2
    print('O seu salario inicial foi de:', salario)
    print('Sera feito um aumento de 20% no seu salario!')
    print('O seu salario actual e de:', salario1)

elif salario > 18000 and salario <= 27000:
    salario2 = salario * 1.15
    print('O seu salario inicial foi de:', salario)
    print('Sera feito um aumento de 15% no seu salario!')
    print('O seu salario actual e de:', salario2)

elif salario > 27000 and salario <= 45000:
    salario3 = salario * 1.10
    print('O seu salario inicial foi de:', salario)
    print('Sera feito um aumento de 10% no seu salario!')
    print('O seu salario actual e de:', salario3)

else:
    salario4 = salario * 1.05
    print('O seu salario inicial foi de:', salario)
    print('Sera feito um aumento de 5% no seu salario!')
    print('O seu salario actual e de:', salario4)

