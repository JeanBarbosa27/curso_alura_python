from manipulacao_strings.extrator_argumentos_url import ExtratorArgumentosUrl


url = 'https://www.bytebank.com.br/cambio?moedaOrigem=moedadestino&moedaDestino=dolar&valor=1500'
argumentos = ExtratorArgumentosUrl(url)
argumentos2 = ExtratorArgumentosUrl(url)

moeda_origem, moeda_destino = argumentos.retorna_moedas()
valor = argumentos.retorna_valor()

print(f"Representação da instância: \n{argumentos}\n")
print(f"Tamanho da instância: {len(argumentos)}")
print(f"Comparação de instâncias: {argumentos == argumentos2}")
