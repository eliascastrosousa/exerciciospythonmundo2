#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
anonasc = int(input('Digite o ano do nascimento: '))
atual = date.today().year
idade = (atual-anonasc)

if idade <0:
    print('Tente novamente com um valor valido!')
elif idade >= 0 and idade <= 9:
    print('Você tem {} anos e sua Categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e sua Categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e sua Categoria é JÚNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e sua Categoria é SÊNIOR'.format(idade))
elif idade > 25 and idade <= 120:
    print('Você tem {} anos e sua Categoria é MASTER'.format(idade))
else:
    print('Tente novamente com um valor valido!')