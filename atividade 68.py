def_q68():
    mulheres = 0
    homens_acima_100 = 0
    soma_peso_mulheres = 0
    maior_peso_homens = 0
    
    for i in range(1, 9):
        sexo = input("Digite o sexo (M/F): ").upper()
        peso = float(input("Digite o peso: "))
    
        if sexo == 'F':
            mulheres += 1
            soma_peso_mulheres += peso
        else:
            if peso > 100:
                homens_acima_100 += 1
    
            if i == 1 or peso > maior_peso_homens:
                maior_peso_homens = peso
    
    if mulheres > 0:
        media = soma_peso_mulheres / mulheres
    else:
        media = 0
    
    print("a) Quantas mulheres:", mulheres)
    print("b) Homens acima de 100Kg:", homens_acima_100)
    print("c) Média de peso das mulheres:", media)
    print("d) Maior peso entre homens:", maior_peso_homens)
    
    input()