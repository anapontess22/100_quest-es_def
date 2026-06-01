def_q52():
    contador = 1
    soma = 0
    maior = 0
    mais18 = 0
    menos5 = 0
    
    while contador <= 10:
        idade = int(input(f"Digite a idade da {contador}ª pessoa: "))
    
        soma += idade
    
        if idade > maior:
            maior = idade
    
        if idade > 18:
            mais18 += 1
    
        if idade < 5:
            menos5 += 1
    
        contador += 1
    
    media = soma / 10
    
    print("\nMédia de idade:", media)
    print("Pessoas com mais de 18 anos:", mais18)
    print("Pessoas com menos de 5 anos:", menos5)
    print("Maior idade:", maior)
    
    input()