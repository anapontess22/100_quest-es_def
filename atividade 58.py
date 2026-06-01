def_q58():
    soma_idade = 0
    quantidade = 0
    
    while True:
        idade = int(input("Digite a idade (999 para parar): "))
        
        if idade == 999:
            break
        
        soma_idade += idade
        quantidade += 1
    
    if quantidade > 0:
        media = soma_idade / quantidade
    else:
        media = 0
    
    print("\nRESULTADO:")
    print("Quantidade de alunos:", quantidade)
    print("Média de idade:", round(media, 2))
    
    input()