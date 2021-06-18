from collections import Counter


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(caractere, contagem / total_de_caracteres) for caractere, contagem in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, frequencia in mais_comuns:
        print('{} => {:.2f}%'.format(caractere, frequencia * 100))


if __name__ == '__main__':
    texto1 = '''
        Até agora temos uma lista de contatos em que, ao menos, cada contato tem seu nome e telefone conectados. Entretanto, por enquanto, só conseguimos acessar um contato individualmente pela sua posição na lista, e não pelo seu próprio nome.

        O ideal seria mapear o nome de cada contato com seu telefone, evitando outros problemas.

        Por exemplo, podemos falar que o contato Yan tem o número de telefone 1234-5678. Assim, quando quisermos saber qual o n de telefone do Yan, basta ir até o seu nome. Dessa forma, não precisamos decorar qual a posição na lista que o telefone se encontra, basta sabermos seu nome de contato.
        
        Veja que, nesse caso, estamos criando uma espécie de dicionário, parecido com os dicionários de língua portuguesa, ou inglesa. Nesses dicionários, temos uma chave que é a palavra que estamos a buscar, que no nosso caso é o nome de contato.
        
        Quando achamos essa palavra, podemos ver o seu significado, isto é, o valor daquela palavra na língua, que no nosso caso, é o número de telefone.
    '''

    texto2 = '''
        Ué, não deveria ordenar? Deveria, mas precisamos primeiro pensar nas seguintes questões:

        Como ordenamos um objeto do tipo Produto?
        Pelo atributo nome? Ou pelo valor?
        Observe que inicialmente não sabemos, pois em determinados momentos, podemos querer ordenar por nome ou por valor. Em outras palavras, o sorted, inicialmente, também não sabe como ordenar o nosso objeto!
        
        Suponhamos que queremos ordenar por nome, como o sorted saberia disso? Não informamos em nenhum momento!
        
        Portanto, quando queremos ordenar um objeto do tipo Produto, precisamos informar por qual atributo ele será ordenado!
    '''
    print('Texto 1')
    analisa_frequencia_de_letras(texto1)
    print('Texto 2')
    analisa_frequencia_de_letras(texto2)
