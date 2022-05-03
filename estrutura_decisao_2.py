"""
Faça um Programa que peça um valor
e mostre na tela se o valor é positivo ou negativo.
"""

valor = int(input('Digite um número: '))

if valor > 0:
    print(f'O valor digitado foi {valor} esse número é positivo! ')
elif valor == 0:
    print(f'O valor digitado foi {valor} esse número é neutro! ')
elif valor < 0:
    print(f'O valor digitado foi {valor} esse número é negativo! ')
else:
    print('Opção inválida! ')

