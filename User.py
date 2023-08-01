class User:
    def __init__(self, id, rating, next_user=None):
        self.id = id
        self.ratings = [rating]
        self.proximo =  next_user