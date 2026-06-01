def_q83():
    import random
    
    lista = []
    
    for i in range(20):
        vetor = random.randint(0, 99)
        lista.append(vetor)
    
    lista.sort()
    
    print(lista)
    
    input()