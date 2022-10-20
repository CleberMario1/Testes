class Destino:

    def __init__(self, ddd: int, destino: str):
        self.DDD = ddd
        self.destino = destino


    def __eq__(self, other):
        if isinstance(other, Destino):
            return self.destino == other.destino and self.DDD == other.DDD


        return False



