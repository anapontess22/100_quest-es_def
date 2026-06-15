class Personagem:
    def __init__(self, nome, ponto_vida, arma, dano):
        self.nome = nome
        self.ponto_vida = ponto_vida
        self.arma = arma
        self.dano = dano

    def gritar(self):
        print('COM OS PODERES DE GREISCOW')

    def atacar(self):
        print(f'{self.nome} se transformou e atacou esqueleto com {self.arma}')
        print(f'Dano causado: -{self.dano}')
        
    def defender(self):
        print(f'{self.nome} se defende')
        print(f'{self.nome}: você não irá sair impune!!')

    def correr(self):
        print('eles saem correndo um na direção um do outro')

    def HeMan(self):
        print(f' {self.nome} pega sua {self.arma} e (BOOOOOOOM EXPLOSÃO)')
        print(f'{self.nome} ACABOU COM A VIDA DE ESQUELETO')

    def forca(self):
        print(f'{self.nome}: EU TENHO A FORÇAA')

heroi = Personagem('He-Man', 200, 'espada', 50)
vilao = Personagem('Esqueleto', 200, 'cajado', 30)

heroi.gritar()
heroi.atacar()
vilao.defender()
heroi.correr()
heroi.HeMan()
heroi.forca() 
