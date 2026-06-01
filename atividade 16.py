def_q16():
    cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
    anos_fumando = int(input("Há quantos anos você fuma? "))
    
    dias_fumando = anos_fumando * 365
    
    total_cigarros = cigarros_por_dia * dias_fumando
    
    minutos_perdidos = total_cigarros * 10
    
    #converte minutos em dias 
    dias_perdidos = minutos_perdidos / 1440
    
    print("Você perdeu aproximadamente", dias_perdidos, "dias de vida.")
    input()