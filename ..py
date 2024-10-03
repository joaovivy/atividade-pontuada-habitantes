# Leonardo Araujo, João Filipe

import os 
os.system("cls || clear")

from dataclasses import dataclass

@dataclass
class Habitantes:
    salario: float
    idade: int
    sexo: str


#variaveis



contador_mulheres = 0
contador_habitantes = 0
contador_mulher = 0

#calculos
lista_salarial = []
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
            idade = int(input("Digite sua idade: "))
            sexo = input("Digite seu genero [F/M]: ").upper()
            salario = float(input("Digite o seu salário: "))
            habitante = Habitantes( 
                idade= idade, sexo=sexo, salario=salario
            )
            lista_salarial.append(habitante.salario)
            lista_habitantes.append(habitante)
            lista_idade.append(habitante.idade)


            if habitante.salario >= 5000 and habitante.sexo == "F":
                contador_mulher += 1

            with open("pesquisa_habitantes.txt", "a") as file:
                for habitante in lista_habitantes:
                    file.write(f"idade::{habitante.idade}, sexo:{habitante.sexo}, salario:{habitante.salario}, quantos mulherescom salario acima de 5000:{contador_mulher}\n")

        case "2":
            print("=====EXIBINDO RESULTADOS=====")
        

            total_habitantes = len(lista_salarial)
            total_salario = sum(lista_salarial)
            media_salarial = total_salario / total_habitantes
            maior_idade = max(lista_idade)
            menor_idade = min(lista_idade)

            print(f"Média de salário é de: {media_salarial: .2f}")
            print(f"Maior idade: {maior_idade}")
            print(f"Menor idade: {menor_idade}")
            print(f"Quantidade de mulheres com salário a acima de 5000 R$: {contador_mulher} ")

        case "3":
            print("fim")
            break

        case _:
           print("opção invalida!!")