def_q85():
    nomes = []
    sexos = []
    salarios = []
    
    for i in range(5):
        print(f" {i+1}º FUNCIONÁRIO ")
        nome = input("Nome: ")
        
        sexo = input("Sexo (M/F): ").strip().upper()
        while sexo not in ['M', 'F']:
            sexo = input("Por favor, digite M ou F: ").strip().upper()
            
        salario = float(input("Salário: R$ "))
        
        nomes.append(nome)
        sexos.append(sexo)
        salarios.append(salario)
        print()
    
    print("  MULHERES QUE GANHAM MAIS DE R$ 5.000,00      ")
    
    print(f"{'NOME':<20} | {'SALÁRIO'}")
    print("-" * 47)
    
    for i in range(5):
    
        if sexos[i] == 'F' and salarios[i] > 5000:
            print(f"{nomes[i]:<20} | R$ {salarios[i]:,.2f}")
            
    input()