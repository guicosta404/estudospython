from rich import print
from rich.panel import Panel

class Churrasco:
    #atributos de classe
    consumo_padrao:float = 0.400
    preço_kg:float = 82.40

    def __init__(self, titulo, qtd):
        # atributos de instancia
        self.titulo = titulo
        self.participantes = qtd

    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preço_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def __str__(self):
        return f"Esse é {self.titulo} com {self.participantes} participantes."
        

    def analisar(self):
        conteudo = f"Analisando {self.titulo}."
        conteudo += f"\nCada participante comera {Churrasco.consumo_padrao} kg de carne e cada kg custa R${self.__class__.preço_kg:,.2f}."
        conteudo += f"\nRecomendo comprar {self.calcular_qtd_carne()} kg de carne."
        conteudo += f"\nO custo por pessoa sera R${self.calcular_custo_individual():,.2f} totalizando R${self.calcular_custo_total():,.2f}"
        analise = Panel(conteudo, title=self.titulo)
        print(analise)
c1 = Churrasco("Churras dos amigos", 15)
print(c1)
c1.analisar()