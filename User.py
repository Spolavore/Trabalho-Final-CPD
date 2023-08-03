class User:
    def __init__(self, id, next_user=None):
        self.id = id
        self.players_rated = [] # tamanho limitado para 20, pois só ira aparecer os 20 maiores
        self.proximo =  next_user
    
    def add_rating(self, player):
        # se o tamanho dos players_rated registrado ainda nao chegou em 20 então só adiciona
        if player[0] not in self.players_rated:
            self.players_rated = [*self.players_rated, player[0]]
