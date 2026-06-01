def_q97():
    def Maior(valor1, valor2, valor3):
        maior = valor1
    
        if valor2 > maior:
            maior = valor2
    
        if valor3 > maior:
            maior = valor3
    
        return maior
    
    
    num1 = int(input("Digite o 1º número: "))
    num2 = int(input("Digite o 2º número: "))
    num3 = int(input("Digite o 3º número: "))
    
    resultado = Maior(num1, num2, num3)
    
    print("O maior número é:", resultado)
    
    input()