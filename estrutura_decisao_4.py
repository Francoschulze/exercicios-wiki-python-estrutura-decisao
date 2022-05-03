"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input('Digite uma letra: ')

vogais = 'AaEeIiOoUu'
consoantes = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'

if letra in vogais:
    print('A letra digitada foi uma vogal! ')
elif letra in consoantes:
    print('A letra digitada foi uma consoante! ')
else:
    print('Opção inválida! ')