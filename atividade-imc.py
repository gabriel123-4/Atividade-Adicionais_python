import os
#LIMPEZA DA TELA

os.system("cls")
1#
Nome = input("Nome: ")
Altura = float(input("Sua altura: "))
peso =  float(input("Peso: "))

imc = peso / ( Altura * Altura)
print("Seu imc é: ", imc)

if( imc < 16.9):
   print("Muito abaixo do peso. ")
elif( imc > 16.9 and 18.4):
  print("Abaixo peso")
elif( imc > 18.5 and 24.9):
  print("Peso normal")
elif( imc > 25 and 29.9):
  print("Acima do peso")
elif( imc > 30 and 34.9):
  print("Obesidade grau 1")
elif ( imc > 35 and 40):
  print("Obesidade grau 2")
elif ( imc > 40):
  print("Obesidade gau 3")
