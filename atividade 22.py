def_q22():
    ano = int(input("Digite o ano que você nasceu: "))
    idade = 2026 - ano
    
    faltam = 18 - idade
    passou = idade - 18
    
    if idade < 18:
        print(f"Faltam {faltam} ano/s pro alistamento")
        
    elif idade == 18:
        print("Você está no ano do alistamento")
    
    else:
        print(f"Passou {passou} ano/s do alistamento")