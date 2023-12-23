#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e menor peso lidos.
from time import sleep

#Jeito 1
#começarei fazendo do jeito que acho que vá dar certo, embora não seja o indicado:
pessoa01 = float(input("Digite o seu peso, em Kg: "))
pessoa02 = float(input("Digite o seu peso, em Kg: "))
pessoa03 = float(input("Digite o seu peso, em Kg: "))
pessoa04 = float(input("Digite o seu peso, em Kg: "))
pessoa05 = float(input("Digite o seu peso, em Kg: "))

if pessoa01 > pessoa02 and pessoa01 > pessoa03 and pessoa01 > pessoa04 and pessoa01 > pessoa05:
    print("A 1ª pesoa tem o maior peso: ", pessoa01)
elif pessoa02 > pessoa01 and pessoa02 > pessoa03 and pessoa02 > pessoa04 and pessoa02 > pessoa05:
    print("A 2ª pesoa tem o maior peso: ", pessoa02)
elif pessoa03 > pessoa02 and pessoa03 > pessoa01 and pessoa03 > pessoa04 and pessoa03> pessoa05:
    print("A 3ª pesoa tem o maior peso: ", pessoa03)
elif pessoa04 > pessoa02 and pessoa04 > pessoa03 and pessoa04 > pessoa01 and pessoa04 > pessoa05:
    print("A 4ª pesoa tem o maior peso: ", pessoa04)
elif pessoa05 > pessoa02 and pessoa05 > pessoa03 and pessoa05 > pessoa04 and pessoa05 > pessoa01:
    print("A 5ª pesoa tem o maior peso: ", pessoa05)
else:
    print("Erro")
sleep(5)

#Jeito 2
#O jeito mais indicado para fazer isso é usando o for loop (estou aprendendo):
#estrutura for
#ainda está errado
for n in range(5):
    peso = float(intput("Digite o seu peso, em Kg: "))
    for resul_men in peso:
        if resul_men < peso
        resul_men = peso
    print("o menor peso é: ", resul_men)
    for resul_maior in peso:
        if resul_maior > peso:
        resul_maior = peso
    print("O maior peso é: ", resul_maior)

sleep(5)