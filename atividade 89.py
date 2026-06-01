def_q89():
    def gerador(texto, borda):
        
        if borda == 1:
            linha = "+-------=======------+"
            
        elif borda == 2:
            linha = "~~~~~~~~:::::::~~~~~~~"
            
        elif borda == 3:
            linha = "<<<<<<<<------->>>>>>>"
            
        else:
            linha = "Borda inválida!"
        
        print(linha)
        print(texto)
        print(linha)
    
    
    mensagem = input("Digite uma mensagem: ")
    tipo = int(input("Escolha a borda (1, 2 ou 3): "))
    
    gerador(mensagem, tipo)
    
    input()