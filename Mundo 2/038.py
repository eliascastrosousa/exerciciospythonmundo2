# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
from time import sleep

print('Bem vindo ao comparador de numeros! ')
sleep(1)
n1 = int(input('Digite um numero inteiro: '))
sleep(0.5)
n2 = int(input('Digite outro numero inteiro: '))
sleep(0.5)
print('Verificando...')
sleep(1)
if n1 > n2:
    print('O numero {} é maior que o numero {} digitado posteriormente.'.format(n1,n2))
elif n1 < n2:
    print('O numero {} é menor que o numero {} digitado posteriormente.'.format(n1,n2))
else:
    print('O numero {} é igual ao numero {} digitado posteriormente.'.format(n1,n2))