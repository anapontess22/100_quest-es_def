def_q31():
    import random
    
    print("=== JOGO JOKENPO ===")
    
    # Opções do jogo
    opcoes = ["pedra", "papel", "tesoura"]
    
    # Jogador escolhe
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    
    # Computador escolhe
    computador = random.choice(opcoes)
    
    print(f"Você escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")
    
    # Regras do jogo
    if jogador == computador:
        print("Empate!")
    
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você venceu!")
    
    elif jogador in opcoes:
        print("Você perdeu!")
    
    else:
        print("Opção inválida!")
        
        
    input()
        
        