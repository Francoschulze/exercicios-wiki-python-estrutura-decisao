"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

"""

numero = int(input('Digite um número:\n'
                   '1 - Domingo\n'
                   '2 - Segunda\n'
                   '3 - Terça\n'
                   '4 - Quarta\n'
                   '5 - Quinta\n'
                   '6 - Sexta\n'
                   '7 - Sábado\n'
                   'Opção:'))

if numero == 1:
    print('Hoje é Domingo! ')

elif numero == 2:
    print('Hoje é Segunda! ')

elif numero == 3:
    print('Hoje é Terça! ')

elif numero == 4:
    print('Hoje é Quarta! ')

elif numero == 5:
    print('Hoje é Quinta! ')

elif numero == 6:
    print('Hoje é Sexta! ')

elif numero == 7:
    print('Hoje é Sábado! ')

else:
    print('Opção inválida!')
