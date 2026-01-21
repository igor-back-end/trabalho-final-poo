from .planta import Planta

class Briofita(Planta):
    @property
    def grupo(self):
        return "Briófita"

    def descricao_reprodutiva(self):
        return "Reproduz-se por esporos e é dependente de água. Não possui flores nem sementes."

class Pteridofita(Planta):
    @property
    def grupo(self):
        return "Pteridófita"

    def descricao_reprodutiva(self):
        return "Reproduz-se por esporos (soros nas folhas). Vascular, mas sem sementes ou flores."

class Gimnosperma(Planta):
    @property
    def grupo(self):
        return "Gimnosperma"

    def descricao_reprodutiva(self):
        return "Sementes nuas (cones/pinhas). Não forma frutos verdadeiros."

class Angiosperma(Planta):
    @property
    def grupo(self):
        return "Angiosperma"

    def descricao_reprodutiva(self):
        return "Possui flores e frutos que protegem a semente. Maior diversidade."
