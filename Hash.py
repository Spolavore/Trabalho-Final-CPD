from Players import Players
from User import User

# Definicao da class hash,
# recebe na inicializacao o tamanho dela
class Hash:
    posicoes_usadas = []
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.hash_table = [[] for i in range(self.tamanho)] # cria uma lista de listas encadeadas independentes
        self.users_top_20_cache = [] # tuple (userdId, list)
     

# Função de Hash para definir o local, retorna a key de onde o valor
# está ou deve ser inserido
    def get_position(self, id):
        key = (id % self.tamanho) # modulo do id pelo tamanho
        return key
        

    # vai precisar ser mudado
    def add(self, infos, type='Player', playerInfos=None, rating=None):
        if type == 'Player':
            id = int(infos[0])
            content = infos[1:]
            # pega a posicao que o dado deve ser inserido com base na funcao hash
            position = id % self.tamanho
            new_player = Players(id, content)
            self.hash_table[position].append(new_player)

        elif type == 'User':
            #infos == id
            position = int(infos) % self.tamanho
            new_user = User(infos, playerInfos, rating)
            self.hash_table[position].append(new_user)
    
    def consulta(self, id):
        key = int(id)
        position = key % self.tamanho
        for i in range(0, len(self.hash_table[position])):
            if self.hash_table[position][i].id == id:
                return self.hash_table[position][i]
    
    def get_users_top20(self, user_id):
        ratings = []
        players = []
        position = user_id % self.tamanho
        # pega o usuario e oq ele votou
        for user in self.hash_table[position]:
            if user.id == user_id:
                ratings.append(user.player_rating)
                players.append(user.player_rated)
        
        # orr_ratings = ratings.copy()
        # orr_ratings.sort(reverse=True)

        orr_ratings = []
        ratings_already_checked = []        
        i = 0
        while i != 20:
            maior = -1
            for rating in ratings:
                if rating > maior and rating not in ratings_already_checked:
                    maior = rating

            orr_ratings.append(maior)
            ratings_already_checked.append(maior)
            i += 1

        print(ratings)
