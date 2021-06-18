class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def singular_ou_plural(self, propriedade, texto_singular, texto_plural):
        return texto_plural if propriedade > 1 else texto_singular

    def __str__(self):
        singular_ou_plural = self.singular_ou_plural(self.likes, 'like', 'likes')
        return f"Programa => nome: {self.nome} - ano: {self.ano} - {self.likes} {singular_ou_plural}"
