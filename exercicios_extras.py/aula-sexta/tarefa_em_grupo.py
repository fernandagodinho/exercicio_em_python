# 1. Crie uma lista chamada frutas com 5 frutas.
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# 2. Adicione uma fruta ao final da lista.
frutas.append("morango")

# 3. Adicione duas frutas de uma vez usando extend().
mais_frutas = ["kiwi", "abacaxi"]
frutas.extend(mais_frutas)

# 4. Insira uma fruta na posição 2.
frutas.insert(2, "pêssego")

# 5. Remova uma fruta pelo nome.
frutas.remove("banana")

# 6. Remova a última fruta da lista.
ultima_fruta = frutas.pop()
print(f"A última fruta removida foi: {ultima_fruta}")

# 7. Mostre a posição de uma fruta com index().
if "laranja" in frutas:
    posicao_laranja = frutas.index("laranja")
    print(f"A fruta laranja está na posição: {posicao_laranja}")
else:
    print("A fruta laranja não está na lista.")

# 8. Conte quantas vezes uma fruta aparece na lista.
quantidade_maca = frutas.count("maçã")
print(f"A fruta maçã aparece {quantidade_maca} vezes na lista.")

# 9. Organize a lista em ordem alfabética.
frutas.sort()
print(f"Lista em ordem alfabética: {frutas}")

# 10. Inverta a ordem da lista.
frutas.reverse()
print(f"Lista com ordem invertida: {frutas}")

# 11. Mostre uma cópia da lista atual.
copia_frutas = frutas.copy()
print(f"Cópia da lista de frutas: {copia_frutas}")