def_q55():
    import random
    
    print("=== JOGO DE ADIVINHAÇÃO ===")
    print("O computador pensou em um número entre 1 e 10...")
    
    numero = random.randint(1, 10)
    
    tentativas = 1
    
    while tentativas <= 4:
        jogador = int(input(f"Tentativa {tentativas}: Tente adivinhar: "))
        
        if jogador == numero:
            print("Parabéns! Você acertou!")
            break
        else:
            print("Você errou!")
        
        tentativas += 1
    
    if jogador != numero:
        print(f"Suas tentativas acabaram! O número era {numero}")
        
    input()