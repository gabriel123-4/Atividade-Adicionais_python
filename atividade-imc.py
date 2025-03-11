import os
#LIMPEZA DA TELA

os.system("cls")
1#
Nome = input("Nome: ")
Altura = float(input("Sua altura: "))
peso =  float(input("Peso: "))

imc = peso / ( Altura * Altura)
print("Seu imc é: ", imc)
