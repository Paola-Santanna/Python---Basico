#	A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
#	mostre sua categoria, de acordo com a idade:
#	- Até 9 anos: Mirim
#	- Até 14 anos: Infantil
#	- Até 19 anos: Júnior
#	- Até 20 anos: Sênior
#	- Acima: Master

from datetime import date

print("Classificação do Nível do Atleta!\n")
anoNasc = int(input("Digite o ano do seu nascimento: "))
idade = date.today().year - anoNasc

if idade<=9:
    print("\nMIRIM!")
elif idade<=14:
    print("\nINFANTIL!")
elif idade<=19:
    print("\nJÚNIOR!")
elif idade<=20:
    print("\nSÊNIOR!")
else:
    print("\nMASTER")
print("\nOperação finalizada!")

n1 = int(input("\n\nDigite um número: "))
print(n1)