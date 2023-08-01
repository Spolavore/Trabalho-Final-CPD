# classe que representa o Nodo da Lista ou seja o jogador
class Players:
    def __init__(self, id, content, proximo_nodo=None):
        self.id = id    # id da fifa
        self.content = content # contem o nome do jogador na posicao 0 e a sua posicao nos nodos seguintes
        self.proximo = proximo_nodo
        self.rating = 0 
        self.total_avaliacoes = 0

    def set_rating(self,rating):
        if self.total_avaliacoes == 0:
            self.rating += rating
        else:
            self.rating = self.rating * self.total_avaliacoes + rating
        
        self.total_avaliacoes += 1
        self.rating = self.rating / self.total_avaliacoes


    