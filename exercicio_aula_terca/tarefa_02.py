"""Parte 2: Operadores Aritméticos
Com base nas variáveis idade e altura, faça os seguintes cálculos:"""


# Defina as variáveis idade e altura
# Variável idade (tipo int)

idade = 42  # Exemplo de valor para idade
altura = 1.65  # Exemplo de valor para altura (em metros)

# Realizando os cálculos
soma_idade = idade + 10
multiplicacao_altura = altura * 2
divisao_idade = idade / 2
modulo_idade = idade % 3

# Imprimindo os resultados com mensagens explicativas
print(f"A idade é: {idade} anos")
print(f"A altura é: {altura} metros")
print(f"A soma da idade com 10 é: {soma_idade}")
print(f"A multiplicação da altura por 2 é: {multiplicacao_altura:.2f} metros")
print(f"A divisão da idade por 2 é: {divisao_idade:.2f}")
print(f"O módulo da idade por 3 é: {modulo_idade}")
