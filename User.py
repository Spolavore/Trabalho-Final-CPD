class User:
    def __init__(self, id, next_user=None):
        self.id = id
        self.players_rated = [] # tamanho limitado para 20, pois só ira aparecer os 20 maiores
        self.proximo =  next_user
    
    def add_rating(self, player):
        # se o tamanho dos players_rated registrado ainda nao chegou em 20 então só adiciona
        if len(self.players_rated) < 20:
            self.players_rated = [*self.players_rated, player]
        elif len(self.players_rated) >= 20:
            menor = self.players_rated[0]
            for i in range(0,len(self.players_rated)):
                if self.players_rated[i][1] < menor[1]:
                   menor = self.players_rated[i]

            print(f'Menor: {menor}')

   