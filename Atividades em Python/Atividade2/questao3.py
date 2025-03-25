try:
    def somarvogais(palavra):
        maio = palavra.upper()
        print(maio)
        soma = 0
        for i in range(0,len(maio)):
            if maio[i] == 'A' or maio[i] == 'E' or maio[i] == 'I' or maio[i] == 'O' or maio[i] == 'U':
                soma = soma + 1
                print(palavra[i])
        return soma
except:
    print("Algum erro ocorreu!!")

sair = 0

while sair != 2:
    try:
        sair = int(input("== CONTADOR DE VOGAIS ==\n1 - Contar Vogais em uma frase\n2 - Sair\nEscolha uma opção: "))
        
        if sair == 1:
            palavra = input("Informe uma palavra: ")
            print(f"O número de vogais da palavra digitada \"{palavra}\" é de {somarvogais(palavra)}")
            
        elif sair == 2:
            print("Até breve!!")
            break
        
    except:
        print("Algum erro ocorreu!!")