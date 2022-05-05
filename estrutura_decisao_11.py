"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""

salario_atual = float(input('Digite seu salário: '))
percentual = int(input('digite o valor percentual de aumento: '))

# Testando a condição e efetuando os cálculos na formatação
if salario_atual < 280:
    print(f'Salário antes do reajuste: R$ {salario_atual:.2f}\n'
          f'Percentual de aumento aplicado: {percentual} %\n'
          f'Valor do aumento: R$ {salario_atual * (percentual / 100):.2f}\n'
          f'Novo salário após aumento: R$ {salario_atual * 1.2:.2f}')
elif 280 < salario_atual < 700:
    print(f'Salário antes do reajuste: R$ {salario_atual:.2f}\n'
          f'Percentual de aumento aplicado: {percentual} %\n'
          f'Valor do aumento: R$ {salario_atual * (percentual / 100):.2f}\n'
          f'Novo salário após aumento: R$ {salario_atual * 1.15:.2f}')
elif 700 < salario_atual < 1500:
    print(f'Salário antes do reajuste: R$ {salario_atual:.2f}\n'
          f'Percentual de aumento aplicado: {percentual} %\n'
          f'Valor do aumento: R$ {salario_atual * (percentual / 100):.2f}\n'
          f'Novo salário após aumento: R$ {salario_atual * 1.1:.2f}')
elif salario_atual > 1500:
    print(f'Salário antes do reajuste: R$ {salario_atual:.2f}\n'
          f'Percentual de aumento aplicado: {percentual} %\n'
          f'Valor do aumento: R$ {salario_atual * (percentual / 100):.2f}\n'
          f'Novo salário após aumento: R$ {salario_atual * 1.05:.2f}')
