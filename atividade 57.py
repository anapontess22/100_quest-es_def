def_q57():
    total_homens = 0
    total_mulheres = 0
    
    while True:
        salario = float(input("Digite o salário: "))
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        
        if sexo == 'M':
            total_homens += salario
        elif sexo == 'F':
            total_mulheres += salario
        
        continuar = input("Quer continuar? (S/N): ").strip().upper()
        
        if continuar == 'N':
            break
    
    print("\nRESULTADO:")
    print("Total de salários pagos aos homens:", total_homens)
    print("Total de salários pagos às mulheres:", total_mulheres)
    
    input()