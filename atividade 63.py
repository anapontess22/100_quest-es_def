def_q63():
    contador = 0
    soma = 0
    pares = 0 
    
    while True:
        numero = int(input("digite um numero: "))
        
        contador += 1
        soma += numero
        
        if contador == 1:
            menor = numero
        else:
            if numero < menor:
                menor = numero
                
        if numero % 2 == 0:
            pares += 1 
        
        continuar = input("quer continuar? (s/n)")
        
        if continuar == "n":
            break
    
        media = soma / contador
    
    print("a) Somatório:", soma)
    print("b) Menor valor:", menor)
    print("c) Média:", media)
    print("d) Quantos valores são pares:", pares)
    
    input()