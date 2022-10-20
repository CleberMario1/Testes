from InterfaceUsuario import InterfaceUsuario
from Destino import Destino
from DestinoRepository import DestinoRepository


def test_solicitar_input(monkeypatch):
    # Arrange
    destino_repository = DestinoRepository()
    user_interface = InterfaceUsuario(destino_repository)

    # Act

    monkeypatch.setattr('builtins.input', lambda _: 1)
    destino1 = user_interface.solicitar_input_usuario()

    # Assert
    assert destino1 == 1


def test_saida(monkeypatch):
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    user_interface = InterfaceUsuario(destino_repository)
    destino_repository.adicionar_destino(Destino(21, "Rio de Janeiro"))
    # Act

    dddsp = 11
    monkeypatch.setattr('builtins.input', lambda _: dddsp)
    destinoerrado = user_interface.saida_usuario(dddsp)

    dddrj = 21
    monkeypatch.setattr('builtins.input', lambda _: dddrj)
    destinocerto = user_interface.saida_usuario(dddrj)
    # Assert

    assert destinocerto == "Rio de Janeiro"
    assert destinoerrado == "DDD inválido"
