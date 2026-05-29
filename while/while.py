#57
#sexo = str(input('Digite seu sexo[M ou F]: ')).strip().upper()[0]

#while sexo not in 'MF':
#    sexo = str(input('Dado inválido. Digite novamente: ')).strip().upper()
#print(f'Sexo {sexo} registrado com sucesso!')    


#58

#import random

#num_random = random.randint(0, 10)
#tentativas = 0
#acertou = False
#while not acertou:
#    num = int(input('Digite um numero de 0 a 10: '))
#    tentativas += 1
#    if num == num_random:
#        print(f'Acertou!')
#        acertou = True
#    else:
#        if num < num_random:
#            print('Mais...')
#        else:
#            print('Menos...')    
#print(f'Acertou em {tentativas} tentativas.')               

    
#59

#num1 = int(input('Digite o primeiro número:'))
#num2 = int(input('Digite o segundo número: '))
#escolha = 0
#while escolha != 5:
#    escolha = int(input('[1]soma\n[2]sub\n[3]mult\n[4]div\n[5]sair'))
#    if escolha == 1:
#        print(f'Resultado da soma = {num1 + num2}')
        
#    elif escolha == 2:
#        print(f'Resultado da subtração = {num1-num2}')
#        
#    elif escolha == 3:
#        print(f'Resultado da mult = {num1*num2}')
        
#    elif escolha == 4:
#        print(f'Resultado da div = {num1/num2}')
        
#    elif escolha == 5:
#        break

#    else:
#        escolha = int(input('Escolha invalida, digite novamente: '))        


#60 

#n = int(input('Digite um número'))
#fatorial = 1
#c = n
#while c > 0:
#    print(c, end = '')
#    print('x' if c > 1 else ' = ', end ='')
#    fatorial *= c
#    c -= 1
    
#print(fatorial)    


# 61 e 62
# primeiro = int(input('Digite o primeiro termo: '))
# razao = int(input('Digite a razão: '))
# termo = primeiro
# c = 1
# total = 0
# mais = 10
# while mais != 0:
#     total += mais
#     while c <= total:
#         print(f'{termo} > ', end='')
#         termo += razao
#         c += 1
#     print('Pausa')
#     mais = int(input('Deseja mais quantos termos? 0 para sair: '))
# print(f'Finalizado com {total} termos mostrados.')



#63

# n = int(input("Digite quantos termos quer mostrar: "))
# cont: int = 3
# t1 = 0
# t2 = 1
# print(f"{t1} -> {t2}", end='')
# while cont <= n:
#     t3 = t1 + t2
#     print(f" -> {t3}", end='')
#     t1 = t2
#     t2 = t3
#     cont +=1


#64

# soma = 0
# maior = menor = 0
# sair = False
# cont = 0 
# while sair is not True:
#     try:
#         num = int(input("Digite um número: "))
#         soma += num
#         cont += 1
#         if cont == 1:
#             maior = menor = num
#         else: 
#             if maior < num:
#                 maior = num
#             if menor > num:
#                 menor = num              
#         sair = str(input("Deseja continuar: s ou n").lower())
#         if "n" in sair:
#             sair = True
           
#     except ValueError as e:
#         print(e)
# print(f"A média dos valores é {soma/cont:.2f}.")
# print(f"O maior foi {maior} e o menor {menor}.")       


#67


# while True:
#     num = int(input("Digite um número: "))
#     if num <= 0:
#         break
#     for i in range(1,11):
#         print(f"{num} x {i} = {num*i}")
#         i += 1  
# print("fim")        


#68
# import random

# wins = 0
# escolha_jogador = ""
# pc = random.randint(0,10)
# soma = 0
# resultado = ""
# while True:
#     pc = random.randint(0,10)
#     numero_jogador = int(input("Escolha um número: "))
#     escolha_jogador = str(input("Par ou Impar? [P/I] ").strip().lower())

#     print(f"Você escolheu {numero_jogador} e o computador {pc}")
#     soma = numero_jogador + pc
#     if soma % 2 == 0:
#         resultado = "p"
#     else:
#         resultado = "i"
#     if escolha_jogador == resultado:
#         print("Voce ganhou. Mais uma vez")
#         wins += 1
#     else:
#         print(f"Você perdeu. Ganhou {wins} vezes.")
#         break


#69

# maiores18 = 0
# homens = 0
# mulheres_menos_20 = 0
# sair = ""
# while True:
#     idade = int(input("Digite a idade: "))
#     sexo = " "
#     while sexo not in "mf":
#         sexo = str(input("Digite o sexo [M/F]: ").strip().lower())
#     if idade > 18:
#         maiores18 += 1
#     if sexo == "f" and idade < 20:
#         mulheres_menos_20 += 1 
#     if "m" in sexo:
#         homens += 1
#     sair = str(input(f"Gostaria de continuar? S ou N"))
#     if "n" in sair:
#         break

# print(f"{maiores18} mais de 18 anos.")
# print(f"{homens} homens cadastrados.")
# print(f"{mulheres_menos_20} mulheres com menos de 20 anos.")                    