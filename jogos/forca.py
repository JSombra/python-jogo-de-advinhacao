def jogar():
    print("\033[1;90;100m*********************************\033[m")
    print("\033[1;90;100m***Bem vindo ao jogo da Forca!***\033[m")
    print("\033[1;90;100m*********************************\033[m")

    palavra_secreta = "folgada".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 6
    print("\n{}".format(letras_acertadas))

    while(not enforcou and not acertou):
        chute = input("Qual a letra?: ")
        chute = chute.strip().upper()
        index = 0

        if(len(chute) > 1):
            print("\n\033[1;30;41mEscreva apenas uma letra de cada vez\033[m")
        else:
            if(chute in palavra_secreta):
                for letra in palavra_secreta:
                    if(chute == letra):
                        letras_acertadas[index] = letra
                    index += 1

            else:
                tentativas -=1
                print("\nOps, Você errou ainda restam {} tentativas".format(tentativas))
            enforcou = tentativas == 0
            acertou = "_" not in letras_acertadas
            print("\n{}".format(letras_acertadas))
            
    if(acertou):
        print("\n\033[0;30;42mVocê acertou a palavra.\033[m")
    else:
        print("\n\033[1;30;43mVocê não descobriu a palavra.\033[m")
    
    print("\nFim do jogo")


if(__name__ == "__main__"):
    jogar()
 