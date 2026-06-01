def_q36():
    horas = float(input("Quantas horas de atividade física no mês? "))
    
    # cálculo dos pontos
    if horas <= 10:
        pontos = horas * 2
    elif horas <= 20:
        pontos = horas * 5
    else:
        pontos = horas * 10
    
    # cálculo do dinheiro
    dinheiro = pontos * 0.05
    
    print(f"Pontos ganhos: {pontos}")
    print(f"Dinheiro ganho: R${dinheiro:.2f}")
    
    input()
    
