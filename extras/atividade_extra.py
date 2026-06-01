import os

def encapsular_em_funcoes():
    pasta_origem = r"C:\Users\ana62455066\OneDrive - SENAC DF\Documentos\thonny"
    pasta_destino = r"C:\Users\ana62455066\OneDrive - SENAC DF\Documentos\questões renomeadas\pasta_ana"
    
    os.makedirs(pasta_destino, exist_ok=True)
    
    for i in range(1, 101):
        nome_arquivo = f'atividade {i}.py'
        caminho_origem = os.path.join(pasta_origem, nome_arquivo)
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        
        if os.path.exists(caminho_origem):
            with open(caminho_origem, "r", encoding = "utf-8") as f_entrada:
                linhas = f_entrada.readlines()
                
            with open(caminho_destino, 'w', encoding = 'utf-8') as f_saida:
                f_saida.write(f'def_q{i}():\n')
                
                if linhas:
                    for texto in linhas:
                        f_saida.write(f'    {texto}')
                        
                else:
                    f_saida(f'    pass  #Arquivo vazio\n')
                    
            print(f'{nome_arquivo} encapsulado com sucesso na pasta {caminho_destino}')
            
    print('processo 100% concluído')
            
            
encapsular_em_funcoes()