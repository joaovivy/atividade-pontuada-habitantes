# Turma = G93313
# Gustavo de Jesus Batista, João Gabriel Dos Santos e Itauã Gualberto Borges 

import os 
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Habitantes:
    salario: float
    idade: int
    sexo: str

contador_mulheres = 0
contador_habitantes = 0
contador_mulher = 0

lista_salario = []
lista_idade = []
lista_habitantes = []

while True:
    print("""
    1 | Adicionar pessoa
    2 | Exibir resultados
    3 | Sair
        """)

    menu = input("Escolha uma opção: ")
    match menu:
        case "1":
            os.system("cls || clear")
            idade = int(input("Digite uma idade: "))
            sexo = input("Digite um gênero [F/M]: ").upper()
            salario = float(input("Digite um salário: "))
            habitante = Habitantes( 
                idade= idade, sexo=sexo, salario=salario
            )
            lista_salario.append(habitante.salario)
            lista_habitantes.append(habitante)
            lista_idade.append(habitante.idade)


            if habitante.salario >= 5000 and habitante.sexo == "F":
                contador_mulher += 1

            with open("pesquisa_habitantes.txt", "a") as file:
                for habitante in lista_habitantes:
                    file.write(f"idade::{habitante.idade}, sexo:{habitante.sexo}, salário:{habitante.salario}, quantas mulheres com salário acima de 5000:{contador_mulher}\n")

        case "2":
            print("=====EXIBINDO RESULTADOS=====")
        

            total_habitantes = len(lista_salario)
            total_salario = sum(lista_salario)
            media_salarial = total_salario / total_habitantes
            maior_idade = max(lista_idade)
            menor_idade = min(lista_idade)

            print(f"Média de salário é de: {media_salarial: .2f}")
            print(f"Maior idade: {maior_idade}")
            print(f"Menor idade: {menor_idade}")
            print(f"Quantidade de mulheres com salário acima de 5000 R$: {contador_mulher} ")

        case "3":
            print("\n=== FIM ===")
            break

        case _:
           print("opção inválida, digite novamente!")