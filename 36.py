#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele 
#vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do 
#salário, ou então, o empréstimo será negado.

print("Aprovador de Empréstimos\n")
casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Digite o valor do seu salário: R$"))
anos = float(input("Digite a quantidade de anos que vai pagar: "))
prest_mensal = casa/ (anos*12)

if prest_mensal > (salario*0.3):
	print("\nA prestação, em {} anos, terá o valor de {}. \nEmpréstimo NEGADO \nExcedeu 30% do seu salário!".format(anos, prest_mensal))
else:
	print("\nEmpréstimo APROVADO!")
print("\nOperação finalizada.")

n1 = int(input("\n\nDigite um número: "))
print(n1)