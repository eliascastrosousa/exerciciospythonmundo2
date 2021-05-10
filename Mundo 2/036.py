# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.

from time import sleep
print('Bem vindo a Calculadora de emprestimo bancario!')
sleep(1)
valor = float(input('Digite o valor do imovel que deseja financiar (sem pontuação): '))
sleep(1)
salario = float(input('Digite qual o seu salario (sem pontuação): '))
sleep(1)
anos = float(input('Digite a quantidade de anos que deseja pagar o imovel: '))
print('Você deseja financiar {} Reais, seu salario é de {} Reais e Deseja pagar em {:.0f} anos.'.format(valor,salario,anos))
sleep(1)
print('Analisando...')
sleep(1)
mensalidade = (valor/anos)/12
limite = salario*1.3-salario

sleep(1)
if (mensalidade <= limite):
    print('Seu credito foi aprovado! Suas parcelas serão de R${:.2f} ao mês.'.format(mensalidade))
else:
    print('Infelizmente seu credito não foi aprovado pois as mensalidades ultrapassam seu limite pré aprovado.')
    print(' (R${:.2f}) ao mês.'.format(limite))