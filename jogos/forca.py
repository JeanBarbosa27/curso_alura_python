import random
import json


def jogar():
    lista_de_palavras_secretas = inicia_lista_de_palavras_secretas()
    lista_de_palavras_secretas_manuseada = manuseia_lista_palavras_secretas(lista_de_palavras_secretas)
    index_palavra_secreta = sorteia_index_palavra_secreta(lista_de_palavras_secretas)
    palavra_secreta = lista_de_palavras_secretas_manuseada[index_palavra_secreta]['palavra']
    categoria_palavra_secreta = lista_de_palavras_secretas_manuseada[index_palavra_secreta]['categoria']
    dica_palavra = inicia_dica_palavra(palavra_secreta)
    chutes_errados = []
    maximo_de_erros = 6
    erros_consecutivos = []
    enforcou = False
    acertou = False

    def adicionar_chute_errado(chute):
        chutes_errados.append(chute)

    def adicionar_erro_consecutivo():
        erros_consecutivos.append(True)

    imprime_mensagem_de_boas_vindas()
    exibir_forca(len(chutes_errados))
    print(f"Dica para a palavra secreta: {mostrar_letras(dica_palavra)}", end='\n\n')

    while not acertou and not enforcou:
        chute = input('Digite uma letra: ')
        anotar_chute(
            palavra_secreta,
            chute.strip(),
            dica_palavra,
            erros_consecutivos,
            adicionar_erro_consecutivo,
            chutes_errados,
            adicionar_chute_errado,
            categoria_palavra_secreta
        )
        acertou = verifica_se_acertou_palavra_secreta(palavra_secreta, dica_palavra)
        enforcou = verifica_se_enforcou(chutes_errados, maximo_de_erros)
        exibir_forca(len(chutes_errados))

    if acertou and not enforcou:
        imprimir_mensagem_vencedor()

    if enforcou and not acertou:
        imprimir_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_de_boas_vindas():
    print("*********************************")
    print("** Bem vindo ao jogo da forca! **")
    print("*********************************")


def forca_vazia():
    print('     ___  ')
    print('    |/  | ')
    print('    |     ')
    print('    |     ')
    print('    |     ')
    print('    |     ')
    print('  __|____ ')



def forca_1_erro():
    print('     ___  ')
    print('    |/  | ')
    print('    |  (_)')
    print('    |     ')
    print('    |     ')
    print('    |     ')
    print('  __|____ ')


def forca_2_erros():
    print('     ___  ')
    print('    |/  | ')
    print('    |  (_)')
    print('    |   | ')
    print('    |     ')
    print('    |     ')
    print('  __|____ ')


def forca_3_erros():
    print('     ___  ')
    print('    |/  | ')
    print('    |  (_)')
    print('    |   |\ ')
    print('    |     ')
    print('    |     ')
    print('  __|____ ')


def forca_4_erros():
    print('     ___  ')
    print('    |/  | ')
    print('    |  (_)')
    print('    |  /|\ ')
    print('    |     ')
    print('    |     ')
    print('  __|____ ')


def forca_5_erros():
    print('     ___  ')
    print('    |/  | ')
    print('    |  (_)')
    print('    |  /|\ ')
    print('    |    \ ')
    print('    |     ')
    print('  __|____ ')


def forca_6_erros():
    print('     ___  ')
    print('    |/  | ')
    print('    |  (_)')
    print('    |  /|\ ')
    print('    |  / \ ')
    print('    |     ')
    print('  __|____ ')


def exibir_forca(quantidade_de_erros):
    if quantidade_de_erros == 0:
        forca_vazia()
    elif quantidade_de_erros == 1:
        forca_1_erro()
    elif quantidade_de_erros == 2:
        forca_2_erros()
    elif quantidade_de_erros == 3:
        forca_3_erros()
    elif quantidade_de_erros == 4:
        forca_4_erros()
    elif quantidade_de_erros == 5:
        forca_5_erros()
    elif quantidade_de_erros == 6:
        forca_6_erros()


def inicia_lista_de_palavras_secretas():
    lista = []
    palavras_e_categorias = []

    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            lista.append(linha.split(','))

    for item_index, item in enumerate(lista):
        if item_index == 0:
            continue
        palavra = lista[item_index][0].strip()
        categoria = lista[item_index][1].strip()
        palavras_e_categorias.append({'palavra': palavra, 'categoria': categoria})

    return palavras_e_categorias


def manuseia_lista_palavras_secretas(lista_de_palavras_secretas):
    objeto_lista_palavras_secretas = json.dumps(lista_de_palavras_secretas)
    lista_de_palavras_secretas_carregada = json.loads(objeto_lista_palavras_secretas)
    return lista_de_palavras_secretas_carregada


def sorteia_index_palavra_secreta(lista_de_palavras_secretas):
    return random.randrange(0, len(lista_de_palavras_secretas))


def inicia_dica_palavra(palavra):
    dica = []

    for letra in palavra:
        dica.append('_')

    return dica


def mostrar_letras(lista_de_letras):
    dica_para_exibir = ''

    for index_letra, letra in enumerate(lista_de_letras):
        dica_para_exibir = dica_para_exibir + f" {letra} "

    return dica_para_exibir if len(lista_de_letras) else None


def verifica_se_quer_dica(erros_consecutivos, categoria_palavra_secreta):
    if len(erros_consecutivos) == 3:
        resposta = input("Quer uma dica? Digite (s) para sim e (n) para não: ")
        if resposta == 's':
            print(f"Essa palavra é da categoria de: {categoria_palavra_secreta}", end='\n\n')


def anotar_chute(palavra, chute, dica, erros_consecutivos, adicionar_erro_consecutivo, chutes_errados, adicionar_chute_errado, categoria_palavra_secreta):
    errou_chute = True
    letras_certas = 0

    for posicao_letra, letra in enumerate(palavra):
        if chute.lower() == letra.lower():
            errou_chute = False
            letras_certas += 1
            dica[posicao_letra] = chute

    if errou_chute:
        adicionar_erro_consecutivo()
        adicionar_chute_errado(chute)
        print('Você errou, essa letra não faz parte da palavra secreta.', end='\n\n')
        verifica_se_quer_dica(erros_consecutivos, categoria_palavra_secreta)
    else:
        if len(erros_consecutivos):
            erros_consecutivos.clear()
        letra_singular_plural = 'letra' if letras_certas < 2 else 'letras'
        mensagem_acertos = f"Você acertou {letras_certas} {letra_singular_plural} da palavra secreta."
        print(mensagem_acertos)

    if len(chutes_errados):
        print(f"Chutes errados até o momento: {mostrar_letras(chutes_errados)}")
    print(mostrar_letras(dica), end='\n\n')


def verifica_se_acertou_palavra_secreta(palavra_secreta, dica_palavra):
    palavra_secreta_para_comparacao = []

    for letra in palavra_secreta:
        palavra_secreta_para_comparacao.append(letra)

    return palavra_secreta_para_comparacao == dica_palavra


def verifica_se_enforcou(chutes_errados, maximo_de_erros):
    return len(chutes_errados) == maximo_de_erros


def imprimir_mensagem_perdedor(palavra_secreta):
    print(f"Infelizmente não foi dessa vez! A palavra secreta era: {palavra_secreta}", end='\n\n')
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


def imprimir_mensagem_vencedor():
    print('Parabéns, você acertou a palavra antes de ser enforcado!', end='\n\n')
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

if __name__ == "__main__":
    jogar()
