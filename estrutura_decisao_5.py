"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a 7,0;
    A mensagem "Reprovado", se a média for menor que 7,0;
    A mensagem "Aprovado com Distinção", se a média for igual a 10,0.
"""

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

# Calculando a média
media = (nota_1 + nota_2) / 2

# Teste lógico para verificar se o valor da média
# é igual a 7 e menor que 10
if 7 <= media < 10:
    print(f'Média {media:.2f} Aprovado! ')
elif media < 7:
    print(f'Média {media:.2f} Reprovado! ')
elif media == 10:
    print(f'Média {media:.2f} Aprovado com distinção! ')
