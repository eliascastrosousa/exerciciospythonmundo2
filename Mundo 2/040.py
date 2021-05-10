#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
# mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('Infelizmente sua nota final foi {} e você foi reprovado.'.format(media))
elif media <= 6.9:
    print('Você obteve nota {} e está em Recuperação!'.format(media))
elif media >= 7:
    print('Parabens, sua nota final é {} e você foi aprovado!'.format(media))
elif media >10:
    print('Tente novamente com um valor valido!'.format(media))
else:
    print('Tente novamente com um valor valido!'.format(media))
