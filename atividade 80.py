def_q80():
    import random
    
    numeros = []
    contagem = 0
    
    for i in range(30):
        sorteado = random.randint(1, 15)
        numeros.append(sorteado)
    
    chave = int(input("Digite um número (chave) entre 1 e 15 para buscar: "))
    
    print(f" Resultados para a chave {chave} ")
    
    for i in range(30):
        if numeros[i] == chave:
            print(f"Chave encontrada na posição: {i}")
            contagem += 1  
    
    print(f"A chave {chave} foi sorteada {contagem} vezes.")
    input()