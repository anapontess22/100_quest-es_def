def_q78():
    numeros = []
    
    for i in range(15):
        valor = int(input('digite um numero:'))
        numeros.append(valor)
    
    for i in range(15):
        print(f'posição {i}: {numeros[i]}')
        
        if numeros[i] % 10 == 0:
             print(f"Posição {i} (valor {numeros[i]})")
             
             
    input()