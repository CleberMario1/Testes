from Destino import Destino
from DestinoRepository import DestinoRepository

class InterfaceUsuario:
    def __init__(self, destino_repository : DestinoRepository):
        self.destino_repository = destino_repository

    def  solicitar_input_usuario(self) -> int:
        result = int(input(
            " Coloque um DDD: "))
        return result

    def exibir_destinos(self):
        lista_destinos = self.destino_repository.lista_destino
        formatText = "{0:<10} {1:<20} \n"
        tabela = formatText.format("DDD", "Destino")

        for item in lista_destinos:
            tabela += formatText.format(item.DDD, item.destino)
        return tabela

    def saida_usuario(self, ddd):
        # ddd = self.solicitar_input_usuario()
        if(self.destino_repository.checa_se_destino_existe(ddd)):
            return self.destino_repository.obter_destino_pelo_ddd(ddd)

        return "DDD inválido"

