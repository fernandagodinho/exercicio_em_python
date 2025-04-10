"""
4) Faça um programa que peça um número inteiro e mostre na tela a sua tabuada."""

numero = int(input("Digite um número de 1 a 10: "))
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")
