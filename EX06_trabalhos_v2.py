#!/usr/bin/python3
#coding: utf-8

# Nesta versão do exercício encontro todos os valores de 3, 5 e 15, somo os reultados de 3 e 5 e subtraio do resultado de 15
# Utilizo vários condições (if) entre somas, mutliplicação, subtração e contadores

# Importar bibliotecas
import sys, os, time, datetime, string

if __name__ == "__main__":
    try:
        # Limpar ecrã
        os.system('clear')

        # Declarar variáveis    
        contador = 1000
        multiplos = [3, 5, 3*5]
        resultado = 0
        soma = 0

        # Inicia o contador pelos multiplos existentes
        for x in multiplos:
            result = 0
            # Inicia contador
            for y in range(contador):
                # Se o resultado dos operandos x * y < 1000, somao a resultado o próprio resultado mais a multiplicação dos operadores x e y
                if y*x < 1000:
                    resultado = resultado + y*x
                # Se o operando y é igual ao contador -1
                elif y == (contador - 1):
                    # e x < 15, a soma será a mesma mais o reultado
                    if x < 15:
                        soma = resultado + soma
                    # se for = a 15, então subtrai da soma a própria soma menos o resultado
                    elif x == 15:
                        soma = soma - resultado
        print("\nO resultado da soma de 3 e 5 para todos os números abaixo de 100 é: " + str(soma) + "\n")

    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()
