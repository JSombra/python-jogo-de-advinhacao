def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "folgada"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = input("Qual a letra?: ")
        chute.strip()
        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index += 1
            letras_faltando = str(letras_acertadas.count("_"))
        print("Ainda faltam {} letras não advinhadas".format(letras_faltando))
        print(letras_acertadas)
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
 