from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self, nome ="", preço=0.0):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        conteudo = f"{self.nome}"
        etiqueta = Panel(conteudo, title="Produto")
        print(etiqueta)

p1 = Produto("Iphone 17 Pro Max", 10000)
print(p1)
p1.etiqueta()