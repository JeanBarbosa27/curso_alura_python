from validate_docbr import CNPJ


class DocCNPJ:
    def __init__(self, documento):
        if self.cnpj_eh_valido(documento):
            self.documento = documento
        else:
            raise ValueError('CNPJ é inválido!')

    def cnpj_eh_valido(self, documento):
        cpf = CNPJ()
        return cpf.validate(documento)

    def adiciona_mascara(self):
        cpf = CNPJ()
        return cpf.mask(self.documento)

    def __str__(self):
        return self.adiciona_mascara()
