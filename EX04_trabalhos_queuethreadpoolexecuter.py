#!/usr/bin/python3
#coding: utf-8
# Este código pode ser otimizado
# Foi desenvolvido para correr em Linux
# Esta versão utilizando queues e threadpoolsexecutor ainda está em desenvolvimento
# Um dos desafios é fazer a barra de progresso para as threads em execução versus as terminadas

# Importar bibliotecas
import random, string, sys, os, time, datetime, zipfile, threading, concurrent.futures, psutil, logging, random
from tqdm import tqdm
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

#logging.basicConfig(level=logging.DEBUG,
#                    format='(%(threadName)-9s) %(message)s',)

#Função para extrair ficheiro
def extrair_ficheiro(ficheiro_zip,senha_cod,dirExtrair):
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
        pass
    else:
        print("[+] A senha encontrada é: " + senha_cod.decode())
        print("[+] O conteúdo do ficheiro zip foi extraído para: " + dirExtrair)
        tfinal = time.time()
        tfinalStr = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(tfinal))
    
        # Calcula o tempo de execução
        ttotal = tfinal - tinicio
    
        print("Inicio do brutal force ao ficheiro zip " + str(tinicioStr))
        print("Fim do brutal force ao ficheiro zip: " + str(tfinalStr))
        print(f"O brutal force foi executado em: {ttotal} seg")
        
        current_system_pid = os.getpid()
        ThisSystem = psutil.Process(current_system_pid)
        ThisSystem.terminate()
        exit(0)

# Definição do worker para multi threading
def worker():
    while not queue.empty():
        senha_cod = queue.get()
        extrair_ficheiro(ficheiro_zip,senha_cod,dirExtrair)

# Definição da função de threading
def super_thread():
    thread = threading.Thread(target=worker)
    thread_list.append(thread)


if __name__ == '__main__':

    # Declara variável
    msg_ajuda = "\nUtilize: python3 -help para obter ajuda!"
    queue = Queue()
    thread_list = []
    senhaencontrada = False
    
    # Limpar ecrã
    os.system('clear')

    # ficheiro = "-help"
    #if len(sys.argv) > 1 and sys.argv[1] == "-help":
    #    print("\nPara executar este programa digite: python3 " + sys.argv[0] + " <nome do ficheiro zip> <nome do ficheiro de senha>")
    #    print("\nExemplo: python3 " + sys.argv[0] +" ficheiro.zip dicionario.txt\n")
    #    sys.exit(0) # Encerra a execução do programa
    #elif len(sys.argv) < 3:        
    #    print("\nNúmero incorreto de argumentos!")
    #    print(msg_ajuda)
    #    sys.exit(0) # Encerra a execução do programa
    
    # Adiciona argumentos as variáveis
    #ficheiro = sys.argv[1]
    #dicionario = sys.argv[2]
    
    ficheiro = "private.zip"
    dicionario = "rockyou2.txt"
    #dicionario = "dicionario.txt"

    # Verifica se os ficheiros existem
    if os.path.exists(ficheiro) == False:
       print("\nFicheiro zip " + ficheiro + " não encontrado")
       print(msg_ajuda)
       sys.exit(0) # Encerra a execução do programa

    if os.path.exists(dicionario) == False:
        print("\nFicheiro de senha " + dicionario + " não encontrado")
        print(msg_ajuda)
        os._exit(1)
        sys.exit(0) # Encerra a execução do programa

    #Função para gestão da diretoria onde será extraído o zip
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

    ficheiro_zip = zipfile.ZipFile(os.getcwd()+"/"+ficheiro)
    n_palavras = len(list(open(dicionario, "rb")))

    # Inicia o brutal force (regista inicio)
    tinicio = time.time()
    tinicioStr = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(tinicio))
    
    senha = None
    print("\nInicio do brutal force ao ficheiro zip " + str(tinicioStr))
    print("\nA preparar execução em threads")
    print("Total de senhas a testar e incluir na queue: " + str(n_palavras))

    thread_lock = threading.Lock()
       
    t_workers = 100
    t_threads = 5000
    
    with open(dicionario, "rb") as dicionario:
         for senha in tqdm(dicionario, total=n_palavras, unit=" senha "):
             senha_cod = senha.strip()
             queue.put(senha_cod)
        
    with concurrent.futures.ThreadPoolExecutor(max_workers=t_workers) as executor:
        for t in range(t_threads):
            executor.submit(super_thread)

    # Gestão das threads
    #for thread in thread_list:
    #    thread.start()
    
    print("\nTotal de threads a executar: " + str(len(thread_list)))

#    for thread in thread_list:
#        thread.daemon = True
#        thread.start()

    for thread in tqdm(thread_list, total=len(thread_list), unit=" threads "):
        thread.daemon = True
        thread.start()

#    main_thread = threading.current_thread()
#    for t in threading.enumerate():
#	    if t is main_thread:
#		        continue
#	    logging.debug('joining %s', t.getName())
#	    t.join()
    
    for thread in thread_list:
        thread.join()

    # Termina o brutal force
    tfinal = time.time()
    tfinalStr = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(tfinal))
    
    # Calcula o tempo de execução
    ttotal = tfinal - tinicio
    
    #print("Threads em execucação: ")
    #for thread in tqdm(thread_list, total=len(thread_list), unit=" threads "):
    #    thread.join()
        
    print("[!] Senha não encontrada!")
    print("\nFim do brutal force ao ficheiro zip: " + str(tfinalStr))
    print(f"\nO brutal force foi executado em: {ttotal} seg")

