#!/usr/bin/python3
#coding: utf-8

# Importar bibliotecas
import sys, os, time, datetime

def convseg(escolha):
    horas = escolha // 3600
    minutos = escolha % 3600 // 60
    segundos = escolha % 3600 % 60
    return "%d:%02d:%02d" % (horas, minutos, segundos)
#    return (horas,minutos,segundos)

# Program principal #
if __name__ == "__main__":

    try:
        # Definição de variáveis
        loop1 = True
        loop2 = True
        escolha = int()
        
        # Limpar ecrã
        os.system('clear')
    
        # Loop para digitar os segundos
        while loop1:
            try:
                escolha = int(input("\nDigite os segundos (número inteiro e positivo) a converter: "))
            except ValueError:
                print("\nDigite um número inteiro e positivo!")
                continue
            #Comentado - foi utilizado para testes e debug
            #print(type(escolha))
            #print(isinstance(escolha, int))
            if (isinstance(escolha, int)) == True:
                if escolha > 0:
                    print("\nA conversão de " + str(escolha) +" segundos para horas:minutos:segundos (hh:mm:ss) é: " + convseg(escolha))
                    loop2 = True
                    # O objetivo desta opção é demonsrar uma outra função de conversão
                    if escolha > 86400:
                        while loop2:
                            simounao = input("\nQuer converter este resultado em dias:horas:minutos:segundos (Digite S para Sim ou N para Não? ")
                            if simounao == "S":
                                print("\nA conversão para dias:horas:minutos:segundos (dd:hh:mm:ss) é: " + str(datetime.timedelta(seconds = escolha)))
                                loop2 = False
                            elif simounao == "N":
                                loop2 = False
                            else:
                                print("\nDigite S para Sim ou N para Não!")
                                loop2 = True
                    loop1 = False
                else:
                    print("\nDigite um número inteiro e positivo!")            
        print("\nFim de programa!!!")
    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()

