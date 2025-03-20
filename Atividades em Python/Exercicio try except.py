def soma(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multiplica(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

opcao = 0

while opcao != 5:
    try:
        opcao = int(input("Informe a operação:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair\n"))
        if opcao > 0 and opcao<5:
            num1 = int(input("Informe o primeiro número: "))
            num2 = int(input("Informe o segundo número: "))
            
            if opcao == 1:
                print("O resultado da soma é:",soma(num1,num2))
            elif opcao == 2:
                print("O resultado da subtração é: ",sub(num1,num2))
            elif opcao == 3:
                print("O resultado da multiplicação é: ",multiplica(num1,num2))
            elif opcao == 4:
                print("O resultado da Divisão é: {:.2f}".format(divide(float(num1),float(num2))))        
    except ValueError:
        print("Selecione apenas números")
    except:
        print("Algum erro ocorreu")