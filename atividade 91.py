def_q91():
    def maior ():
        valor1 = int(input("digite o 1º numero: "))
        valor2 = int(input("digite o 2º numero: "))
        
        if valor1 > valor2:
            print(f' O maior numero é o valor: {valor1}')
            
        elif valor2 > valor1:
            print(f' O maior numero é o valor: {valor2}')
            
        else:
            print(f' os valores são iguais')
            
    maior()
    
    input()