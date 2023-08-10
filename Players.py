# classe que representa o Nodo da Lista ou seja o jogador
class Players:
    def __init__(self, id, content):
        self.id = id    # id da fifa
        self.name = content[0]
        self.tags = []
        self.player_positions = content[1]# contem o nome do jogador na posicao 0 e a sua posicao nos nodos seguintes
        self.rating_acumulative = 0 
        self.total_avaliacoes = 0

    def set_rating(self,rating):
        self.rating_acumulative += rating
        self.total_avaliacoes += 1
    
    def get_rating(self):
        return round( (self.rating_acumulative / self.total_avaliacoes), 6)


    