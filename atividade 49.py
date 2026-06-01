def_q49():
    contador = 1
    soma_par = 0
    soma_impar= 0
    
    while contador <=6:
        numero = int(input('digite um numero inteiro:'))
        par = numero % 2 == 0
        impar = numero % 2 > 0
        
        soma_par += par
        soma_impar += impar
        contador += 1 
        
    
    print(f"A quantidade de numeros pares é: {soma_par}. E de numero impares é: {soma_impar} ")
    
    input()