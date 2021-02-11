#!/usr/bin/python3
#coding: utf-8

# A função gerar senha1 é mais simples, contudo não garante uma política de senhas como:
# - 1 minúscula, 1 maiúscula, 1 caracter especial e 1 número
# - ter como primeiro caracter da senha uma letra ou número e não um caracter especial
# A 2ª função permite utilizar a política acima descrita.
# A 2ª função pode ainda ser otimizada

# Importar bibliotecas
import random, string, sys, os, time, datetime

# Exemplo de uma função para gerar senha aleatória, sem estabelecer uma política de senhas
def gerar_senha1(tamanho):
    string1 = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(string1) for i in range(tamanho))
    #Comentado - foi utilizado para debug
    #print("\nA senha aleatória utilizando a função 1 (sem política de senhas) é:", senha)
    criaficheiros(senha,"senha_funca1.txt")

# Exemplo de uma função para gerar senhas de acordo com uma política de senha pré-estabelecida
def gerar_senha2(tamanho):
    letrasmin = string.ascii_lowercase
    letrasmai = string.ascii_uppercase
    numeros = string.digits
    carespec = string.punctuation
    tudojunto = string.ascii_letters + string.digits + string.punctuation
    # Gerar aleatoriamente 1 letra minúscula
    string1 = ''.join(random.choice(letrasmin) for i in range(1))
    # Gerar aleatoriamente 1 letra maiúscula
    string2 = ''.join(random.choice(letrasmai) for i in range(1)) 
    # Gerar aleatoriamente 1 número
    string3 = ''.join(random.choice(numeros) for i in range(1))
    # Gerar aleatoriamente 1 caracter especial
    string4 = ''.join(random.choice(carespec) for i in range(1))
    # Gerar aleatoriamente uma nova string tendo como base a string1 (min), string2 (mai), string3(núm)
    string5 = ''.join(random.sample(string1+string2+string3,3))
    # Gerar aleatoriamente uma string com 4 caracteres de todos os tipos
    string6 = ''.join(random.choice(tudojunto) for i in range(4))
    # Cria uma nova string - faz o scramble de todos os restantes caracteres
    string7 = ''.join(string4+string6+string5[1:3])
    # Forma a string garantindo que a política senha
    string8 = string5[0:1]+string7
    # Se o tamanho da string for 8 gera a senha tendo em conta a criação das strings no passo anterior
    if tamanho == 8:
        senha = string8
    else:
        # Gera aleatoriamente mais caracteres a serem adicionados na senha final
        # De acordo com o tamanho da senha pretendida (subtrai os 8 carateres míminos definidos em string8)
        string9 = ''.join(random.choice(tudojunto) for i in range(tamanho-8))
        senha = string8+string9
    #Comentado - foi utilizado para debug
    #print("\nA senha aleatória utilizando a função 2 (com política de senhas) é:", senha)
    criaficheiros(senha,"senha_funca2.txt")
    
# Função para criar o ficheiro
def criaficheiros(senha,ficheiro):
    # Apaga o ficheiro se existir
    if os.path.exists(ficheiro):
        os.remove(ficheiro)
    # Cria o ficheiro
    criarfich = open(ficheiro, 'w')
    # Escreve a senha no ficheiro
    criarfich.write(senha)
    # Fecha o ficheiro
    criarfich.close()
    print("\nO ficheiro " + ficheiro + " foi criado em " + os.getcwd())
    
# Programa principal    
if __name__ == "__main__":
    try:
        # Definir variáveis
        string1 =""
        string2 =""
        string3 =""
        string4 =""
        string5 =""
        string6 =""
        string7 =""
        string8 =""
        string9 =""
        senha = ""
        letrasmin = ""
        letrasmai = ""
        numeros = ""
        carespec = ""
        tudojunto = ""
        entrada = 0
        criarfich = ""
        ficheiro = ""
        
        # Limpar ecrã
        os.system('clear')
        
        # Entrada de dados (2 letras)
        while not (entrada >= 8 and entrada <= 32):
            try:
                entrada = int(input("\nDigite o tamanho da senha (min=8 - max=32): "))
                if entrada < 8 or entrada > 32:
                    print("\nA entrada deve ser entre 8 e 32! Digite novamente")
            except ValueError:
                print("\nEntrada inválida. Digite novamente!")
                continue
        
        gerar_senha1(entrada)
        gerar_senha2(entrada)

        print("\nFim de programa!!!")

    except KeyboardInterrupt:
        print("Program terminado a pedido! Bye...")
        sys.exit()
    except:
        print("Ups, ocorreu um erro inesperado!")
        sys.exit()