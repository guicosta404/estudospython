# Listas

# .append("#")
# .insert(0,"#")

# del exemplo[3] - del pela posição
# exemplo.pop(3)

# exemplo.remove("#") - del pelo conteúdo

# if 'conteudo' in exemplo:
#     exemplo.remove("conteudo")

# valores = list(range(4, 11)) -> valores = [4, 5, 6, 7, 8, 9, 10, 11]
# valores = [8, 2, 5, 4]
# valores.sort() -> [2, 4, 5, 8]
# valores.sort(reverse=True) -> [8, 5, 4, 2]
# len(valores) = 4 

# num = [2,5,9,1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# if 5 in num:
#     num.remove(5)
# else:
#     print('Nao achei')    
# print(num)
# print(f'essa lista tem {len(num)} posições')


# valores = list() 
# valores.append(5)
# valores.append(9)
# valores.append(4)
# for c,v in enumerate(valores):
#     print(f"Na posição {c} encontrei os valores{v}.")
# print("Final da lista.")    

# valores = list()
# for cont in range(0,5):
#     valores.append(int(input("Digite o valor: ")))

# for c,v in enumerate(valores):
#     print(f"Na posição {c} encontrei o valor {v}")


# 78

# valores = list()
# maior = 0
# menor = 0

# for c in range(0,5):
#     valores.append(int(input(f"Digite um valor para a posição {c}: ")))
#     if c == 0:
#         maior = menor = valores[c]
#     else:
#         if valores[c] > maior:
#             maior = valores[c]
#         if valores[c] < menor:
#             menor = valores[c]

# print(f"O maior valor digitado foi {maior} nas posições ", end='')
# for i, v in enumerate(valores):
#     if v == maior:
#         print(f"{i}", end=' ')


# print(f"\nO menor valor digitado foi {menor} nas posições ", end='')
# for i, v in enumerate(valores):
#     if v == menor:
#         print(f"{i}", end=' ')                     

#79

# valores = list()
# q = True

# while q:
#     n = int(input("Digite um valor (0 para sair): "))
#     if n not in valores:
#         valores.append(n)
#         print("Valor adicionado. Add outro (0 para sair)")
#     if 0 in valores:
#         q = False
       
# valores.remove(0)        
# valores.sort()
# print(f"Voce digitou os numeros : {valores}")

#80
# 
# valores = list()

# for v in range(0,5):
#     valor = int(input("Digite um valor: "))
#     if v == 0 or valor > valores[len(valores)-1]:
#         valores.append(valor)
#         print("Adicionado ao final da lista")
#     else:
#         pos = 0
#         while pos < len(valores):
#             if valor <= valores[pos]:
#                 valores.insert(pos, valor)
#                 print(f"Adicionado na posição {pos} da lista.")
#                 break
#             pos += 1 
# print(f"Os valores digitados em ordem foram {valores}: ")                
