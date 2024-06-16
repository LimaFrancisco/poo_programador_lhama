from abc import ABC, abstractmethod

class AveVoadora(ABC):

    @abstractmethod
    def comer(self) -> None:
        raise "Should Implement comer method"
    
    @abstractmethod
    def voar(self) -> None:
        raise "Should Implement voar method"

    @abstractmethod
    def gritar(self) -> None:
        raise "Should Implement gritar method"
    
class AveQueNaoVoa(ABC):

    @abstractmethod
    def comer(self) -> None:
        raise "Should Implement comer method"

    @abstractmethod
    def gritar(self) -> None:
        raise "Should Implement gritar method"
    