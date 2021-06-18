import random
import json


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    numero_minimo_aceitavel = 1
    numero_maximo_aceitavel = 100
    pontos = 1000

    print("Escolha seu nível de dificuldade", numero_secreto)
    nivel = input("Digite 1 para fácil, 2 para médio e 3 para difícil: ")

    dicionario_dificuldade = {
        "1": {
            "maximo_tentativas": 20,
            "dificuldade": "fácil"
        },
        "2": {
            "maximo_tentativas": 10,
            "dificuldade": "médio"
        },
        "3": {
            "maximo_tentativas": 5,
            "dificuldade": "difícil"
        },
    }

    objeto_dificuldade = json.dumps(dicionario_dificuldade)
    dificuldade = json.loads(objeto_dificuldade)

    total_de_tentativas = dificuldade[nivel]["maximo_tentativas"]

    print(f"No nível {dificuldade[nivel]['dificuldade']} você terá um total de {total_de_tentativas} tentativas", end='\n\n')

    for rodada in range(1, total_de_tentativas + 1):
        chute_str = input(f"Digite um número entre {numero_minimo_aceitavel} e {numero_maximo_aceitavel}: ")
        print("Você digitou o número ", chute_str)
        chute = int(chute_str)
        chute_fora_dos_limites = chute < numero_minimo_aceitavel or chute > numero_maximo_aceitavel

        if chute_fora_dos_limites:
            print(f"Opção inválida, por favor insira um número entre {numero_minimo_aceitavel} e {numero_maximo_aceitavel}")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if acertou:
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            maior_ou_menor = ""
            if chute_maior:
                maior_ou_menor = "maior"
            elif chute_menor:
                maior_ou_menor = "menor"

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            # duas formas de interpolar strings em Python
            print(f"Você errou! O seu chute é {maior_ou_menor} do que o número secreto.", end=' ')

            # dessa forma é possível acessar outras funcionalidades
            # como por exemplo alterar a ordem de exibição dos parâmetros do método format
            print("Essa foi a tentativa {1} de {0}".format(total_de_tentativas, rodada), end='\n\n')
            if rodada == total_de_tentativas:
                print(f"O número secreto era {numero_secreto}!")

    print("Fim de jogo!")


if __name__ == "__main__":
    jogar()
