class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.string_eh_valida(url):
            self.url = url.lower()
        else:
            raise LookupError('A URL informada é inválida!')

    def encontra_indice_inicio_substring(self, busca_moeda):
        tamanho_busca_moeda = len(busca_moeda)
        return self.url.find(busca_moeda) + tamanho_busca_moeda

    def corrige_moeda_origem(self, moeda_origem):
        return moeda_origem.replace('moedadestino', 'real')

    def retorna_valor(self):
        busca_valor = 'valor='.lower()
        tamanho_substring_valor = len(busca_valor)
        inicio_substring_valor = self.url.find(busca_valor) + tamanho_substring_valor
        return self.url[inicio_substring_valor:]

    def retorna_moedas(self):
        busca_moeda_origem = 'moedaorigem='.lower()
        busca_moeda_destino = 'moedadestino='.lower()

        inicio_substring_moeda_origem = self.encontra_indice_inicio_substring(busca_moeda_origem)
        fim_substring_moeda_origem = self.url.find('&')

        inicio_substring_moeda_destino = self.encontra_indice_inicio_substring(busca_moeda_destino)
        fim_substring_moeda_destino = self.url.find('&valor')

        moeda_origem = self.url[inicio_substring_moeda_origem:fim_substring_moeda_origem]
        moeda_destino = self.url[inicio_substring_moeda_destino:fim_substring_moeda_destino]
        valor = self.retorna_valor()

        if moeda_origem == 'moedadestino':
            moeda_origem = self.corrige_moeda_origem(moeda_origem)

        return moeda_origem, moeda_destino

    @staticmethod
    def string_eh_valida(url):
        if url:
            return True
        else:
            return False

    def __str__(self):
        moeda_origem, moeda_destino = self.retorna_moedas()
        valor = self.retorna_valor()
        return f"Valor: {valor}\nMoeda Origem: {moeda_origem}\nMoeda Destino {moeda_destino}"

    def __len__(self):
        return len(self.url)

    def __eq__(self, outra_instancia):
        return self.url == outra_instancia.url
