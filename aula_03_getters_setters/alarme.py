class Alarme:

    # constructor
    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    # getters
    def get_estado(self) -> bool:
        return self.__estado
    
    # setters
    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor
