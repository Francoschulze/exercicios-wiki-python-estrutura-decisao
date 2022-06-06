"""
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax² + bx + c. O programa deverá pedir os valores de a, b e c e
fazer as consistências, informando ao usuário nas seguintes situações:

    -Se o usuário informar o valor de A igual a zero, a equação não é
    do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    -Se o delta calculado for negativo, a equação não possui raizes reais.
    Informe ao usuário e encerre o programa;
    -Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
    informe-a ao usuário;
    -Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""

a = float(input('Digite o valor correspondente ao A: '))
a = a ** 2
delta = 0
x1 = 0
x2 = 0

if a == 0:
    print('A equação não é do segundo grau! ')
elif a != 0:
    b = float(input('Digite o valor correspondente ao B: '))
    c = float(input('Digite 0 valor correspondente ao C: '))

    delta = b ** 2 - 4 * a * c

    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    if delta < 0:
        print('A equação não possui raízes reais! ')
if delta == 0:
    print('A equação possui apenas uma raíz real! ')
elif delta > 0:
    print(f"A equação possui duas raízes reais:\n"
          f"x'= {x1:.1f} e x''= {x2:.1f}")
