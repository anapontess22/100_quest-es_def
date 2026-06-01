def_q69():
    primeiro = int(input("Digite o primeiro termo: "))
    razao = int(input("Digite a razão: "))
    
    soma = 0
    
    for i in range(10):
        termo = primeiro + i * razao
        print(termo, end=' ')
        soma += termo
    
    print("Soma dos termos:", soma)
    
    
    input()