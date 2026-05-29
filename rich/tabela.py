from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome", justify="left", style="red")
tabela.add_column("Preço", justify="right", style="blue")
tabela.add_row("Lápis", "[green]R$1.00[/]")
tabela.add_row("Caderno", "R$5,00")
print(tabela)