def_q96():
    def Media(n1, n2):
        soma = n1 + n2
        media = soma / 2
        return media
    
    
    def Situacao(media):
        if media >= 7:
            return "APROVADO"
        elif media >= 5:
            return "RECUPERAÇÃO"
        else:
            return "REPROVADO"
    
    
    not1 = float(input("Digite a primeira nota: "))
    not2 = float(input("Digite a segunda nota: "))
    
    resultado = Media(not1, not2)
    situacao = Situacao(resultado)
    
    print("A média do aluno é:", resultado)
    print("Situação do aluno:", situacao)
    
    input()