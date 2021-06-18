import re


padrao = '\\d{4,5}\\s?[-]?\\d{4}'
texto1 = 'O meu celular é 98765-4321.'
texto2 = '1234-5678 é o telefone lá de casa.'
texto3 = 'No trabalho temos os telefones 1324-5768 e 2413-6857 para os setores comerciai e financeiro respectivamente.'
texto4 = 'Você consegue me contactar através dos números 98765-4321, 12345678, 1324 5768 e 2413-6857'
retorno = re.findall(padrao, texto4)
print(retorno)
