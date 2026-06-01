import importlib #serve para chamar uma biblioteca, pra conseguirmos usar os arquivos do python q salvamos

while True:
    n = input("\nQual questão testar? (0 para sair): ")
    if n == '0': #aqui significa q se vc digitar 0 no input de cima o break vai terminar o programa 
        break
    
    try:#significa "tente executar este código", para caso o programa de um erro ele nao pare de funcionar 
       
        modulo = importlib.import_module(f"atividade {n}.py") #o "importlib.import" e para importar um arquivo do python e a "(f"atividade {n}.py" e para acessar nossos arquivos py
        getattr(modulo, f"q_{n}")() #esse aqui é para executar a função digitada for '30' ele executa, se for maior q 100 ele diz nao foi encontrado ou foi erro de execução
        
    
    except Exception:
        if int(n) > 100:
            print("[!] Questão não encontrada ou erro na execução.")
        
        #explique o erro: o "erro" seria o if, eu coloquei o if em baixo de exception para caso o numero digitado (n) for maior q 100 ele vai printar o erro "[!] Questão não encontrada ou erro na execução"
        