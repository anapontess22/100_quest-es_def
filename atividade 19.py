def_q19():
    distancia = int(input('digite quantos km você deseja percorrer:'))
    
    print(f'distancia percorrida: {distancia}')
    
    if distancia < 200:
        preco = distancia * 0.50
        print(f' valor : {preco}')
        
    else:
        preco = distancia * 0.45
        print('valor: {preco}')