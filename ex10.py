import datetime


class Relogio:
    def mostrar_hora(self):
        hora_atual = datetime.datetime.now()
        hora_formatada = hora_atual.strftime("%H:%M:%S")
        print(f"{hora_formatada} horas no hórario de Brasília")


relogio = Relogio()
relogio.mostrar_hora()
