# Solicita ao usuário que insira o seu nome
nome = input("Digite seu nome: ")

# Exibe uma mensagem de saudação personalizada
print(f"Olá, {nome}! Vamos fazer algumas contas.")

# Solicita ao usuário dois números para realizar as operações matemáticas
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

# Realiza as operações matemáticas (soma, subtração, multiplicação, divisão)
soma = num1 + num2 # Calcula a soma dos dois números
subtracao = num1 - num2 # Calcula a subtração dos dois números
multiplicacao = num1 * num2 # Calcula a multiplicação dos dois números
divisao = num1 / num2 # Calcula a divisão do primeiro número pelo segundo

# Exibe os resultados das operações matemáticas
print(f"A soma de {num1} e {num2} é {soma}")
print(f"A subtração de {num1} e {num2} é {subtracao}")
print(f"A multiplicação de {num1} e {num2} é {multiplicacao}")
print(f"A divisão de {num1} por {num2} é {divisao}")

# Agradece o usuário por usar a calculadora simples
print("Obrigado por usar a calculadora simples!")
