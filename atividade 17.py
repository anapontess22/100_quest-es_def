def_q17():
    velocidade = float(input("Digite a velocidade do carro:"))
    
    if (velocidade > 80):
        multa = (velocidade - 80) * 5
        print("você foi multado")
        print("valor da multa: R$",round(multa,2))
    else:
        print("velocidade dentro do limite.")
    input() 