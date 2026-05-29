#46
#import time

#for c in range(10, -1, -1):
#    print(f'...{c}')
#    time.sleep(1)
#print('Bum')    


#47 

#for c in range(0, 51, 2):
#    print(f'{c}')


#48
#soma_multiplos = 0
#for c in range(0,501, 3):
#    if c % 3 == 0:
#        soma_multiplos += c
#print(soma_multiplos)        


#49

#num = int(input("Digite o numero"))

#for c in range(1, 11):
#    print(f'{num*c}')


#50

#soma_pares = 0
#for c in range(1,7):
#    numeros = int(input("Digite um numero: "))
#    if numeros % 2 == 0:
#        soma_pares += numeros
#print(f"{soma_pares}")  

#51
#primeiro = int(input('Digite o primeiro termo: '))
#razao = int(input('Digite a razao: '))
#decimo = primeiro + (10-1) * razao
#for c in range (primeiro, decimo + razao , razao):
#   print(f'{c} ->')
#52

#53
#num = int(input('Digite um numero: '))
#divisiveis = 0
#for c in range(1, num + 1): 
#     if num % c == 0:
#          divisiveis += 1
#if divisiveis > 2:
#     print('Numero nao é primo')
#else: 
#     print('Numero primo.')           

#54
#soma = 0 
#for c in range(1,8):
#    idade = int(input("Digite sua idade: "))
#    if idade >= 18:
#        soma += 1
#print(soma)

#55
#maior = 0
#menor = 0
#for c in range(1,6):
#    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
#    if c == 1:
#        maior = peso
#        menor = peso
#    else:
#        if peso > maior:
#            maior = peso
#        elif peso < menor:
#            menor = peso
#print(f"O maior peso lido foi de {maior} kg")
#print(f"O menor peso lido foi {menor} kg")                    

#56

#maior_idade_masc = 0
#nome_mais_velho = 0
#soma_idade = 0
#media_idade = 0
#total_mulher20 = 0

#for pessoa in range(1,5 ):
#    print(f'---{pessoa}ª pessoa---')
#   nome = str(input('Digite o nome: '))
#    idade = int(input('Digite a idade: '))
#    sexo = str(input('Digite o sexo M/F: '))

#    soma_idade += idade

#    if pessoa == 1 and sexo in 'Mm':
#        maior_idade_masc = idade
#       nome_mais_velho = nome
#    if sexo in 'Mm' and idade > maior_idade_masc:
#        maior_idade_masc = idade
#        nome_mais_velho = nome
#    
#    if sexo in 'Ff' and idade < 20:
#        total_mulher20 += 1

#media_idade = soma_idade / 4
#print(f'A média de idade do grupo é {media_idade:.1f}.')
#print(f'O homem mais velho se chama {nome_mais_velho} e tem {maior_idade_masc} anos.')  
#print(f'{total_mulher20} mulheres tem menos de 20 anos.')  

#60

#num = -2

#factorial = 1

#if num < 0:
#    print('Factorial does not exist from negative numbers.')
#elif num == 0:
#    print('Factorial of 0 is 1.')
#else: 
#    for i in range(1, num+1, +1):
#        factorial *= i

#    print(f'The factorial number of {num} is {factorial}.')        