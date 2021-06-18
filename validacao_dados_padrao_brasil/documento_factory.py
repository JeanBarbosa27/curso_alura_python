from validacao_dados_padrao_brasil import doc_cpf, doc_cnpj


class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        remover_caracteres = ['.', '-', '/']

        for caractere in remover_caracteres:
            documento = documento.replace(caractere, '')

        if len(documento) == 11:
            return doc_cpf.DocCPF(documento)

        elif len(documento) == 14:
            return doc_cnpj.DocCNPJ(documento)
        else:
            raise ValueError('Quantidade inválida de dígitos!')
