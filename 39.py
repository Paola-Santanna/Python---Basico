#	Faça um programa que leie o ano de nascimento de um jovem e informe,
#	de acordo com a sua idade:
#	- Se ele ainda vai se alistar no serviço militar
#	- Se é a hora de se alistar
#	- Se já passou do tempo do alistamento.
#		Seu programa também deverá mostrar o tempo que passou ou que falta para o prazo

from datetime import date

print("Alistamento Militar!\n")
ano = int(input("Digite o ano do seu nascimento: "))
atual = date.today().year
idade = atual - ano
alistamento = ano + 18

if idade<18:
	falta = 18-idade
	if falta>1:
		print("\nFaltam {f} anos para o seu alisamento!".format(f=falta))
        print("Você se alistará no ano de {s}".format(s=alistamento))
	else:
		print(nome + "\n, falta {f} ano para o seu alistamento!".format(f=falta))
	print("Ainda vai se alistar!")
elif idade == 18:
	print("\nJá é hora de se alistar!")
else:
	passou = idade - 18
	if passou == 1:
		print("\nJá passou {p} ano de você se alistar!".format(p=passou))
        print("Você deveria ter se alistado em {s}".format(s=alistamento))
	else:
		print("\nJá se passaram {p} anos de você se alistar!".format(p=passou))
		
print("\nOperação finaizada!")

n1 = int(input("\n\nDigite um número: "))
print(n1)