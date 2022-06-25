import random

def jogo():
    print("---------------------------------")
    print("Bem Vindo ao Jogo de Advinhação!")
    print("---------------------------------\n")


    numero_secreto =  random.randint(1, 100)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Digite a dificuldade do jogo desejada. \n1 - Fácil (20 tentativas) \n2 - Intermediário (10 tentativas) \n3 - Difícil (5 tentativas)")
    dificuldade = int(input("\nDigite apenas o número correspondente: "))

    if (dificuldade) == 1:
        total_tentativas = 20
    elif (dificuldade) == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("\n********************************")
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        print("********************************")
        
        numero_jogador = int(input("\n\nDigite um número: "))

        if(numero_jogador < 1 or numero_jogador > 100):
            print("\nVocê deve chutar um número entre 1 e 100!")
            continue

        acertou = numero_jogador == numero_secreto
        maior   = numero_jogador > numero_secreto
        menor   = numero_jogador < numero_secreto
        if(acertou):
            print("\nParabéns, você acertou o número e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("\nO Chute foi maior que o número secreto")
            elif (menor):
                print("\nO Chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - numero_jogador)
            pontos = pontos - pontos_perdidos
        rodada += 1    
    print("\nFim do jogo, o número correto era {}\n".format(numero_secreto))
if(__name__ == "__main__"):
    jogo()