def_q98():
    def SuperSomador(num1, num2):
        soma = 0
    
        if num1 > num2:
            num1, num2 = num2, num1
    
        for i in range(num1, num2 + 1):
            soma = soma + i
    
        return soma
    
    
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    resultado = SuperSomador(num1, num2)
    
    print("A soma do intervalo é:", resultado)
    
    input()