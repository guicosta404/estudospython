class Funcionario:
    # Atributos de classe
    empresa = "Tecsa Group"

    def __init__(self, nome="", setor="", cargo=""):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f"Olá, sou {self.nome}, do setor {self.setor} com cargo de {self.cargo} na empresa {self.__class__.empresa}"
    
f1 = Funcionario("Luiz", "tech", "estagiário")
print(f1.apresentar())

f2 = Funcionario("Maria", "adm", "auxiliar")
print(f2.apresentar())
