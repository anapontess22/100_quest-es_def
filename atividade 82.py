def_q82():
    notas = []
    
    for i in range(10):
        valor = float(input("Digite a nota: "))
        notas.append(valor)
    
    soma = 0
    
    for i in range(10):
        soma += notas[i]
    
    media = soma / 10
    
    acima = 0
    
    for i in range(10):
        if notas[i] > media:
            acima += 1
    
    maior = notas[0]
    
    for i in range(10):
        if notas[i] > maior:
            maior = notas[i]
    
    print("Média da turma:", media)
    print("Alunos acima da média:", acima)
    print("Maior nota:", maior)
    
    print("Posições da maior nota:")
    
    for i in range(10):
        if notas[i] == maior:
            print(i, end=' ')
    input()