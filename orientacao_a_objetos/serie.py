from orientacao_a_objetos.programa import Programa


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        singular_ou_plural_temporadas = self.singular_ou_plural(self.temporadas, 'temporada', 'temporadas')
        singular_ou_plural_likes = self.singular_ou_plural(self.likes, 'like', 'likes')

        return f"Série => " \
               f"nome: {self.nome} - " \
               f"ano: {self.ano} - " \
               f"{self.temporadas} {singular_ou_plural_temporadas} - " \
               f"{self.likes} {singular_ou_plural_likes}"
