class User:
    def __init__(self, id, next_user=None):
        self.id = id
        self.ratings = [0] # tamanho limitado para 20, pois só ira aparecer os 20 maiores
        self.proximo =  next_user
    
    def add_rating(self, rating):
        # se o tamanho dos ratings registrado ainda nao chegou em 20 então só adiciona
        if len(self.ratings) < 20:
            self.ratings = [*self.ratings, float(rating)]
        elif len(self.ratings) == 20: # se já chegou em 20 então começa a substituir pelo menor valor contido
            menor_valor = min(self.ratings)
            if float(rating) > menor_valor:
                index_to_change = self.ratings.index(menor_valor)
                self.ratings[index_to_change] = float(rating)
        