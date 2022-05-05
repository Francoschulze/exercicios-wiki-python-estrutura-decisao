"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
ou "Valor Inválido!", conforme o caso.
"""

# \t dá uma identação na string
print('\t\t\tQual período você estuda? ')
turno = input('Digite M para matutino, V para vespertino ou N para noturno: ')

# Procurando valor digitado
if turno in 'Mm':
    print('Período matutino! ')
elif turno in 'Vv':
    print('Período vespertino! ')
elif turno in 'Nn':
    print('Período noturno! ')
else:
    print('Opção inválida! ')
