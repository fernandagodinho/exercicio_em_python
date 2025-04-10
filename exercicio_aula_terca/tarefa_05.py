# Solicita as informações do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cores_favoritas = tuple(input("Digite suas três cores favoritas, separadas por vírgulas: ").split(','))

# Exibe uma mensagem personalizada com nome e idade
print(f"\nOlá, {nome}! Você tem {idade} anos.")

# Exibe a tupla com as cores favoritas
print(f"Suas cores favoritas são: {cores_favoritas}")
