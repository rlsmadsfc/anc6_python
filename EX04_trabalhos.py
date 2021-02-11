#!/usr/bin/python3
#coding: utf-8
# Este código pode ser otimizado
# Foi desenvolvido para correr em Linux

# Importar bibliotecas
import random, string, sys, os, time, datetime, zipfile
from tqdm import tqdm

#Função para gestão da diretoria onde será extraído o zip
def CriaDir():
    #Cria uma diretoria para descompactar o ficheiro zip
    #Se a diretoria exitir, renomeia e cria uma nova
    dirExtrair = '/tmp/extrair'    
    direxiste = os.path.isdir(dirExtrair)
    if direxiste == True:
        modTimeDir = os.path.getmtime(dirExtrair)
        newTime = time.strftime('%Y%m%d%H%M%S', time.localtime(modTimeDir))
        newDir = dirExtrair + "-" + newTime
        os.rename(dirExtrair,newDir)
    os.mkdir(dirExtrair)
    return(dirExtrair)

#Função para extrair ficheiro
def descobre_senha_forca_bruta(ficheiro,dicionario,dirExtrair):
    #Prepara o ficheiro zip
    ficheiro_zip = zipfile.ZipFile(os.getcwd()+"/"+ficheiro)
    #Prepara o dicionário de palavras (senhas mais comuns)
    n_palavras = len(list(open(dicionario, "rb")))

    senha = None
    print("Total de senhas a testar: " + str(n_palavras))

    #Executa extração
    #Trata das exceções com try e except
    with open(dicionario, "rb") as dicionario:
        #A biblioteca tqdm permite gerar uma barra de progresso
        for senha in tqdm(dicionario, total=n_palavras, unit=" senha "):
            senha_cod = senha.strip()
            try:
                #Executa a extração do ficheiro zip
                ficheiro_zip.extractall(dirExtrair, pwd=senha_cod)
            except Exception as e:
                if "Bad password for file" in str(e):
                    pass
                elif "Erro -3 enquanto unzip" in str(e):
                    pass
                else:
                    pass
            except KeyboardInterrupt:
                print("Program terminado a pedido! Bye...")
                sys.exit()
            except:
                continue
            else:
                print("[+] A senha encontrada é: " + senha_cod.decode())
                print("[+] O conteúdo do ficheiro zip foi extraído para: " + dirExtrair)
                exit(0)

    print("[!] Senha não encontrada, tente outra lista de senhas.")


if __name__ == '__main__':

    # Declara variável
    msg_ajuda = "\nUtilize: python3 -help para obter ajuda!"
    
    # Limpar ecrã
    os.system('clear')

    # ficheiro = "-help"
    if len(sys.argv) > 1 and sys.argv[1] == "-help":
        print("\nPara executar este programa digite: python3 " + sys.argv[0] + " <nome do ficheiro zip> <nome do ficheiro de senha>")
        print("\nExemplo: python3 " + sys.argv[0] +" ficheiro.zip dicionario.txt\n")
        sys.exit(0) # Encerra a execução do programa
    elif len(sys.argv) < 3:        
        print("\nNúmero incorreto de argumentos!")
        print(msg_ajuda)
        sys.exit(0) # Encerra a execução do programa
    
    # Adiciona argumentos as variáveis
    ficheiro = sys.argv[1]
    dicionario = sys.argv[2]
    
    # Verifica se os ficheiros existem
    if os.path.exists(ficheiro) == False:
       print("\nFicheiro zip " + ficheiro + " não encontrado")
       print(msg_ajuda)
       sys.exit(0) # Encerra a execução do programa

    if os.path.exists(dicionario) == False:
        print("\nFicheiro de senha " + dicionario + " não encontrado")
        print(msg_ajuda)
        sys.exit(0) # Encerra a execução do programa

    # Executa as funções
    dirExtrai = CriaDir()
    descobre_senha_forca_bruta(ficheiro,dicionario,dirExtrai)
