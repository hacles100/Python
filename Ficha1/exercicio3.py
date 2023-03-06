lado1 = int(input('Insira o primeiro lado do triangulo: '))
lado2 = int(input('Insira o segundo lado do triangulo: '))
lado3 = int(input('Insira o terceiro lado do triangulo: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Esses valores forma um triangulo!')

    if lado1 == lado2 == lado3:
        print('Triangulo Equilatero!') 

    elif lado1 != lado2 != lado3:
        print('Triagulo Escaleno!')
        
    else:
        print('Triangulo Isosceles!')

else:
    print('Nao e um triangulo!')