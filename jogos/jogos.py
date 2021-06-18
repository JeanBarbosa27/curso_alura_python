import adivinhacao
import forca


def escolher_jogo():
    print("*********************************")
    print("*********** Bem vindo! **********")
    print("*********************************")

    print("Qual jogo você deseja jogar?")
    jogo_escolhido = int(input("Digite (1) para adivinhação e (2) para forca: "))


    if jogo_escolhido == 1:
        print('Jogando Adivinhação')
        adivinhacao.jogar()
    elif jogo_escolhido == 2:
        print('Jogando Forca')
        forca.jogar()

if __name__ == '__main__':
    escolher_jogo()
