import random


print("*******************")
print("Jogo de Advinhação!")
print("*******************")


numero_secreto =  random.randint(1, 100)
numero_jogador = random.randint(1, 100)
contador_de_tentativas = 0

while (numero_secreto != numero_jogador):
    print("Você Errou. Número chutado foi {} e o número secreto foi {}".format(numero_jogador, numero_secreto))
    numero_secreto =  random.randint(1, 100)
    numero_jogador = random.randint(1, 100)
    contador_de_tentativas = contador_de_tentativas + 1
else:
    print("Parabéns, você acertou o número. {} = {}".format(numero_secreto, numero_jogador))

print("Fim do Jogo")

print("\nForam necessárias {} tentativas para encontrar o número correto".format(contador_de_tentativas))