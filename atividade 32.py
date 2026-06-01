def_q32():
    import random
    
    print("=== JOGO DE ADIVINHAÇÃO ===")
    print("O computador pensou em um número entre 1 e 5...")
    
    numero = random.randint(1, 5)
    
    jogador = int(input("Tente adivinhar: "))
    
    if jogador == numero:
        print("Parabéns! Você acertou!")
    else:
        print(" Você errou!")
        print(f"O número era {numero}")
        
    
    input()
    
    
