#   Refaça o desafio dos triângulos, acrescentando o recurso de mostrar
#   que tipo de triângulo será formado:
#   - Equilátero: Todos os lados iguais
#   - Isóceles: Dois lados iguais
#   - Escaleno: todos os lados diferentes"""

print("Identificando o Tipo de Triângulo!\n")
l1 = float(input("Digite o valor do lado 1: "))
l2 = float(input("Digite o valor do lado 2: "))
l3 = float(input("Digite o valor do lado 3: "))

if l1<l2+l3 and l2<l1+l3 and l3<l2+l1:
    print("\nOs seguimentos acima podem formar um  triângulo!")
    if (l1==l2 or l1==l3) and (l1!=l3 or l1!=l3) :
        print("\nÉ um triângulo Isóceles!")
    elif (l2==l1 or l2==l3) and (l2!=l3 or l2!=l1):
        print("\nÉ um triângulo Isóceles!")
    elif (l3==l2 or l3==l1) and (l3!=l1 or l3!=l2):
        print("\nÉ um triângulo Isóceles!")
    elif (l1==l2==l3):
        print("\nÉ um triânguli Equilátero!")
    elif l1!=l2!=l3 and l3!=l1:
        print("\nÉ um triângulo Escaleno!")
    print("\nFim da operação!")
else:
    print("Os segmentos acima não podem formamr um triângulo!")

n1 = int(input("\n\nDigite um número: "))
print(n1)