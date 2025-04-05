# Simulador de Nota Escolar (Versão Simples)

#  Entrada de dados
print("Insira três notas (entre 0 e 10):")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

#  Cálculo da média
media = (nota1 + nota2 + nota3) / 3

#  Exibição da média final
print(f"A média final é: {media:.2f}")

# Exibe a média com duas casas decimais
# Verifica se o aluno foi aprovado ou reprovado

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")