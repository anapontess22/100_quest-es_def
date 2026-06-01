def_q77():
    nomes = []
    
    
    for i in range(7):
        nome = input('digite um nome:')
        nomes.append(nome)
        
    print(f' ordem inversa: ')
    
    for i in range(6, -1, -1):
        print(nomes[i])
        
    input()