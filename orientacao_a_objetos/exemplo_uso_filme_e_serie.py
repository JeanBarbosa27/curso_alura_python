from orientacao_a_objetos.filme import Filme
from orientacao_a_objetos.serie import Serie
from orientacao_a_objetos.playlist import Playlist

def exibir_playlist():
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    vingadores.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()

    atlanta = Serie('atlanta', 2018, 2)
    atlanta.dar_like()
    atlanta.dar_like()

    gambito_rainha = Serie('o gambito da rainha', 2020, 1)
    gambito_rainha.dar_like()

    """
    Exemplo de como usar uma classe de forma iterável (com o for in e com o len, já que usamos o __getitem__ na
    sua definição.
    """
    playlist = Playlist('Fim de semana', [vingadores, atlanta, gambito_rainha])

    for programa in playlist:
        print(programa)

    """
    Como também definimos o __len__ nessa classe, torna-se possível utilizar a verificação do tamanho,
    como se fosse um list
    """
    print(f"Tamanho da playlist: {len(playlist)}")

if __name__ == '__main__':
    exibir_playlist()
