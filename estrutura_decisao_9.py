"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.

Obs.: Lembrando que o exercício é para treinar sua lógica com o que você
aprendeu até o momento. Não busque por soluções mirabolantes, use o conhecimento
atual. Mais para frente você será capaz de utilizar códigos melhores.
"""

num_1 = 20
num_2 = 10
num_3 = 30

print(f'{num_1}, {num_2} e {num_3} ')

if num_3 > num_2:
    auxiliar = num_3
    num_3 = num_2
    num_2 = auxiliar

if num_2 > num_1:
    auxiliar = num_2
    num_2 = num_1
    num_1 = auxiliar

if num_3 > num_2:
    auxiliar = num_3
    num_3 = num_2
    num_2 = auxiliar

print(f'Ordem decrescente: {num_1}, {num_2} e {num_3}! ')
