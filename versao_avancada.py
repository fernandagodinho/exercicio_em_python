#versão com classe e metodos
class Aluno:
    def __init__(self, nome, notas):
        
        #Inicializa a classe Aluno com o nome e as notas.
        
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        
       # Calcula a média das notas do aluno.
        
        return sum(self.notas) / len(self.notas)
    
    def verificar_aprovacao(self):
        
        #Verifica se o aluno foi aprovado ou reprovado com base na média.
        
        media = self.calcular_media()
        return "Aprovado" if media >= 7 else "Reprovado"
    
    def exibir_resultado(self):
        
        #Exibe os resultados, incluindo média e status de aprovação/reprovação.
        
        media = self.calcular_media()
        status = self.verificar_aprovacao()
        print(f"\nAluno: {self.nome}")
        print(f"Média Final: {media:.2f}")
        print(f"Status: {status}")


# Fluxo principal do programa

print("Simulador de Nota Escolar (Versão Avançada)")

# Entrada de dados do aluno

nome = input("Digite o nome do aluno: ")
print("Insira três notas (entre 0 e 10):")
notas = [
    float(input("Nota 1: ")),
    float(input("Nota 2: ")),
    float(input("Nota 3: "))
]

# Criação do objeto Aluno e exibição dos resultados
aluno = Aluno(nome, notas)
aluno.exibir_resultado()

print("\nObrigado por usar o simulador de nota escolar!")

"""
Explicação das melhorias:

Estrutura com Classes e Métodos:

O código foi organizado em uma classe chamada Aluno, o que facilita 
o gerenciamento e reutilização.

Encapsulamento: 
Métodos como calcular_media, verificar_aprovacao e exibir_resultado 
garantem que a lógica seja bem definida dentro da classe.

Entrada Dinâmica:
As notas são recebidas como uma lista, tornando o código mais flexível 
 para futuras modificações."""