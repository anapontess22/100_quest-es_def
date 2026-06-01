def_q45():
    inicio = int(input("Digite o primeiro valor: "))
    fim = int(input("Digite o último valor: "))
    incremento = int(input("Digite o incremento: "))
    
    if incremento == 0:
        print("Incremento não pode ser zero!")
    else:
        numero = inicio
    
        
        if inicio < fim:
            while numero <= fim:
                print(numero, end=' ')
                numero += abs(incremento)
    
        
        else:
            while numero >= fim:
                print(numero, end=' ')
                numero -= abs(incremento)
    
    print("Acabou!")