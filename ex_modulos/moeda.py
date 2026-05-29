def metade(preco, formato = False):
    new_price = preco /2
    return new_price if formato is False else moeda(new_price) 


def dobro(preco, formato = False):
    new_price = preco * 2
    return new_price if formato is False else moeda(new_price)


def aumentar(preco, porcentagem = 0, formato = False):
    new_price = preco + (preco * porcentagem / 100)
    return new_price if formato is False else moeda(new_price)


def reduzir(preco, porcentagem = 0, formato = False):
    new_price = preco - (preco * porcentagem / 100)
    return new_price if formato is not True else moeda(new_price)

def moeda(preco, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')