#!/usr/bin/python3
import os

# limpa ecra
os.system('clear')

# definir variaveis iniciais
a = 76
b = 13
c = 0

print("Exercicio 1 Operacao aritmetica entre 2 variaveis")
x1 = (a * b) / 2
print(x1)
print("")

print("Exercicio 2 Operacao relacional entre 2 variaveis")
x2 = a < b
print(x2)
print("")

print("Exercicio 3 Operacao binaria entre 2 variaveis")
print("Na operacao binaria >> o valor do operando da esquerda e movido para a direita pelo numero de bits especificados pelo operando a direita")
x3 = a >> 2
print("A operacao binaria de " + str(a) + " >> 2 e " + str(x3) + " que em binario e "+ str(bin(x3)))
print("")

print("Exercicio 4 Operacao identidade ou associacao entre 2 variaveis")
print("Para este exercicio o valor da operacao binaria " + str(x3) +" foi incluido na lista da variavel d")
d =[16,5,x3,73,47,20,21]
x4 = 19 in d
print(x4)