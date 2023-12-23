#	Crie um programa que elia duas notas de um aluno e calcule sua média, mostrando
#	uma mensagem no final, de acordo com a média atingida:
#	- Média abaixo de 5.0: REPROVADO
#	- Média entre 5.0 e 6.9: RECUPERAÇÃO
#	- Média 7.0 ou superior: APROVADO

print("Calculadora de Médias!\n")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1+nota2)/2

if media<5:
    print("\nREPROVADO!")
elif media>=5 and media<=6.9:
    print("\nRECUPERAÇÃO!")
else:
    print("\nAPROVADO!")
print("\nOperação finalizada!")

n1 = int(input("\n\nDigite um número: "))
print(n1)