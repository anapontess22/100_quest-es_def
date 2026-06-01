def_q29():
    nome = input('Digite o nome do funcionário: ')
    salario = float(input('Digite o salário: '))
    anos = int(input('Quantos anos ele trabalha na empresa? '))
    
    
    if anos <= 3:
        aumento = salario * 0.03
    
    elif anos <= 10:
        aumento = salario * 0.125
    
    else:
        aumento = salario * 0.20
    
    novo_salario = salario + aumento
    
    print(f'Funcionário: {nome}')
    print(f'Salário antigo: R${salario:}')
    print(f'Novo salário: R${novo_salario + salario:}')
    
    
    
    input()
    
    
    
    
    
    
