#2 – Simulador de caixa eletrônico
#Crie um programa que simule um caixa eletrônico. O usuário inicia com um
#saldo de R$ 1000,00 e pode escolher no menu:
#1. Ver saldo
#2. Depositar dinheiro
#3. Sacar dinheiro
#4. Sair

saldo = 1000.00

def versaldo(saldo):
    return "O saldo  do usuário é de R${:.2f}".format(saldo)

def depositar(saldo):
    try:
        deposito = 0
        while deposito <= 0:
            deposito = float(input("Informe o valor do depósito: "))
            return deposito + saldo
    
    except ValueError:
        print("O valor informado é inválido!")
        
def saque(saldo):
    try:
        saque = 0
        while saque <= saldo:
            saque = float(input("Informe o valor do saque: "))
            return saldo - saque
    
    except ValueError:
        print("O valor informado é inválido!")
        
    except:
        print("Algum erro aconteceu!")

sair = 0
while sair != 4:
    try:
    
        sair = int(input("Bem vindo ao caixa!! Selecione a operação:\n1. Ver Saldo\n2. Depositar dinheiro\n3. Sacar dinheiro\n4. Sair\n"))
        if sair == 1:
            print(versaldo(saldo))
            
        elif sair == 2:
            saldo = depositar(saldo)
            
        elif sair == 3:
            saldo = saque(saldo)
        
        elif sair ==4:
            print("Volte Sempre!!")
            break

    except ValueError:
        print("Valor informado é inválido!")

    except:
        print("Algum erro aconteceu!")