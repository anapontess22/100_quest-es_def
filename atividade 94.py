def_q94():
    def Fibonacci(n):
    
        a = 1
        b = 1
    
        for i in range(n):
    
            print(a, end=' >> ')
    
            novo = a + b
    
            a = b
            b = novo
    
        print('FIM')
    
    
    quantidade = int(input('Quantos termos deseja mostrar? '))
    
    Fibonacci(quantidade)
    
    input()