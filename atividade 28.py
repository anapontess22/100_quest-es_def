def_q28():
    largura  = float(input('digite a largura do espaço:'))
    comprimento = float(input('digite o comprimento do espaço:'))
    
    area = largura * comprimento
    
    if area < 100:
        print('popular')
    
    elif area >= 100 and area <=500:
        print('master')
        
    else:
        print('VIP')
    input()
    
    
    
    
    
    
    
