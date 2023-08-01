# classe que representa o Nodo da Lista ou seja o jogador
class Players:
    def __init__(self, id, content, proximo_nodo=None):
        self.id = id    # id da fifa
        self.content = content # contem o nome do jogador na posicao 0 e a sua posicao nos nodos seguintes
        self.proximo = proximo_nodo
        self.rating = 0
        self.total_avaliancoes = 0

    