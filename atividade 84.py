def_q84():
    nomes = []
    idades = []
    
    for i in range(9):
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
    
        nomes.append(nome)
        idades.append(idade)
    
    print(" Menores de idade :")
    
    for i in range(9):
        if idades[i] < 18:
            print(nomes[i], '-', idades[i], "anos")
    
    input()
    
    
    
    
    
