#"""Escreva um programa que leia dois número inteiros e compare-os,
#mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor pe maior
#- Não existe valor maior, os dois são iguais"""

print("Identificando Números!\n")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num1>num2:
	print("\nO primeiro valor é maior!")
elif num2>num1:
	print("\nO segundo valor é maior!")
else:
	print("Não existe número maior, os dois são iguais!")
print("\nOperação finalizada!")

n1 = int(input("\n\nDigite um número: "))
print(n1)