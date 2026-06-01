def_q43():
    numero = 30
    while numero >= 1:
        if numero % 4 == 0:
            print(f'{[numero]}', end=' ')
        else:
            print(numero, end=' ')
        
        numero -= 1
    
    print('Acabou!')
