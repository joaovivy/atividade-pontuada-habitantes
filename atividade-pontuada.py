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

contador_mulher5000 = 0
feminino = 0
masculino = 0
contador_mulheres = 0
contador_habitantes = 0

lista_salario = []
lista_idade = []
lista_habitantes = []
lista_mulheres5000 = []

while True:

    print("""
1- | adicionar         |
2- | Exibir resultados |
3- | Sair              |
""")
    opcao = int(input("Escolha uma opção: "))
    match(opcao):
        case 1:
            os.system("cls || clear")        
            salario = float(input("Digite seu salario: "))
            lista_salario.append(salario)
            idade = int(input("Digite sua idade: "))
            lista_idade.append(idade)
            sexo = input("Digite seu sexo: ").upper().strip()
            
            lista_habitantes.append(Pesquisa(contador_mulher5000, salario, idade, sexo))

            if salario > 5000 and sexo == "F":
                contador_mulher5000 += 1
            with open("pesquisa_habitantes.txt", "w") as arquivo_habitantes:
                for habitante in lista_habitantes:
                    arquivo_habitantes.write(f"Mulheres com o salário acima de R$ 5000: {habitante.contador_mulher5000}, Idade: {habitante.idade}, Sexo: {habitante.sexo}, Salário: {habitante.salario}\n")
            
        case 2:
            maior_idade = max(idade)
            menor_idade = min(idade)
            salario_total = sum(lista_salario)
            media_salario = salario_total / lista_habitantes

            print("\n=== Exibindo resultados ===")
            print(f"Média de salário do grupo: {media_salario}")
            print(f"Maior idade do grupo: {maior_idade}")
            print(f"Menor idade do grupo: {menor_idade}")
            print(f"Quantidade de mulheres com salário a partir de R$5.000,00: {contador_mulher5000}")

            with open("pesquisa_habiantes.txt", "r") as arquivo_habitantes:
                print("Dados salvos...")
                lista_habitantes.append(Pesquisa(salario=float(salario), idade=int(idade), sexo=sexo, ))


        
        case "3":
            nome_do_arquivo = "pesquisa_habitante.txt"
            with open(nome_do_arquivo, "a") as arquivo_habitantes:
                for habitante in lista_habitantes:
                    pesquisadts.write(f"{habitante.salario}, {habitante.idade}, {habitante.sexo}\n")
            break