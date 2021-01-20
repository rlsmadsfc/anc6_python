#!/usr/bin/python3

# Este programa não valida permissões de escrita na diretoria onde os ficheiros serão criados
# Executar o programa em uma diretoria com permissoes de escrita para poder criar ficheiros

# Importar bibliotecas para manusear ficheiros, funçoes de tempo e comandos OS
import os.path
import time
import os

# Declarar variaveis e abrir listas
iplista = []
portolista = []
ipfixo = "192.168.1."

# Cria ficheiros (se existirem, apaga os ficheiros existentes)
if os.path.exists("ipLista.txt"):
    os.remove("ipLista.txt")
iplistafic = open("ipLista.txt","w")

if os.path.exists("portoLista.txt"):
    os.remove("portoLista.txt")
portolistafic = open("portoLista.txt","w")

# Cria lista de IPs (adiciona 0 a 255 a lista de ip)
for seqip in range(1,256):
   iplista.append(ipfixo+str(seqip))

# Cria lista de portos de 1 a 1024
for seqporto in range(1,1025):
    portolista.append(str(seqporto))

# Grava lista de IPs no ficheiro de IPs - funcao write (linha a linha) - imprime resultados no ecra
for x in iplista:
     print(x)
     iplistafic.write(x)
     iplistafic.write('\n')

# Temporizador para visualizar as diferentes impressoes / limpa terminal
time.sleep(3)
os.system('clear')

# Grava lista de Portos no ficheiro de Portos - funcao print - imprime resultados no ecra
# Instruçẽs abaixo comentados para poder demonstrar a alternativa do print
#     portolistafic.write(y)
#     portolistafic.write('\n')
for y in portolista:
    print(y)
    print(y, file=portolistafic)

# Fecha ficheiros
iplistafic.close()
portolistafic.close()

# Comentado - utilizado para visualizar as listas criadas - testes apenas
# print(iplista)
# print(portolista)
 