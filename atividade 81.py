def_q81():
    idade = []
    
    for i in range(8):
        valor = int(input("Digite a idade: "))
        idade.append(valor)
    
    soma = 0
    maior = 0
    
    for i in range (8):
        soma += idade[i]
    
        if idade[i] > maior:
            maior = idade[i]
    
    media = soma / 8
    
    
    print("Média de idade:", media)
    
    print("Posições com pessoas maiores de 25:")
    for i in range(8):
        if idade[i] > 25:
            print(i, end=' ')
    
    print("Maior idade:", maior)
    
    print("Posições da maior idade:")
    for i in range(8):
        if idade[i] == maior:
            print(i, end=' ')
            
    input()