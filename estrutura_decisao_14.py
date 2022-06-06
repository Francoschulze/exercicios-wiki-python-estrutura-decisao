"""Faça um programa que lê as duas notas parciais obtidas
por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
"""

nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))

media = (nota_1 + nota_2) / 2

if media > 9:
    print(f'Parabéns, sua média foi: {media:.2f} e você tirou um A. ')
elif 7.5 <= media < 9:
    print(f'Sua média foi: {media:.2f} e você tirou um B. ')
elif 6 <= media < 7.5:
    print(f'Sua média foi: {media:.2f} e você tirou um C. ')
elif 4 <= media < 6:
    print(f'Sua média foi: {media:.2f} e você tirou um D. ')
elif media < 4 or media == 0:
    print(f'Sua média foi: {media:.2f} e você tirou um E. ')
else:
    print('Digite apenas números.')
