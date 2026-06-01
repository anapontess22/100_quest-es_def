def_q30():
    a = float(input('Digite o primeiro segmento: '))
    b = float(input('Digite o segundo segmento: '))
    c = float(input('Digite o terceiro segmento: '))
    
    # Verifica se NÃO forma triângulo
    if a >= b + c or b >= a + c or c >= a + b:
        print('Não forma triângulo')
    
    else:
        print('Forma um triângulo')
    
        # Classificação
        if a == b == c:
            print('Equilátero')
        elif a == b or a == c or b == c:
            print('Isósceles')
        else:
            print('Escaleno')
    
    
    input()
    
    
    
    
