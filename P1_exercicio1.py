""" Projeto 1 """

import random

def rolagem_de_dados():
    while True:
            tamanho_dado = input("Forneça o tamanho do dado que será rolado (ENTER para sair): ")
            if tamanho_dado.isnumeric():
                while True:
                    quantidade_dados = input("Forneça o número de dados que serão rolados (em branco == 1): ")
                    if quantidade_dados.isnumeric():
                        for lançamento in range(1,int(quantidade_dados) + 1):
                            aleatorio_dados = random.randint(1 , float(tamanho_dado))
                            print("Lançamento n.", lançamento , " - ", aleatorio_dados)
                        break
                    elif quantidade_dados == "":
                        aleatorio_dados = random.randint(1 , float(tamanho_dado))
                        print("Lançamento n. 1 - ", aleatorio_dados)
                        break
                    else:
                        print("A informação passada não é válida!")
                break
            elif tamanho_dado == "":
                break
            else:
                print("A informação passada não é válida!")

                
rolagem_de_dados()