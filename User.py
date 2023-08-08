class User:
    def __init__(self, id):
        self.id = id
        self.players_rated = []   
        self.players_ratings = []
        self.top_ratings = [] # notas que o usuário deu pro player ordenadas
        self.isOrr = False

    
    def add_players_info(self, player_rated, player_rating):
        self.players_rated = [*self.players_rated, player_rated]
        self.players_ratings = [*self.players_ratings, player_rating]

    def get_top_ratings(self):
        if not self.isOrr:
            index = 0
            itens_already_search = []
            while index != 20:
                maior = -1
                for rating in self.players_ratings and rating not in itens_already_search:
                    if rating > maior:
                        maior = rating
                
                self.top_ratings.append(maior)
                itens_already_search.append(itens_already_search)
                index += 1

            self.isOrr = True
        return self.top_ratings
                
        
            
