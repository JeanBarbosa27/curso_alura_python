import requests


class Endereco:
    def __init__(self, cep):
        self.endereco_completo = ''
        cep = str(cep).replace('-', '')

        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido!')

    def valida_cep(self, cep):
        return len(cep) == 8

    def consulta_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json"
        resposta = requests.get(url)

        self.endereco_completo = resposta.text
        dados = resposta.json()

        return dados['bairro'], dados['localidade'], dados['uf']

    def __str__(self):
        self.consulta_cep()
        return self.endereco_completo
