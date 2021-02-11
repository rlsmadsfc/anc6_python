#!/usr/bin/python3
#coding: utf-8

# Neste exercício poderia ter sido utilizada apenas a manipulação de listas
# Contudo preferi utilizar listas e strings para exercitar a lógica, manipulação de variáveis

# Importar bibliotecas
import sys, os, time, datetime, string

# Função para procurar a letra na lista
def procura_letra(lista, letra):
    for i in range(len(lista)):
        if lista[i] == letra:
            return True
    return False

# Programa principal
if __name__ == "__main__":

    try:
        # Definir variáveis
        index1 = int()
        index2 = int()
        string1=""
        string2=""
        loop1 = 1
        loop2 = True
        letras = []
        listaAlfabeto = []
        output = []
        msg = ""

        # Criar uma lista com o alfabeto em minúsculas
        listaAlfabeto = list(string.ascii_lowercase)

        # Limpar ecrã
        os.system('clear')
        
        # Imprime a lista (alfabeto)
        print("\nAs letras digitadas em maiúsculas serão convertidas para minúsculas\n")
        print("\nEste é o alfabeto (em lista):")
        print(listaAlfabeto)
        
        # Cria a condição para entrada de dados (2 letras)
        for loop1 in range(1,3):
            if loop1 == 1:
                msg = "primeira"
            else:
                msg = "segunda"
    
            loop2 = True

        # Entrada de dados (2 letras)
            while loop2:
                entrada = input("\nDigite a " + msg + " letra (a-z): ")
                if len(entrada) != 1:
                    print("\nDigite uma única letra (a-z)")
                # Valida se a letra digita está no alfabeto
                if procura_letra(listaAlfabeto, entrada.lower()) == True:
                    # Valida se a letra já foi digitada
                    if procura_letra(letras, entrada.lower()) == False:
                        letras.append(entrada.lower())
                        loop2 = False
                    else:
                        print("\nLetra já digitada! Digite uma nova letra!")
                else:
                    loop2 = True

        # Cria indexadores ordenados pelas posições das letras no alfabeto
        # Uma alternativa seria fazer o sort da lista
        if listaAlfabeto.index(letras[0]) < listaAlfabeto.index(letras[1]):
            index1 = listaAlfabeto.index(letras[0])
            index2 = listaAlfabeto.index(letras[1])
        else:
            index1 = listaAlfabeto.index(letras[1])
            index2 = listaAlfabeto.index(letras[0])
        
        # Cria uma string com alfabeto tendo como base a lista
        for i in range(len(listaAlfabeto)):
            string1 = string1+" "+listaAlfabeto[i]
        
        # Imprime o alfabeto em string
        print("\nEste é o alfabeto (em string):" + string1)

        # Cria uma string com as letras fornecidas
        for i in range(index1, index2+1):
            string2 = string2+listaAlfabeto[i]

        # Valida se as letras estão lado a lado. Se sim, imprime as letras em maiúsculas para diferenciar do alfabeto
        # Se não estiverem próximas, avança para os próximos passos
        if index2 - index1 == 1:
            print("\nAs letras são próximas e não há uma letra central. Ver abaixo as letras em maiúsculas:\n")
            output=listaAlfabeto
            output[index1] = listaAlfabeto[index1].upper()
            output[index2] = listaAlfabeto[index2].upper()
            print(output)
        else:
            # Retonar as duas letras centrais quando o total de elementos na string for par
            # Ou retorna a letra central se o total de elementos na string for ímpar)
            if len(string2) % 2 == 0:
                meio_esquerda = string2[(len(string2) - 1) // 2]
                meio_direita = string2[len(string2) // 2]
                # A impressão é feita de acordo com a sequência de entrada do utilizaodr
                print("\nAs letras " + meio_esquerda + "," + meio_direita + " são centrais as letras " + str(letras[0] + "-" + str(letras[1])))
            else:
                medio = string2[len(string2)//2]
                # A impressão é feita de acordo com a sequência de entrada do utilizaodr
                print("\nA letra " + medio + " é central as letras " + str(letras[0] + "-" + str(letras[1])))

        print("\nFim de Programa!!!")
    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()
