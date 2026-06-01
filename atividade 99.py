def_q99():
    def Potencia(base, expoente):
        resultado = base ** expoente
        return resultado
    
    
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))
    
    resultado = Potencia(base, expoente)
    
    print("O resultado da potência é:", resultado)
    
    input()