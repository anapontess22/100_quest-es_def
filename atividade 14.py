def_q14():
    Dias = int(input('digite aqui por quantos dias o seu carro foi alugado:'))
    km = float(input('digite aqui quantos km foram percorridos:'))
    
    valor_dias = Dias * 90
    valor_km = km * 0.20
    
    print(f'o valor a pagar fica totalizado de {valor_dias+valor_km}')
    input()