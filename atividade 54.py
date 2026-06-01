def_q54():
    soma_altura = 0
    mais_90kg = 0
    menos_50_e_baixas = 0
    altos_e_pesados = 0
    
    contador = 1
    
    while contador <= 7:
        print(f"\nPessoa {contador}")
        
        peso = float(input("Digite o peso (kg): ").replace(",", "."))
        altura = float(input("Digite a altura (m): ").replace(",", "."))
        
        soma_altura += altura
        
        if peso > 90:
            mais_90kg += 1
            
        if peso < 50 and altura < 1.60:
            menos_50_e_baixas += 1
            
        if altura > 1.90 and peso > 100:
            altos_e_pesados += 1
        
        contador += 1
    
    media_altura = soma_altura / 7
    
    print("\nRESULTADOS:")
    print("a) Média de altura:", round(media_altura, 2))
    print("b) Pessoas com mais de 90kg:", mais_90kg)
    print("c) Pessoas com menos de 50kg e menos de 1.60m:", menos_50_e_baixas)
    print("d) Pessoas com mais de 1.90m e mais de 100kg:", altos_e_pesados)
    
    input()