#Calculadora
#Criar uma funcao reguladora. Exemplo. Funcao_reguladora = 0 ate 3, if menu == 0
#Funcao soma -> ira soma a + b / a funcao subtacao a -b , a multiplicacao seria um pelo outro e a divisao a pelo b.
print('Bem vindo,bem vinda. Voce esta acessando uma calculadora na versao beta 0.1.0.''\n''Bugs podem acontecer')
print('Para usar a calculadora, digite o valor reference ao calculo''\n''0 - para soma ''\n''1 - para subracao''\n''2 - para multiplicacao''\n''3 - para divisao')
menu = int(input())
print('Muito bem, opcao {}.'.format(menu))

while menu >=0 and menu <=3:
    while menu == 0:
        a = float(input('Digite o primeiro valor para a soma: '))
        b = float(input('Digite o segundo valor para a soma: '))
        print('O valor da soma e de :{:.2f}''\n'.format(a+b))
        print('Para usar a calculadora, digite o valor referente ao calculo''\n''0 - para soma ''\n''1 - para subracao''\n''2 - para multiplicacao''\n''3 - para divisao')
        menu = int(input())
        print('Muito bem, opcao {}.'.format(menu))
    while menu == 1:
        a = float(input('Digite o primeiro valor para a subtracao: '))
        b = float(input('Digite o segundo valor para a subtrair do primeiro valor: '))
        print('O valor da subtracao e de :{:.2f}''\n'.format(a-b))
        print('Para usar a calculadora, digite o valor referente ao calculo''\n''0 - para soma ''\n''1 - para subracao''\n''2 - para multiplicacao''\n''3 - para divisao')
        menu = int(input())
        print('Muito bem, opcao {}.'.format(menu))
    while menu == 2:
        a = float(input('Digite o primeiro valor para a multiplicacao: '))
        b = float(input('Digite o segundo valor para multiplicar pelo primeiro: '))
        print('O valor da multiplicacao e de :{:.2f}''\n'.format(a*b))
        print('Para usar a calculadora, digite o valor referente ao calculo''\n''0 - para soma ''\n''1 - para subracao''\n''2 - para multiplicacao''\n''3 - para divisao')
        menu = int(input())
        print('Muito bem, opcao {}.'.format(menu))
    while menu == 3:
        a = float(input('Digite o primeiro valor para a divisao: '))
        b = float(input('Digite o segundo valor para dividir pelo primeiro: '))
        print('O valor da divisao e de :{:.2f}''\n'.format(a/b))
        print('Para usar a calculadora, digite o valor referente ao calculo''\n''0 - para soma ''\n''1 - para subracao''\n''2 - para multiplicacao''\n''3 - para divisao')
        menu = int(input())
        print('Muito bem, opcao {}.'.format(menu))
