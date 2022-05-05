"""
Faça um programa que pergunte o preço de três produtos
e informe qual produto deverá comprar, sabendo que a
decisão é sempre pelo mais barato.
"""

produto_1 = float(input('Digite o valor do primeiro produto: '))
produto_2 = float(input('Digite o valor do segundo produto: '))
produto_3 = float(input('Digite o valor do terceiro produto: '))

if produto_1 < produto_2 and produto_1 < produto_3:
    print(f'O produto de valor: R$ {produto_1:.2f} é o mais barato! ')
elif produto_2 < produto_1 and produto_2 < produto_3:
    print(f'O produto de valor: R$ {produto_2:.2f} é o mais barato! ')
elif produto_3 < produto_1 and produto_3 < produto_2:
    print(f'O produto de valor: R$ {produto_3:.2f} é o mais barato! ')
