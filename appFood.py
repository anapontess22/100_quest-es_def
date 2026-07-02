from modelos.avaliacao import Avaliacao
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.prato import Prato
from modelos.restaurante import Restaurante
import os

def exibir_nome_do_programa():
         
            print(r""" 
╭━━━╮╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱┃╭━━╯╱╱╱╱╱╱╱┃┃
┃┃╱┃┣━━┳━╮┃╰━━┳━━┳━━┳━╯┃
┃╰━╯┃╭╮┃╭╮┫╭━━┫╭╮┃╭╮┃╭╮┃
┃╭━╮┃╰╯┃┃┃┃┃╱╱┃╰╯┃╰╯┃╰╯┃
╰╯╱╰┫╭━┻╯╰┻╯╱╱╰━━┻━━┻━━╯
╱╱╱╱┃┃
╱╱╱╱╰╯""")
            print("1. Cadastrar restaurante")
            print("2. Listar restaurantes")
            print("3. Alternar estado do restaurante")
            print("4. Adicionar avaliação")
            print("5. Adicionar item ao cardápio")
            print("6. Exibir cardápio")
            print("7. Sair")

            opcao = input('Digite uma opção: ')


            if opcao == '1':
                    cadastrar_restaurante()

            elif opcao == '2':
                    listar_restaurantes()
                
            elif opcao == "3":
                    alternar_estado()

            elif opcao == "4":
                    receber_avaliacao()

            elif opcao == "5":
                    receber_cardapio()

            elif opcao == "6":
                    mostrar_cardapio()

            elif opcao == "7":
                   sair()
                    



def cadastrar_restaurante():
        print("Cadastro de Restaurante")

        nome = input("Nome do restaurante: ")
        categoria = input("Categoria: ")

        variavel = Restaurante(nome, categoria)

        print(f"O restaurante '{nome}' foi cadastrado com sucesso!")
        sair()



def listar_restaurantes():
    print("Nome do Restaurante | Categoria | Avaliações")

    for restaurante in Restaurante.Restaurantes:
        print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(20)} | {restaurante.media_avaliacoes}")

    sair()

def alternar_estado():
    nome_restaurante = input("Digite o nome do restaurante: ")

    for restaurante in Restaurante.Restaurantes:

        if restaurante._nome.lower() == nome_restaurante.lower():

            restaurante.alternar_estado()

            print(f"O restaurante {restaurante._nome} teve seu estado alterado!")

            sair()
            return

    print("Restaurante não encontrado.")
    sair()



def receber_avaliacao():
    nome_restaurante = input("Nome do restaurante: ")
    nome_cliente = input("Seu nome: ")
    nota = float(input("Nota (0 a 5): "))

    for restaurante in Restaurante.Restaurantes:
        if restaurante._nome.lower() == nome_restaurante.lower():
            restaurante.receber_avaliacao(nome_cliente, nota)
            print("Avaliação adicionada com sucesso!")
            sair()
            return

    print("Restaurante não encontrado.")
    sair()




def receber_cardapio():
    nome_restaurante = input("Nome do restaurante: ")

    for restaurante in Restaurante.Restaurantes:

        if restaurante._nome.lower() == nome_restaurante.lower():

            tipo = input("Digite P para prato ou B para bebida: ").upper()

            nome = input("Nome: ")
            preco = float(input("Preço: "))

            if tipo == "P":
                descricao = input("Descrição: ")
                prato = Prato(nome, preco, descricao)
                restaurante.receber_cardapio(prato)

            elif tipo == "B":
                tamanho = input("Tamanho: ")
                bebida = Bebida(nome, preco, tamanho)
                restaurante.receber_cardapio(bebida)

            print("Item adicionado ao cardápio!")

            sair()
            return

    print("Restaurante não encontrado.")
    sair()




def mostrar_cardapio():

    nome_restaurante = input("Nome do restaurante: ")

    for restaurante in Restaurante.Restaurantes:

        if restaurante._nome.lower() == nome_restaurante.lower():

            restaurante.mostrar_cardapio()

            sair()
            return

    print("Restaurante não encontrado.")
    sair()


def sair():
    input("\nTecle Enter para voltar ao menu...")
    os.system('cls')


def main():
    while True:
        os.system('cls')
        exibir_nome_do_programa()

if __name__ == "__main__":
    main()