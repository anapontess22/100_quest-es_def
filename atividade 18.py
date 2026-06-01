def_q18():
    ano = int(input('digite aquio o ano que você nasceu:'))
    
    idade= 2026 - ano
    
    if idade < 16:
        print(f' você tem menos de 16 anos')
        print('não pode votar')
        
    else:
        print(' você tem mais de 16 anos, ja pode votar')
    input()