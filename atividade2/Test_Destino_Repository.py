from Destino import Destino
from DestinoRepository import DestinoRepository


def test_adiciona_destino():
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    destino1 = Destino(75, "Feira de Santana")
    destino2 = Destino(11, "São Paulo")
    destino3 = Destino(21, "Rio de Janeiro")
    # Act

    destino_repository.adicionar_destino(destino1)
    destino_repository.adicionar_destino(destino2)

    # Assert
    assert len(destino_repository.lista_destino) == 2
    assert not destino3 in destino_repository.lista_destino
    assert type(destino_repository.lista_destino) == list


def test_checa_se_existe():
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    destino1 = Destino(11, "Curitiba")
    destino2 = Destino(75, "Feira de Santana")
    destino_repository.adicionar_destino(destino1)
    destino_repository.adicionar_destino(destino2)
    # Act


    resultOK = destino_repository.checa_se_destino_existe(11)
    resultNOK = destino_repository.checa_se_destino_existe(76)

    # Assert
    assert len(destino_repository.lista_destino) == 2
    assert resultOK == True
    assert resultNOK == False