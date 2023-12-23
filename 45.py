#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
print('==-'*10)
print("JOKENPÔ")
print('==-'*10)

print('\n')
print('*-*-'*10)
itens = (' ','Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3)
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('\nComputador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('*-*-'*10)

if computador==1 and jogador==2:
    print('\nVocê venceu!')
elif jogador==1 and computador==2:
    print('\nO Computador é o vencedor!')
elif computador==jogador:
    print('\nEmpate!')
elif computador==3 and jogador==2:
    print('\nO Computador é o vencedor!')
elif jogador==3 and computador==2:
    print('\nVocê venceu!')
elif computador==1 and jogador==3:
    print('\nO Computador é o vencedor!')
elif jogador==1 and computador==3:
    print('\nVocê venceu!')
else:
    print('\nOpção Inváida.')

n1 = int(input("\n\nDigite um número: "))
print(n1)