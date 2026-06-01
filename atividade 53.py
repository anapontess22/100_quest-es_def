def_q53():
    homens = 0
    mulheres = 0
    soma_idade = 0
    soma_idade_homens = 0
    mulheres_mais_20 = 0
    
    for i in range(5):
        idade = int(input(f"Digite a idade da pessoa {i+1}: "))
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        
        soma_idade += idade
        
        if sexo == 'M':
            homens += 1
            soma_idade_homens += idade
        elif sexo == 'F':
            mulheres += 1
            if idade > 20:
                mulheres_mais_20 += 1
    
    media_idade = soma_idade / 5
    
    if homens > 0:
        media_homens = soma_idade_homens / homens
    else:
        media_homens = 0
    
    
    print("\nRESULTADOS:")
    print(f"a) Homens cadastrados: {homens}")
    print(f"b) Mulheres cadastradas: {mulheres}")
    print(f"c) Média de idade do grupo: {media_idade:.2f}")
    print(f"d) Média de idade dos homens: {media_homens:.2f}")
    print(f"e) Mulheres com mais de 20 anos: {mulheres_mais_20}")