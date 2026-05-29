#Declaração de Classe:
class Aluno:
    """
    Essa classe cria um aluno, com nome e idade.
    Para criar um nove aluno:
    var = Aluno(n, i)
    """
    def __init__(self, n ="", i=0): # Método construtor
        #Atributos de instância:
        self.nome = n
        self.idade = i
    # Métodos de instância:
    def Aniversario(self):
        self.idade = self.idade + 1      

    def __str__(self):
        return f"{self.nome} é aluno e tem {self.idade} anos."
    
    def __getstate__(self):
        return f"Estado: nome= {self.nome} ; idade = {self.idade}"
#Declaração de Objetos:

g1 = Aluno("Maria", 24)
g1.Aniversario()
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)