def_q74():
    lista = []
    
    for i in range(10):
        if i % 2 == 0:
            lista.append(5)
        else:
            lista.append(3)
    
    for i in range(10):
        print(lista[i], end=' ')
    
    input()
