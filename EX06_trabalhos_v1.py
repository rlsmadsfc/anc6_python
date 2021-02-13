#!/usr/bin/python3
#coding: utf-8

# Nesta versão do exercício optei por utilizar o "or" entre o múltiplo de 3 e 5 

# Importar bibliotecas
import sys, os, time, datetime, string

if __name__ == "__main__":
    try:
        # Declarar variáveis e listas
        numero = int()
        soma = int()
        soma35 = int()
        multi35 = []

        # Limpar ecrã
        os.system('clear')

        # iniciar variáveis
        numero = 1
        soma = 0
        soma35 = 0
    
        # Contador de 1 a 1000
        for numero in range(1, 1000):
            # Condição entre os divisores 3 e 5
            if numero % 3== 0 or numero % 5 == 0:
                soma35 = soma35 + numero
                multi35.append(numero)                

        print("\n Os números divisíveis por 3 e 5 são: " + str(multi35))
        print("\n" , 15 * "*", "A soma dos números divisíveis por 3 e 5 é: " , str(soma35) , 15 * "*")
        print("\n\nFim de programa!!!")

    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()
