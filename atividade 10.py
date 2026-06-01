def_q10():
    largura = float(input("Digite a largura da parede (m): "))
    altura = float(input("Digite a altura da parede (m): "))
    area = largura * altura
    tinta = area / 2
    
    print("Área da parede:", area, "m²")
    print("Quantidade de tinta necessária:", tinta, "litros")