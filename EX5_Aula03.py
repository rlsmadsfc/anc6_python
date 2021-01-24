#!/usr/bin/python3
#coding: utf-8

# Executar este programa em uma diretoria com permissões de escrita
# A diretoria /tmp deverá ter permissões de escrita para quem for executar este programa
# A próxima versão deste programa irá salvar os logs numa base de dados mysql

# Importar bibliotecas
import sys, os, socket, time, datetime, subprocess, ipaddress, threading, concurrent.futures
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


# Definicão da Função Port Scanner
def PortScanner(endIP, Porto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criar um socket
        resultado = sock.connect_ex((endIP, Porto)) # conectar socket ao destino

        if resultado == 0: # validar se a porta está "open, filtered ou closed"
            # Adiciona o Porto a lista de Portas abertas
            ListaPortosAbertos.append(Porto)
            with print_lock:
                print("A porta " + str(Porto) + " está aberta") # imprimir resultado no ecrã
            sock.close()
            return True
        else:
            # Adiciona o Porto a lista de Portas fechadas            
            ListaPortosFechados.append(Porto)
            with print_lock:
                print("A porta " + str(Porto) + " está fechada") # imprimi resultado no ecrã
            sock.close()
            return False

    except KeyboardInterrupt:
        print("Programa terminado a pedido! Bye...")
        print("Programa terminado a pedido! Bye...", file=ficipscan)
        ficipscan.close()
        sys.exit()

    except socket.gaierror:
        print("Endereco IP não foi resolvido")
        print("Endereco IP não foi resolvido", file=ficipscan)
        ficipscan.close()
        sys.exit()

    except socket.error:
        print("Não foi possivel conectar ao IP")
        print("Não foi possivel conectar ao IP", file=ficipscan)
        ficipscan.close()
        sys.exit()

    except:
        print("Ocorreu um erro inesperado!")
        print("Ocorreu um erro inesperado na função Scanner!", file=ficipscan)
        ficipscan.close()
        sys.exit()

# Definição da função valida endereço IP
def valida_ip(endIP):
   try:
      # Verifica tipo de IP
      ipTipo=type(ipaddress.ip_address(endIP))
      print("", file=ficipscan)
      print("Endereço IP: " + str(endIP), file=ficipscan)

      if str(ipTipo).find("IPv4") != -1:
         ipCateg = "IPv4"
         print("É da classe IPv4")
         print("É da classe IPv4", file=ficipscan)
         return ipCateg, True

      if str(ipTipo).find("IPv6") != -1:
         ipCateg = "IPv6"
         print("Este programa ainda não suporta testes ao IPv6")
         print("Este programa ainda não suporta testes ao IPv6", file=ficipscan)
         return ipCateg, False

   except ValueError:
      ipCateg = ""  
      return ipCateg, False

# Definição do worker para multi threading
def worker():
    while not queue.empty():
        Porto = queue.get()
        PortScanner(endIP,Porto)

# Definição da função de threading
def super_thread():
    thread = threading.Thread(target=worker)
    thread_list.append(thread)


# Program principal #
if __name__ == "__main__":

    # Declaração de varíaveis e listas
    queue = Queue()
    ListaPortosAbertos = []
    ListaPortosFechados = []
    thread_list = []

    # Faz o lock da thread durante a impressão para que se realize uma impressão limpa
    print_lock = threading.Lock()

    # Limpar ecrã
    os.system('clear')
    print("\n \nPressione Ctrl+c para interromper para interromper o programa \n \n")

    # Criar diretoria em tmp
    diretoria="/tmp/Scans"
    direxiste=os.path.exists(diretoria)

    # Valida se a diretoria já existe
    if direxiste == False:
        os.mkdir(diretoria)

    # Muda para a diretoria pretendida
    os.chdir(diretoria)

    # Valida se ficheiro de log existe. Se existir renomeia
    if os.path.exists("PortScan.txt"):
        modTimeFic = os.path.getmtime("PortScan.txt")
        newTime = time.strftime('%Y%m%d%H%M%S', time.localtime(modTimeFic))
        newFic = "PortScan-" + newTime + ".txt"
        os.rename("PortScan.txt",newFic)

    # Cria ficheiro de log
        ficipscan = open("PortScan.txt", "w")
        ficipscan.write("Port Scanner \n")

    # Entrada de dados
    # Poderia ter incluído isto numa função ao invés da função principal
    try:
        while True:
            endIP    = input("Digite o endereço IP: ")

            print("A validar endereço IP! Aguarde por favor!")

            # Chama função valida IP
            ClasseIP,CondIP=valida_ip(endIP)
       
            if CondIP == True and ClasseIP == "IPv4":
                print("Este IP é válido!")
                ficipscan.write("Este IP é válido!")
                IPteste = os.system("ping -c 1 " + endIP + " >/dev/null 2>&1")
                if IPteste == 0:
                    print("Está ativo e a responder aos pedidos!")
                    ficipscan.write("Está a responder aos pedidos \n \n")
                    break
                else:
                    print("Mas, não está a responder aos pedidos!")
                    print("Tente novamente!")
                    ficipscan.write(" Mas, não está a responder aos pedidos \n \n")
                    continue
            elif CondIP == False and ClasseIP == "IPv6":
                continue
            else:
                print()
                print("Este IP (" + endIP + ") nao é valido! Tente novamente!")
                ficipscan.write("Este IP (" + endIP + ") não é válido \n \n")
                continue

        # Inicia Scan (regista inicio)
        tinicio = time.time()
        tinicioStr = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(tinicio))
        ficipscan.write("Inicio do scan das portas: " + str(tinicioStr))

        # Cria a queue para o número de portos (65536)
        thread_lock = threading.Lock()
        for Porto in range(1, 65536):
            queue.put(Porto)
        
        # O desempenho do programa depende de como se joga com estas duas variáveis: t_workers e t_threads
        # O rácio entre workers e threads é mais ef# Faz o lock da thread durante a impressão para que se realize uma impressão limpa
        # - um número menor de workers (ex. 10) e um número maior de threads (ex. 1000) - limitado sempre aos recurso de SO)
        # - testes em uma rede local demonstraram se possível fazer o scan de 65535 portas em cerca de 25 segundos
        t_workers = 10
        t_threads = 1000

        # Define um timeout para para o socket (0.25 mostrou-se suficiente para a maioria dos testes)
        # Contudo, este pode impactar no tempo de execução do programa
        t_socketTimeout = 0.25
        socket.setdefaulttimeout(t_socketTimeout)
        
        # Executa ThreadPoolExecutor - chama a função supert_thread que irá chamar a função Port Scanner
        with concurrent.futures.ThreadPoolExecutor(max_workers=t_workers) as executor:
            for t in range(t_threads):
                executor.submit(super_thread)

        # Gestão das threads
        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()

    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        print("Program terminado a pedido! Bye...", file=ficipscan)
        ficipscan.close()
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado no programa principal!")
        print("Ups, ocorreu um erro inesperado no programa principal!", file=ficipscan)
        ficipscan.close()
        sys.exit()

    # Termina scan
    tfinal = time.time()
    tfinalStr = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(tfinal))
    ficipscan.write("\nFim do scan: " + str(tfinalStr) + "\n \n")

    # Calcula o tempo de execução
    ttotal = tfinal - tinicio
    print(f"O Port Scanner foi executado em:  {ttotal} seg \n", file=ficipscan)
    print(f"O Port Scanner foi executado em:  {ttotal} seg")
        
    # Ordena a lista de portos
    ListaPortosAbertos.sort()
    ListaPortosFechados.sort()
    TotalPortos = len(ListaPortosAbertos) + len(ListaPortosFechados)

    # Imprime resultados no ficheiro de log
    print("Resultado do Scan para " + str(TotalPortos) + " portas: \n", file=ficipscan)
        
    for iPortosAbertos in ListaPortosAbertos:
        print("A porta: " + str(iPortosAbertos) + " está aberta", file=ficipscan)

    print("", file=ficipscan)
    for iPortosFechados in ListaPortosFechados:
        print("A porta: " + str(iPortosFechados) + " está fechada", file=ficipscan)
    
    # Fecha o ficheiro de log
    ficipscan.close()

