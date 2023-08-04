class User:
    def __init__(self, id, next_user=None):
        self.id = id
        self.players_rated = [] # tamanho limitado para 20, pois só ira aparecer os 20 maiores
        self.top_ratings = [] # notas que o usuário deu pro player ordenadas
        self.isOrr = False
        self.proximo =  next_user
    


    def get_top_ratings(self):
        if not self.isOrr:
            for player in self.players_rated:
                self.top_ratings.append(player.rating)
            self.top_ratings.sort(reverse=True)
            self.isOrr = True
        
        return self.top_ratings
                
        
            
       