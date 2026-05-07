def metade(preco):
    new_price = preco /2
    return new_price


def dobro(preco):
    new_price = preco * 2
    return new_price


def aumentar(preco, porcentagem = 0):
    new_price = preco + (preco * porcentagem / 100)
    return new_price


def reduzir(preco, porcentagem = 0):
    new_price = preco - (preco * porcentagem / 100)
    return new_price

def moeda(preco, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')