from abc import ABC, abstractmethod

class CypherBase(ABC):
    '''
        The base class for various ciphers.
    '''
    @abstractmethod
    def encode(self, plaintext:str):
        pass

    @abstractmethod
    def decode(self, cyphertext:str):
        pass