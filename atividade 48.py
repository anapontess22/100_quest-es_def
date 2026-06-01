def_q48():
    contador = 1
    soma = 0
    
    while contador <= 7:
        numero = int(input(f"Digite o {contador}º número: "))
        soma += numero
        contador += 1
    
    print("A soma total é:", soma)
    
    input()