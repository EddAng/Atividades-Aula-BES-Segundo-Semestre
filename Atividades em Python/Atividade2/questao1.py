#1 - Crie um programa em Python que calcule o Índice de Massa Corporal (IMC)
#de uma pessoa. O usuário deverá informar seu peso (kg) e altura (m). O
#programa deve calcular o IMC utilizando a fórmula:


try:
    sair = 0
    while sair !=2 and sair !=1:
        print("== CALCULADORA DE IMC ==")
        sair = float(input("Calcular IMC \n1- Calcular IMC\n2- Sair\nEscolha uma opção: "))
        
        if sair == 1:
            try:
                peso = 0
                altura = 0
                while peso <= 0:
                    peso = float(input("Informe seu peso (KG): "))
                    if(peso <= 0):
                        print("Informe um valor maior que zero")
                
                while altura <= 0:
                    altura = float(input("Informe sua alura (m): "))
                    if(altura <= 0):
                        print("Informe um valor maior 6que zero")
                
                print("O valor do IMC é: {:.2f}".format(peso / (altura*2)))

            except(ValueError):
                print("O valor informado não é valido")

            except:
                print("Algum erro aconteceu")
            sair = 0
            
except(ValueError):
    print("O valor informado não é valido")