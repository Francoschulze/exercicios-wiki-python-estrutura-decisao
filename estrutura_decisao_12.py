"""
Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende
do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%
    Imprima na tela as informações, dispostas conforme o exemplo abaixo.

No exemplo o valor da hora é R$ 5.00 e a quantidade de horas é 220 h.

        Salário Bruto: (5 * 220)        : R$  1100,00
        (-) IR (5%)                     : R$  55,00
        (-) INSS (10%)                  : R$  110,00
        FGTS (11%)                      : R$  121,00
        Sindicato (3%)                  : R$  33,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  902,00
"""

valor_hora = float(input('Qual o valor que você recebe por hora: '))
hora_mes = int(input('digite a quantidade de horas trabalhadas no mês: '))

# Calculando o salário mensal
salario_bruto = valor_hora * hora_mes

# Calculando o valor a ser pago ao inss
# Onde o percentual é de 10% que é o mesmo que 10 / 100 = 0,10
# O mesmo cálculo é utilizado para os outros casos
INSS = salario_bruto * 0.10
FGTS = salario_bruto * 0.11
sindicato = salario_bruto * 0.03

# Aqui testamos as condições conforme os dados digitados.
# Se a condição for aceita em alguma das estruturas abaixo
# Será executada conforme o salário bruto mensal.
if salario_bruto < 900:
    print(f'\t\tSalário Bruto: ({valor_hora} * {hora_mes})\t: R$ {salario_bruto:.2f}')

elif 900 < salario_bruto < 1500:
    IR = salario_bruto * 0.05
    print(f'\t\tSalário Bruto: ({valor_hora} * {hora_mes})\t: R$ {salario_bruto:.2f}\n'
          f'\t\t(-) IR (5%)\t\t\t\t\t: R$ {IR:.2f}\n'
          f'\t\t(-) INSS (10%)\t\t\t\t: R$ {INSS:.2f}\n'
          f'\t\tFGTS (11%)\t\t\t\t\t: R$ {salario_bruto * 0.11:.2f}\n'
          f'\t\tSindicato (3%)\t\t\t\t: R$ {sindicato:.2f}\n'
          f'\t\tTotal de descontos\t\t\t: R$ {IR + INSS + sindicato:.2f}\n'
          f'\t\tSalário líquido\t\t\t\t: R$ {salario_bruto - IR - INSS - sindicato:.2f}')

elif 1500 < salario_bruto < 2500:
    IR = salario_bruto * 0.10
    print(f'\t\tSalário Bruto: ({valor_hora} * {hora_mes})\t: R$ {salario_bruto:.2f}\n'
          f'\t\t(-) IR (10%)\t\t\t\t: R$ {IR:.2f}\n'
          f'\t\t(-) INSS (10%)\t\t\t\t: R$ {INSS:.2f}\n'
          f'\t\tFGTS (11%)\t\t\t\t\t: R$ {salario_bruto * 0.11:.2f}\n'
          f'\t\tSindicato (3%)\t\t\t\t: R$ {sindicato:.2f}\n'
          f'\t\tTotal de descontos\t\t\t: R$ {IR + INSS + sindicato:.2f}\n'
          f'\t\tSalário líquido\t\t\t\t: R$ {salario_bruto - IR - INSS - sindicato:.2f}')

elif salario_bruto > 2500:
    IR = salario_bruto * 0.20
    print(f'\t\tSalário Bruto: ({valor_hora} * {hora_mes})\t: R$ {salario_bruto:.2f}\n'
          f'\t\t(-) IR (20%)\t\t\t\t: R$ {IR:.2f}\n'
          f'\t\t(-) INSS (10%)\t\t\t\t: R$ {INSS:.2f}\n'
          f'\t\tFGTS (11%)\t\t\t\t\t: R$ {salario_bruto * 0.11:.2f}\n'
          f'\t\tSindicato (3%)\t\t\t\t: R$ {sindicato:.2f}\n'
          f'\t\tTotal de descontos\t\t\t: R$ {IR + INSS + sindicato:.2f}\n'
          f'\t\tSalário líquido\t\t\t\t: R$ {salario_bruto - IR - INSS - sindicato:.2f}')
