import re


class Telefone:
    def __init__(self, telefone):
        self.padrao = '(\\d{2,3})?(\\d{2})(\\d{4,5})(\\d{4})'

        if self.telefone_eh_valido(telefone):
            self.telefone = telefone
        else:
            raise ValueError('Número de telefone inválido')

    def telefone_eh_valido(self, telefone):
        resposta = re.findall(self.padrao, telefone)
        return resposta

    def __str__(self):
        grupos = re.search(self.padrao, self.telefone)

        sinal_mais = '+' if grupos.group(1) else ''
        codigo_pais = f"{grupos.group(1)} " if grupos.group(1) else ''
        codigo_area = grupos.group(2)
        primeira_parte_telefone = grupos.group(3)
        segunda_parte_telefone = grupos.group(4)

        return f"{sinal_mais}{codigo_pais}({codigo_area}) {primeira_parte_telefone}-{segunda_parte_telefone}"
