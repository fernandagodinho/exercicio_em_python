# Exercício 1: Verificar se uma palavra é um palíndromo

def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

# Exemplo de uso
print(eh_palindromo("arara"))  # Saída: True
print(eh_palindromo("python"))  # Saída: False
