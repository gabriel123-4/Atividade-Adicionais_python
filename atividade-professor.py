import os
#LIMPEZA DA TELA

os.system("cls")
1#
professor = input("Nome do professor: ")
Nivel = int(input ("Nível do professor: "))
hora_trabalho = int(input("Quantas aulas por semana: "))



if (Nivel == 1):
    Soma1 = 12 * hora_trabalho 
    print("Professoar está nível 1- R$ 12,00 por hora/aula")
    print("Seu salário do mês é: ",  Soma1 * 4 )
elif (Nivel == 2):
    soma2 = 17 * hora_trabalho
    print("Professor está no nível 2")
    print("Seu salário do mês é: ", soma2 * 4)
elif (Nivel == 3):
    soma3 = 25 * hora_trabalho
    print("Professor está no nível 3")
    print("Seu salário do mês é: ", soma3 * 4)







