#Crie um programa que leie o ano de nascimento
# de sete pessoas. No final, mostre quantas pessoas ainda não
#atingiram a maioridade e quantas já são maiores.
from time import sleep
contador = 0
for pessoas in range(7):
    ano_nasc = int(input("Digite o ano que você nasceu: "))
    idade = 2023 - ano_nasc
    if idade < 18:
        contador = contador+1
print("A quantidade de pessoas que não atngiram a maior idade é :", contador)
sleep(5)