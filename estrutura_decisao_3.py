"""
Faça um Programa que verifique se uma letra digitada é
"F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

letra = input('Digite a letra F para feminino ou M para masculino: ')

if letra in 'Mm':
    print(f'Você digitou a letra {letra} é masculino! ')
elif letra in 'Ff':
    print(F'Você digitou a letra {letra} é feminino! ')
else:
    print('Opção inválida! Digite [F] ou [M]. ')
