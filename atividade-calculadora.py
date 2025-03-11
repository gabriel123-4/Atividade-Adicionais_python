import os
#LIMPEZA DA TELA

os.system("cls")
1# 
print("CALCULADORA")
print("___________________________")

2#
N1 = float(input("Escolha seu primeiro NÚMERO: "))
N2 = float(input("Escolha seu segundo NÚMERO: "))
operaçao = input("Escolha sua operação: ")

    

if (operaçao == "+"):
    print("Valor: ", N1 + N2)
    print("Operação escolha foi: Soma")

elif (operaçao == "-"):
    print("Valor: ", N1 - N2)
    print("Operação escolha foi: Subtração")


elif (operaçao == "*"):
    print("Valor: ", N1 * N2)
    print("Operação escolha foi: Multiplicação")


elif (operaçao == "/"):
    print("Valor: ", N1 / N2)
    print("Operação escolha foi: Divisão")


    
 



