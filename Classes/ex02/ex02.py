class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos.
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self.nome = nome
        self.saldo = saldo 
        print(f"Conta de {self.nome} criada com sucesso. Saldo inicial de R${self.saldo:,.2f}.")

    def __str__(self):
        return f"A conta {self.id} de {self.nome} tem R${self.saldo:,.2f} de saldo bancário."
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depositado R${valor:,.2f} na conta {self.id} de {self.nome}. ")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque negado na conta {self.id}. Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} da conta {self.id} de {self.nome} realizado com sucesso.")

conta1 = ContaBancaria(112, "Maria", 3000)
conta1.sacar(30001)
print(conta1)

