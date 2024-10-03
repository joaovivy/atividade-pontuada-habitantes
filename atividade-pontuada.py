import os
from dataclasses import dataclass

os.system("cls || clear")

# Turma: G93313
# Equipe: Itauã Gualberto, João Gabriel, Gustavo Batista.
@dataclass
class Pesquisa:
    salario: float
    idade: int
    sexo: str

def media(x,y):
    media = x/y
    return media

def maior_menor(x):
    maior = max(lista_de_idade)
    menor = min(lista_de_idade)
    return maior, menor

lista_de_idade = []
lista_habitantes = []
lista_salario = []
contador_salario = 0
lista_mulheres = []
contador_idade = 0
numero_habitantes = 0
QTD = 1

print("""
1- | adicionar         |
2- | Exibir resultados |
3- | Sair              |
""")
opcao = int(input("Escolha uma opção: "))

match(opcao):
    case 1:
    salario = float(input("Digite seu salário: ")),
    idade = int(input("Digite sua idade: ")),
    sexo = input("Digite seu sexo: ")
        
            lista_mulheres
        lista_habitantes.append(habitantes)
        lista_salario.append(habitantes.salario)    
        contador_salario += 1
        numero_habitantes += 1

        os.system("cls || clear")        
        
    case 2:
        print("exibindo...")
        for habitantes in lista_habitantes:
                print(f"Idade: {habitantes.idade}")
                print(f"Sexo: {habitantes.sexo}")
                print(f"Salário: R$ {habitantes.salario}")
                

            maior_idade, menor_idade = maior_menor(lista_de_idade)
            media_salario = media(sum(lista_salario), (len(lista_salario)))
            print(f"\nMédia de salários: {media_salario:.2f}")
            print(f"\nMaior idade: {maior_idade:.2f}")
            print(f"\nMenor idade: {menor_idade:.2f}")
            
        if contador_idade > 1 and sexo == "f" and salario >= 5000:
                lista_mulheres.append(habitantes.salario.sexo)
            