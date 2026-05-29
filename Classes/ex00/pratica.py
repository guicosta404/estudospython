#Declaração de Classe:
class Aluno:
    def __init__(self): # Método construtor
        #Atributos de instância:
        self.nome = ""
        self.idade = 0
    # Métodos de instância:
    def Aniversario(self):
        self.idade = self.idade + 1

    def Mensagem(self):
        return f"{self.nome} é aluno e tem {self.idade} anos."        

#Declaração de Objetos:

g1 = Aluno()
g1.nome = "Maria"
g1.idade = 18
g1.Aniversario()
print(g1.Mensagem())

g2 = Aluno()
g2.nome = "Luiz"
g2.idade = 26
g2.Aniversario()
print(g2.Mensagem())

g3 = Aluno()
print(g3.Mensagem())