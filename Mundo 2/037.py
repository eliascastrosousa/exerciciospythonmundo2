#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
from time import sleep
import math
print('Bem vindo ao seu conversor de bases numericas!')
sleep(1)
n = int(input('Digite um numero inteiro que deseja converter: '))
binario = bin(n)
octal = oct(n)
hexadecimal = hex(n)

print('''Você deseja converter em
1 - Binario
2 - Octal
3 - Hexadeximal
''')
conversao = int(input('Digite aqui: '))
if conversao == 1:
    print('O numero {}, convertido em binario fica {}.'.format(n,binario[2:]))
elif conversao == 2:
    print('O numero {}, convertido em octal fica {}.'.format(n,octal[2:]))
elif conversao == 3:
    print('O numero {}, convertido em hexadecimal fica {}.'.format(n,hexadecimal[2:]))
else:
    print('Tente novamente com um numero valido.')