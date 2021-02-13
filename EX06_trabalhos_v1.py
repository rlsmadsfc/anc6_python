#!/usr/bin/python3
#coding: utf-8

# Neste exercício poderia ter sido utilizada apenas a manipulação de listas
# Contudo preferi utilizar listas e strings para exercitar a lógica, manipulação de variáveis

# Importar bibliotecas
import sys, os, time, datetime, string

if __name__ == "__main__":
    try:
        # Declarar variáveis e listas
        numero = int()
        soma = int()
        soma35 = int()
        soma15 = int()
        multi35 = []
        multi15 = []

        # Limpar ecrã
        os.system('clear')

        # iniciar variáveis
        numero = 1
        soma = 0
        soma15 = 0
        soma35 = 0
    
        # Condição de 1 a 1001
        for numero in range(1, 1001):

            if numero % 3== 0 and numero % 5 == 0:
                soma35 = soma35 + numero
                multi35.append(numero)                

            if numero % 15==0:
                soma15 = soma15 + numero
                multi15.append(numero)

        print("\n" , 15 * "*", "A soma dos números divisíveis por 3 e 5 é: " , str(soma35) , 15 * "*")
        print("\n Os números divisíveis por 3 e 5 são: " + str(multi35))
        print("\n" , 15 * "*", "Estes números também são divisíveis por 15: " , str(soma15) , 15 * "*")
        print("\n Os números divisíveis por 15 são: " + str(multi15))
        print("\n\nFim de programa!!!")

    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()
