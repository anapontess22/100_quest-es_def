def_q62():
    contador = 0
    soma = 0
    maior21 = 0
    
    while True:
        idade = int(input("Digite a idade: "))
        contador += 1 
        soma += idade
        
        if idade >= 21:
            maior21 +=  1
        
        continuar = input("Quer continuar? (s/n): ")
    
        if continuar == "n":
            break
        
    media = soma / contador     
    
    print("quantidade de idade: ", contador)
    print("media dass idades: ", media)
    print("pessoas com 21 ou mais: ", maior21)
    
    input()