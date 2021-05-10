#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
print('Seja bem vindo a calculadora de Alistamento Militar')
anonasc = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade  = atual-anonasc
print('Você tem {} anos'.format(idade))
if idade < 18:
    print('Você ainda Não precisa se alistar no Serviço militar.')
    print('Ainda falta {} anos para o alistamento.'.format(18-idade))
elif idade == 18:
    print('Chegou seu momento de se alistar!')
elif idade > 18:
    print('Você está atrasado {} ano(s) para o alistamento militar. Vá o quanto antes a uma junta de serviço militar!'.format(idade-18))
else:
    print('Tente novamente ocm um valor Valido!')


