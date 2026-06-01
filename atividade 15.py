def_q15():
    dias = int(input('nos diga seus dias trabalhados:'))
    
    horas_trabalhadas = 8 * 25
    dias_trabalhados = dias * horas_trabalhadas
    
    print(f' seu salário será de: {dias_trabalhados+horas_trabalhadas}')
    input()