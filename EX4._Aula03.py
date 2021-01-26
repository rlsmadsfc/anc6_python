#!/usr/bin/python3
#coding: utf-8

# Este programa ainda tem muito por optimizar
# O Objetivo foi demonstrar a navegação em um menu
# Executar os comandos de operações em diretorias: mudar, criar, apagar, renomear e listar (apenas diretorias)

# Importar bibliotecas
import sys, os, time, datetime, platform, pathlib

# Função Lista Diretoria
def listaDir(loopDef):
    loopEspera = True
    print("Lista atual de diretorias:")
    listaDiretorias = [os.path.join(os.getcwd(), o) for o in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), o))]
    print(listaDiretorias)
    if loopDef == 1:
        while loopEspera:
            escolhaDir = input("\nDigite 0 para regressar ao menu principal: ")
            if escolhaDir == "0":
                os.system('clear')
                loopEspera = False
            else:
                loopEspera = True

# Função Cria Diretoria
def criaDir():
    loopCria = True
    escolhaDir = ""
    os.system('clear')
    print("Diretoria atual: " + os.getcwd())    
    print("\n")
    listaDir(0)

    while loopCria:
        escolhaDir = input("\nDigite a diretoria a criar nesta pasta ou 0 para sair: ")
        if escolhaDir == "0":
            os.system('clear')
            loopCria = False
        else:
            direxiste=os.path.exists(escolhaDir)
            if direxiste == False:
                os.mkdir(escolhaDir)
                print("\nDiretoria criada!\n")
                listaDir(1)
                os.system('clear')
                loopCria = False
            else:   
                print("A diretoria " + escolhaDir +" já existe nesta pasta!")
                loopCria = True
                continue

# Função remove diretoria
def removeDir():
    loopRemove = True
    escolhaDir = ""
    os.system('clear')
    print("Diretoria atual: " + os.getcwd() +"\n")
    print("\n")
    listaDir(0)
    
    while loopRemove:
        escolhaDir = input("\nDigite a diretoria a apagar nesta pasta ou 0 para sair: ")
        if escolhaDir == "0":
            loopRemove = False
        else:
            direxiste=os.path.exists(escolhaDir)
            if direxiste == True:
                os.rmdir(escolhaDir)
                print("\nDiretoria apagada!\n")
                listaDir(1)
                os.system('clear')
                loopRemove = False
            else:   
                print("A diretoria a apagar " + escolhaDir +" não existe nesta pasta!")
                continue
 
# Função renomeia diretoria
def renomeDir():
    loopRenome = True
    loopNova = True
    escolhaDir = ""
    novaDir = ""
    os.system('clear')
    print("Diretoria atual: " + os.getcwd() +"\n")
    print("\n")
    listaDir(0)
    
    while loopRenome:
        escolhaDir = input("\nDigite a diretoria a renomear nesta pasta ou 0 para retornar ao menu principal: ")
        if escolhaDir == "0":
            loopRemove = False
        else:
            direxiste=os.path.exists(escolhaDir)
            if direxiste == False:
                print("A diretoria não existe e não pode ser renomeada.")
                loopRenome = True
            else:
                loopRenome = False

    while loopNova:
        novaDir= input("\nDigite o nome da nova diretoria ou 0 para retornar ao menu principal: ")
        if novaDir == "0":
           loopNova=False
        else:
            direxistenova=os.path.exists(novaDir)
            if direxistenova == False:
                os.rename(escolhaDir,novaDir)
                print("\nDiretoria renomeada!\n")
                listaDir(1)
                os.system('clear')
                loopNova = False
            else:   
                print("A diretoria a renomear " + escolhaDir +" já existe nesta pasta!")
                loopNova = True
    
# Função muda diretoria
def mudaDir():
    loopMuda = True
    escolhaDir = ""
    os.system('clear')
    print("Diretoria atual: " + os.getcwd() +"\n")
    listaDir(0)
    print("\n")

    while loopMuda:
        escolhaDir = input("\nDigite a diretoria destino ou 0 para retornar ao menu principal: ")
        if escolhaDir == "0":
            loopMuda = False
        else:
            direxiste=os.path.exists(escolhaDir)
            if direxiste == False:
                print("A diretoria pretendida não existe!")
                loopMuda = True
            else:
                os.chdir(escolhaDir)
                print("\nDiretoria atual é: " + os.getcwd() +"\n")
                listaDir(1)
                # time.sleep(5)
                os.system('clear')
                loopMuda = False


# Função define menu
def menuDir():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Lista diretoria")
    print("2. Cria diretoria")
    print("3. Remove diretoria")
    print("4. Renomear diretoria")
    print("5. Mudar diretoria")
    print("6. Exit")
    print(67 * "-")
  
    loop=True      
  
# Program principal #
if __name__ == "__main__":

    try:
        # Definição de variáveis
        loop = True
        escolha = '0'

        # Limpar ecrã
        os.system('clear')
    
        # Loop no menu para escolha de opções
        while loop:
            menuDir()
            escolha = input("Digite a opção da operação: ")
        
            if escolha == "1":     
                os.system('clear')
                listaDir(1)
            elif escolha == "2":
                criaDir()
            elif escolha == "3":
                removeDir()
            elif escolha == "4":
                renomeDir()
            elif escolha == "5":
                mudaDir()
            elif escolha == "6":
                loop=False
            else:
                print(escolha)
                print("Seleção incorreta. Tente novamente!")
                continue

    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()

