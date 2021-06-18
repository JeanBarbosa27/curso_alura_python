from validate_docbr import CPF


class DocCPF:
    def __init__(self, documento):
        if self.cpf_eh_valido(documento):
            self.documento = documento
        else:
            raise ValueError('CPF é inválido!')

    def cpf_eh_valido(self, documento):
        cpf = CPF()
        return cpf.validate(documento)

    def adiciona_mascara(self):
        cpf = CPF()
        return cpf.mask(self.documento)

    def __str__(self):
        return self.adiciona_mascara()
