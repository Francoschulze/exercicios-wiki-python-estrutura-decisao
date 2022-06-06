"""Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem formar um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Condição de existência:
        a + b > c
        b + c > a
        a + c > b
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

lado_A = int(input('Digite o lado A do triangulo: '))
lado_B = int(input('Digite o lado B do triângulo: '))
lado_C = int(input('Digite o lado C do triângulo:'))

if lado_A + lado_B > lado_C and lado_B + lado_C > lado_A and lado_A + lado_C > lado_B:
    if lado_A == lado_B and lado_A == lado_C:
        print('Triângulo Equilátero! ')
    elif lado_A == lado_B or lado_A == lado_C or lado_B == lado_C:
        print('Triângulo Isósceles! ')
    else:
        print('Triângulo Escaleno! ')
else:
    print('Dados inválidos ou as medidas não podem formar um triângulo! ')
