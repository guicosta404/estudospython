#72

#extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

#while True:
#    num = int(input('Digite um numero de zero a dez: '))
#    if 0 <= num <= 20:
#        break
#    print("Tente novamente.")

#print(f'Voce digitou o numero {extenso[num]}')

#73 

#times = ('PAL', 'SAO', 'FLU', 'FLA', 'BHA','ATL', 'CRB', 'ATM', 'RBB', 'BOT', 'GRE', 'VAS', 'INT', 'VIT', 'SAN', 'CON', 'CHA', 'REM', 'CRU', 'MIR')
#print(f'Lista de times do brasileirão {times}')
#print(f'Os cinco primeiros são {times[0:5]}')
#print(f'Os ultimos 4 são {times[-4:]}')
#print(f'Times em ordem alfabética{sorted(times)}')
#print(f'Chape está em {times.index('CHA')+1}')

#74

#from random import randint

#n = (randint(0,10),randint(0,10), randint(0,10), randint(0,10), randint(0,10))
#print('Os números sorteados foram: ', end='')
#for i in n:
#    print(f'{i} ', end='')
#print(f'\nO maior valor sorteado foi {max(n)}.') 
#print(f'O menor valor sorteado foi {min(n)}')       


#75

#num = (int(input('Digite o primeiro: ')), int(input('Digite o segundo: ')), int(input('Digite o terceiro: ')), int(input('Digite o quarto: ')) )

#print(f'Voce digitou os numeros {num}')
#print(f'O valor 9 apareceu {num.count(9)}')
#if 3 in num:
#    print(f'O número 3 apareceu na {num.index(3)+1}ª posição.')
#else:
#    print('O valor 3 nao foi digitado.')
#print('Os numeros pares digitados foram: ', end=' ')    
#for n in num:
#    if n % 2 == 0:
#        print(n, end=' ')

#76

#listagem = ("Lápis", 1.75,
#            "Borracha", 2,
#            "Caderno", 15.90)

#for pos in range(len(listagem)):
#    if pos % 2 == 0:
#        print(f"{listagem[pos]:.<30} ", end='')
#    else:
#        print(f"R${listagem[pos]:>7.2f}")

#77


# palavras = ("Barcelona", "time", "viado")

# for palavra in palavras:
#     print(f'\nNa palavra {palavra.upper()} temos as vogais', end='')
#     for letra in palavra:
#         if letra in "aeiou":
#             print(letra, end=' ')
        