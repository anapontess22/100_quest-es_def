def_q34():
    print(" CÁLCULO DE IMC ")
    
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    imc = peso / (altura ** 2)
    
    print(f"\nSeu IMC é: {imc:.2f}")
    
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    
    elif imc < 25:
        print("Classificação: Peso ideal")
    
    elif imc < 30:
        print("Classificação: Sobrepeso")
    
    elif imc < 40:
        print("Classificação: Obesidade")
    
    else:
        print("Classificação: Obesidade mórbida")
        
    input()    
        
    
