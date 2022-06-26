import random

def jogar():

    imprime_boas_vindas()
    palavra_secreta = define_palavra()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print("\n{}".format(letras_acertadas))

    enforcou = False
    acertou = False
    erros = 6
    letras_utilizadas = []
    
    while(not enforcou and not acertou):
        chute = solicita_dado()

        if(len(chute) > 1):
            print("\n\033[1;30;41mEscreva apenas uma letra de cada vez\033[m")
        else:
            if(chute in palavra_secreta):
                marca_acerto(chute, letras_acertadas, palavra_secreta)
                letras_utilizadas.append(chute)
            else:
                letras_utilizadas.append(chute)
                erros -=1
                print("\nOps, Você errou ainda restam {} tentativas".format(erros))
                desenha_forca(erros)

            enforcou = erros == 0
            acertou = "_" not in letras_acertadas
            print("\n{}".format(letras_acertadas))

        print("Letras Utilizadas até o momento \033[1;30;42m{}\033[m".format(letras_utilizadas))
        
            
    if(acertou):
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_boas_vindas():
        print("\033[1;90;100m*********************************\033[m")
        print("\033[1;90;100m***Bem vindo ao jogo da Forca!***\033[m")
        print("\033[1;90;100m*********************************\033[m")

def imprime_mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def define_palavra():
    arquivo = open("/home/je/Projects/curso-python/jogos/palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)
    arquivo.close()

    numero_palavra = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero_palavra]
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def solicita_dado():
    chute = input("Qual a letra?: ")
    chute = chute.strip().upper()
    return chute
        
def marca_acerto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1



if(__name__ == "__main__"):
    jogar()