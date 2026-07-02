from .avaliacao import Avaliacao
from .cardapio.prato import Prato
from .cardapio.item_cardapio import ItemCardapio
import os

class Restaurante:
    Restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._avaliacoes = []
        self._cardapio = []
        self._ativo = False
        
        Restaurante.Restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('Nome do Restaurante | Categoria | Avaliações')

        for restaurante in cls.Restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacoes}')


    def receber_avaliacao(self, nome, nota):
        if 0  < nota <= 5:
            avaliacao = Avaliacao(nome, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if len(self._avaliacoes) == 0:
            return 0 
        
        for i in self._avaliacoes:
            soma = i._nota

        media = soma / len(self._avaliacoes)
        return media
        
        
            
    def receber_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)


    def mostrar_cardapio(self):
            for item in self._cardapio:

              if isinstance(item, Prato):
                   print(f'Prato: {item._nome} - "{item._descricao}" - R${item._preco}')


              else:
                  print(f'Bebida: {item._Bebida} - "{item.tamanho}" - R${item._preco}')
                

    def alternar_estado(self):
        self._ativo = not self._ativo
    