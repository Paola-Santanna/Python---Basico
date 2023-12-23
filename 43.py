#   Desenvolva uma lógica que leia o peso e a atura de uma pessoa,
#   calcule seu IMC e ostre seu status, de acordo com a tebela abaixo:
#   - Abaixo de 18.5: Abaixo do peso
#   - Entre 18.5 e 25: Peso ideal
#   - 25 até 30: Sobrepeso
#   - 30 até 40: Obesidade
#   - Acima de 40: Obesidade mórbida"""

print("Calculadora de IMC (Índice de Massa Corporal)\n")
peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura, em Metros: "))
imc = peso/(altura*altura)

if imc<18.5:
    print("\nAbaixo do peso.")
elif imc>=18.5 and imc<25:
    print("\nPeso ideal.")
elif imc>=25 and imc<30:
    print("\nSobrepeso.")
elif imc>=30 and imc<40:
    print("\nObesidade.")
else:
    print("\nObesidade Mórbida.")
print("\nFim")

n1 = int(input("\n\nDigite um número: "))
print(n1)