#!/usr/bin/python3
import time
import os

# limpa ecra
os.system('clear')

# Definicao da lista
# Acrescentados outros SOs a lista original
lista=["windows","macos","linux","solaris","android","ios","as400","aix","hpux"]

# Expressao for
print("Expressao for:")
for i in lista:
   if i != "solaris":
     print(i);

# Pausa por 5 segundos e limpa ecra
time.sleep(5)
os.system('clear')

# Expressao while
print("Expressao while:")
x=0
y=len(lista)
while x < y:
   if lista[x] != "solaris":
       print(lista[x])
       x+=1
   else: x+=1;

