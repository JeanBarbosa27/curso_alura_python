from datetime import datetime, timedelta


class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.now()
        self.formatacao_data = '%d/%m/%Y %H:%M'

    def mes_cadastro(self):
        meses_ano = {
            '1': 'janeiro', '2': 'fevereiro', '3': 'março', '4': 'abril', '5': 'maio', '6': 'junho',
            '7': 'julho', '8': 'agosto', '9': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'
        }

        return meses_ano[str(self.momento_cadastro.month)]

    def dia_cadastro(self):
        dias_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']

        return dias_semana[self.momento_cadastro.weekday()]

    def tempo_cadastro(self):
        simula_cadastro_ha_um_tempo = timedelta(days=15, hours=3)

        return self.momento_cadastro - simula_cadastro_ha_um_tempo

    def __str__(self):
        return self.momento_cadastro.strftime(self.formatacao_data)
