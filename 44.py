#   Elabore um programa que calcule o valor a ser pago por um produto,
#   considerando o seu preço normal e condição de pagamento:
#   - À vista dinheiro/cheque: 10% de desconto
#   - À vista no cartão: 5% de desconto
#   - Em até 2x no cartão: Preço normal
#   - 3x ou mais no cartão: 20% de juros

print("Calculadora de Conta kkkk\n")
produto = float(input("Digite o valor do produto: R$"))
pagamento = int(input("""Digite o número correspondente à forma de pagamento:
1) À vista/cheque: 10% de desconto
2) Até 2x no cartão
3) Até 3x ou mais, no cartão: 20% de juros
4) À vista no cartão: 5% de desconto
__: """))

if pagamento==1:
    Pfinal = produto - (produto*0.1)
    print("\nO preço final é R${p}".format(p=Pfinal))
elif pagamento==2:
    Pfinal = produto
    print("\nSua compra será parcelada em 2x no cartão\nO preço final é R${p}".format(p=Pfinal))
elif pagamento==3:
    Pfinal = produto + (produto*0.2)
    parcelas = int(input("\nDigite a quantidade de parcelas: "))
    Pfinal2 = float(Pfinal / parcelas)
    print("\nSu compra será parcelada em {}x no catão, com 20% de júros\nO preço final é R${}, em {}x.".format(parcelas, Pfinal2, parcelas))
elif pagamento==4:
    Pfinal = produto - (produto*0.05)
    print("\nO preço final é R${p}".format(p=Pfinal))
else:
    print("\nIndefinido!")
print("\nFim do programa.")
  

n1 = int(input("\n\nDigite um número: "))
print(n1)