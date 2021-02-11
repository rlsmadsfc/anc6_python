#!/usr/bin/python3
#coding: utf-8

# Importar bibliotecas
import sys, os, time, datetime, math

# Função que utiliza lista
# Multiplicar todos os números da lista - obter um número que é divisível por todos os números desta lista
# Excluir os fatores que são comuns caso seja um múltiplo
def calculo_lista(x, y):
    # Ignorar os múltiplos de 1 (x+1) na lista
    inteiros = list(range(x+1, y + 1))
    
    lcm = 1
    while len(inteiros) > 0:
        z = inteiros.pop(0)
        if z == 1:
          continue
        lcm *= z
        inteiros = [w // z if w % z == 0 else w for w in inteiros]
    return lcm

# Definição de funções
# Retornar o maior divisor comum dos inteiros x e y
def gcd(x,y):
    return y and gcd(y,x % y) or x

# Esta função vai retonar o menor múltiplo comum entre x e y
def lcm(x,y):
    return x * y / gcd(x,y)

# Programa principal
if __name__ == "__main__":

    try:
        # Limpar ecrã
        os.system('clear')
    
        # Definição de variáveis
        # A utilização destas variáveis permite adaptar o codigo para receber o input do utilizador
        minimo = 1
        maximo = 20

        print("\nCálculo do menor número que é uniformemente divisível por todos os números de 1 até " + str(maximo) + " !")

        # Execução do 1º método - trabalhar com listas
        print("\n1º Método, utilizando a lista para cálculos. Resultado: " + str(calculo_lista(minimo,maximo)))

        # Execução do 2º método - função gcd()
        resultado = 1
        for i in range(minimo, maximo + 1):
            resultado = int(lcm(resultado, i))
        print("\n2º Método, utilizando a função gcd(). Resutlado: " + str(resultado))

        print("\nFim de programa!!!\n")
    
    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()
