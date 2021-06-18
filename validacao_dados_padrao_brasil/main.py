from validacao_dados_padrao_brasil import documento_factory, telefone, datas_br, endereco

documento = {
    'cpf': {
        'numero': {
            'certo': 11513972707,
            'errado': 1151397270
        },
        'string': {
            'certo': '115.139.727-07',
            'errado': '115.139.727-0',
        },
    },
    'cnpj': {
            'numero': {
                'certo': 57998063000104,
                'errado': 5799806300010,
            },
            'string': {
                'certo': '57.998.063/0001-04',
                'errado': '57.998.063/0001-0',
            }
        }
}

print('Documentos certos')
cpf_um = documento['cpf']['numero']['certo']
cpf_dois = documento['cpf']['string']['certo']
cnpj_um = documento['cnpj']['numero']['certo']
cnpj_dois = documento['cnpj']['string']['certo']

documento_um = documento_factory.Documento.cria_documento(cpf_um)
documento_dois = documento_factory.Documento.cria_documento(cpf_dois)
documento_tres = documento_factory.Documento.cria_documento(cnpj_um)
documento_quatro = documento_factory.Documento.cria_documento(cnpj_dois)

print(documento_um)
print(documento_dois)
print(documento_tres)
print(documento_quatro)

# Documentos errados

cpf_tres = documento['cpf']['numero']['errado']
cpf_quatro = documento['cpf']['string']['errado']
cnpj_tres = documento['cnpj']['numero']['errado']
cnpj_quatro = documento['cnpj']['string']['errado']

# Ao descomentar cada instância abaixo será jogada a devida exceção
# documento_cinco = documento_factory.Documento.cria_documento(cpf_tres)
# documento_seis = documento_factory.Documento.cria_documento(cpf_quatro)
# documento_sete = documento_factory.Documento.cria_documento(cnpj_tres)
# documento_oito = documento_factory.Documento.cria_documento(cnpj_quatro)


# para isso funcionar legal, o código do pais precisaria vir de outro campo
'''
telefone_um = telefone.Telefone('552124921565')
telefone_dois = telefone.Telefone('5521979568890')

print(telefone_um)
print(telefone_dois)

cadastro = datas_br.DatasBr()

print(cadastro.tempo_cadastro())
'''

cep = '20231-050'

endereco_centro = endereco.Endereco(cep)

print(endereco_centro)
bairro, cidade, estado = endereco_centro.consulta_cep()
print(bairro, cidade, estado)
