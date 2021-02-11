#!/usr/bin/python3
#coding: utf-8

# Importar bibliotecas
import sys, os, time, datetime, collections


# Program principal #
if __name__ == "__main__":

    try:
        # Definição de variáveis
        loop1 = 1
        loop2 = True
        resultado = False
        numero = int()
        lista = []
        # Limpar ecrã
        os.system('clear')
    
        # Loop para digitar os segundos
        while loop1 < 5:
            try:
                numero = int(input("\nDigite o número " + str(loop1) + " (inteiro): "))
                lista.append(numero)
                loop1 +=1
            except ValueError:
                print("\nDigite um número inteiro!")
                continue

        print("\nA lista de números é :" + str(lista))
        
        resultado = lista.count(lista[0]) == len(lista)
        if resultado == True:
            print("\nNão há nuḿeros diferentes, todos os números são iguais!")
        else:
            print("\nNúmeros diferentes: " + str(len(set(lista))))
               
        print("Número de pares: " + str(len(list(filter(lambda pares: (pares%2 == 0) , lista)))))
        print("Número de ímpares: " + str(len(list(filter(lambda impares: (impares%2 != 0) , lista)))))

        print("\nFim de programa!!!")
    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()

