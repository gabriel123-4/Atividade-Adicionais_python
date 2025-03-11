import os
#LIMPEZA DA TELA

os.system("cls")
1# 
produto = input("Nome do produto: ")
preço = float(input("Preço produto: "))
quantidade = int(input("Quantos produtos deseja: "))
total = preço * quantidade

print("Total a paga sem desconto: ", total)
print("______________________________________________")





if(quantidade <= 5 ):
    desconto = total * 0.02
    print("Você ganhou 2% de desconto.")
    print("Desconto: ", desconto)
    print("Preço total com desconto: ", total - desconto)

elif (quantidade > 5 <= 10):
    desconto = total * 0.03
    print("Você ganhou 3% de desconto.")
    print("Desconto: ", desconto)
    print("Preço total com desconto: ", total - desconto )

elif (quantidade > 10):
    desconto = total * 0.05
    print("Você ganhou 5% de desconto")
    print("Desconto: ", desconto)
    print("Preço total com desconto: ", total - desconto )

