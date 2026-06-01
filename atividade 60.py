def_q60():
    soma_idade = 0
    quantidade = 0
    
    nome_mais_velho = ""
    maior_idade = 0
    
    nome_mulher_jovem = ""
    menor_idade_mulher = None
    
    homens_mais_30 = 0
    mulheres_menos_18 = 0
    
    while True:
    
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        
        
        soma_idade += idade
        quantidade += 1
        
        
        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho = nome
        
        
        if sexo == 'F':
            if menor_idade_mulher is None or idade < menor_idade_mulher:
                menor_idade_mulher = idade
                nome_mulher_jovem = nome
        
        
        if sexo == 'M' and idade > 30:
            homens_mais_30 += 1
        
        
        if sexo == 'F' and idade < 18:
            mulheres_menos_18 += 1
        
        continuar = input("Quer continuar? (S/N): ").strip().upper()
        if continuar == 'N':
            break
    
    if quantidade > 0:
        media = soma_idade / quantidade
    else:
        media = 0
    
    print("\nRESULTADOS:")
    print("a) Pessoa mais velha:", nome_mais_velho)
    print("b) Mulher mais jovem:", nome_mulher_jovem)
    print("c) Média de idade:", round(media, 2))
    print("d) Homens com mais de 30 anos:", homens_mais_30)
    print("e) Mulheres com menos de 18 anos:", mulheres_menos_18)
