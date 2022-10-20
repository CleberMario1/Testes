from Destino import Destino
from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario

destino_repository = DestinoRepository()
user_interface = InterfaceUsuario(destino_repository)
destino_repository.adicionar_destino(Destino(61, "Brasilia"))
destino_repository.adicionar_destino(Destino(75, "Feira de Santana"))
destino_repository.adicionar_destino(Destino(11, "São paulo"))
destino_repository.adicionar_destino(Destino(21, "Rio de Janeiro"))


print(user_interface.exibir_destinos())


while True:
    ddd = user_interface.solicitar_input_usuario()
    print(user_interface.saida_usuario(ddd))



