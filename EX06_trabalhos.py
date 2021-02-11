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
        soma3 = int()
        soma5 = int()
        multi3 = []
        multi5 = []
        multi15 = []

        # Limpar ecrã
        os.system('clear')

        # iniciar variáveis
        numero = 1
        soma = 0
        soma3 = 0
        soma5 = 0
    
        # Condição de 1 a 1001
        for numero in range(1, 1001):
            # Validar se o número é divisível por 3. Adicionar a lista e as somas de controlo.
            if numero % 3==0:
                multi3.append(numero)
                soma3 = soma3 + numero
                #soma = soma + numero
            # Validar se o número é divisível por 5. Adicionar a lista e a soma de controlo.
            if numero % 5==0:
                multi5.append(numero)
                soma5 = soma5 + numero
                #soma = soma + numero
            # Validar se o número é divisível por 3 e 5 (um número divisível por 3 e 5 é divisível por 15)
            if numero % 15==0:
                multi15.append(numero)
    
        print("\nOs números divisíveis por 3 são:")
        print(str(multi3))
        print("\nOs números divisíveis por 5 são:")
        print(str(multi5))
        print("\nOs números divisíveis por 3 e 5 são:")
        print(str(multi15))
        print("\n" , 3 * "*" , "A soma dos números divisíveis por 3 é: " , str(soma3) , 3 * "*")
        print("\n" , 5 * "*" , "A soma dos números divisíveis por 5 é: " , str(soma5) , 5 * "*")
        print("\n" , 8 * "*" , "A soma dos números divisíveis por 3 e 5 é: " , str(soma3+soma5) , 8 * "*")
        #print(soma)
        print("\n\nFim de programa!!!")

    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()
