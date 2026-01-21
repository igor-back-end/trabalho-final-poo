from abc import ABC, abstractmethod
from .folhas import TIPOS_FOLHA

class Planta(ABC):
    def __init__(self, nome_comum, nome_cientifico, 
                 tamanho, tem_espinhos, tem_flor_visivel, formato_folha):

        self._nome_comum = nome_comum
        self._nome_cientifico = nome_cientifico
        
        self._tamanho = tamanho
        self._tem_espinhos = tem_espinhos
        self._tem_flor_visivel = tem_flor_visivel

        if formato_folha not in TIPOS_FOLHA:
            raise ValueError(
                f"Formato de folha inválido: '{formato_folha}'. "
                f"Use um dos seguintes: {', '.join(TIPOS_FOLHA)}"
            )

        self._formato_folha = formato_folha

    @property
    def nome_comum(self):
        return self._nome_comum

    @property
    def nome_cientifico(self):
        return self._nome_cientifico

    @property
    def tamanho(self):
        return self._tamanho

    @property
    def tem_espinhos(self):
        return self._tem_espinhos

    @property
    def tem_flor_visivel(self):
        return self._tem_flor_visivel

    @property
    def formato_folha(self):
        return self._formato_folha

    @property
    @abstractmethod
    def grupo(self):
        """Retorna o nome do grupo da planta (ex: Angiosperma)"""
        pass

    @abstractmethod
    def descricao_reprodutiva(self):
        """Método polimórfico: Cada grupo deve explicar como se reproduz"""
        pass

    def __str__(self):
        return f"{self.nome_comum} ({self.nome_cientifico}) - {self.grupo}"

    def obter_fichas(self):
        return {
            "tamanho": self._tamanho,
            "tem_espinhos": self._tem_espinhos,
            "tem_flor_visivel": self._tem_flor_visivel,
            "formato_folha": self._formato_folha
        }