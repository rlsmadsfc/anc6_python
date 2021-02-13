#!/usr/bin/python3
#coding: utf-8

# Neste exercício poderia ter sido utilizada apenas a manipulação de listas
# Contudo preferi utilizar listas e strings para exercitar a lógica, manipulação de variáveis
# Nesta versão do exercício 6 encontro todos os valores de 3, 5 e 15, somo os reultados de 3 e 5 e subtraio do resultado de 15

# Importar bibliotecas
import sys, os, time, datetime, string

if __name__ == "__main__":
    try:
        # Declarar variáveis e listas
        numero = int()
        soma = int()
        soma3 = int()
        soma5 = int()
        soma15 = int()
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
        soma15 = 0
  
        # Inicia o contador - menor que 1000
        for numero in range(1, 1000):
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
                soma15 = soma15 + numero
    
        print("\nOs números divisíveis por 3 são:")
        print(str(multi3))
        print("\nOs números divisíveis por 5 são:")
        print(str(multi5))
        print("\nOs números divisíveis por 3 e 5 são:")
        print(str(multi15))
        print("\n" , 3 * "*" , "A soma dos números divisíveis por 3 é: " , str(soma3) , 3 * "*")
        print("\n" , 5 * "*" , "A soma dos números divisíveis por 5 é: " , str(soma5) , 5 * "*")
        print("\n" , 8 * "*", "A soma dos números divisíveis por 3 e 5 são divisíveis por 15: " , str(soma15) , 8 * "*")        
        print("\n" , 15 * "*" , "A soma dos números divisíveis por 3 e 5 abaixo de 1000 é: " , str(soma3+soma5-soma15) , 15 * "*")
        print("\n\nFim de programa!!!")

    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()
