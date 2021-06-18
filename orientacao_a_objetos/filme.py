from orientacao_a_objetos.programa import Programa


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        singular_ou_plural_likes = self.singular_ou_plural(self.likes, 'like', 'likes')

        return f"Filme => " \
               f"nome: {self.nome} - " \
               f"ano: {self.ano} - " \
               f"duração: {self.duracao} minutos - " \
               f"{self.likes} {singular_ou_plural_likes}"
