def_q21():
    ano = int(input('digite o ano:'))
    
    resto = ano % 4
    
    if resto == 0:
        print('ano bissexto')
        
    else:
        print('ano não bissexto')
    input()