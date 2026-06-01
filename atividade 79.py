def_q79():
    numeros = []
    
    for i in range(10):
        valor = int(input(f'Digite o {i+1}º número: '))
        numeros.append(valor)
    
    print(" Números Pares Encontrados: ")
    
    for i in range(10):
        if numeros[i] % 2 == 0:
            print(f"O número {numeros[i]} é par e está na posição {i}")
            
    input()