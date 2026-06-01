def_q25():
    a = float(input('digite o primeiro segmento:'))
    b = float(input('digite o segundo segmento:'))
    c = float(input('digite o terceiro segmento:'))
    
    if a >= b + c:
        print('não forma triangulo')
        
    elif b >= a + c:
        print('não forma triangulo')
    
    elif c >= a + b:
        print('não forma triangulo')
        
    else:
        print('forma um triagulo')
    input()