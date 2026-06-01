def_q50():
    maior_idade = 0
    homens = 0
    soma_idade_homens = 0
    
    menor_idade_mulher = None  
    
    while True:
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        
        if idade > maior_idade:
            maior_idade = idade
        
        if sexo == 'M':
            homens += 1
            soma_idade_homens += idade
        
        if sexo == 'F':
            if menor_idade_mulher is None or idade < menor_idade_mulher:
                menor_idade_mulher = idade
        
        continuar = input("Quer continuar? (S/N): ").strip().upper()
        if continuar == 'N':
            break
    
    if homens > 0:
        media_homens = soma_idade_homens / homens
    else:
        media_homens = 0
    
    print("\nRESULTADOS:")
    print("a) Maior idade:", maior_idade)
    print("b) Homens cadastrados:", homens)
    print("c) Idade da mulher mais jovem:", menor_idade_mulher)
    print("d) Média de idade dos homens:", round(media_homens, 2))
    
    input()