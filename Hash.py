from Players import Players
from User import User
from rich.table import Table
from rich.console import Console


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
    

    # funções da hash de usuários 
    # inicio:
    def get_user_top20(self, user_id):
        ratings = []
        players = []
        position = user_id % self.tamanho
        # pega o usuario e em quem ele votou e a quantidade
        for user in self.hash_table[position]:
            if user.id == user_id:
                ratings.append(user.player_rating)
                players.append(user.player_rated)
        
        # orr_ratings = ratings.copy()
        # orr_ratings.sort(reverse=True)

        orr_ratings = ratings.copy()

        # selection sort
        maior = -1
        for j in range(0, 20): # vai pegar apenas os 20 maiores, ou seja , nao ordena todo o vetor so as 20 primeiras posicoes
            maior = -1
            index = 0
            for i in range(j, len(orr_ratings)):
                if orr_ratings[i] > maior:
                    index = i
                    maior = orr_ratings[i]
            orr_ratings[j],orr_ratings[index] = orr_ratings[index], orr_ratings[j]

        orr_ratings = orr_ratings[0:20]
        table = Table(title=f'Tags')
        table.add_column("sofifa_id", style='purple')
        table.add_column("name", style='white')
        table.add_column("player_positions", style='purple')
        table.add_column("rating", style='white')
        table.add_column("count", style='purple')
        for rating in orr_ratings:
            index = ratings.index(rating)
            player = players[index]
            players.pop(index)
            ratings.pop(index)
            table.add_row(f'{player.id}',f'{player.name}',f'{player.player_positions}',f'{player.get_rating()}',f'{player.total_avaliacoes}')

        console = Console()
        console.print(table)
    # fim
    
    # Funções da Hash de jogadores
    # tags devem vir no formato de string seperadas por vígula
    def tags(self, tags=str):
        tags = tags.split(',')
        players_with_tags = []
        for i in range(0, len(self.hash_table)):
            for player in self.hash_table[i]:
                all_tags_in = False
                for tag in tags:
                    if tag in player.tags:
                        all_tags_in = True
                    else:
                        break
                if all_tags_in:
                    players_with_tags.append(player)
        
        table = Table(title=f'Tags')
        table.add_column("sofifa_id", style='cyan')
        table.add_column("name", style='white')
        table.add_column("player_positions", style='cyan')
        table.add_column("rating", style='white')
        table.add_column("count", style='cyan')
        for player in players_with_tags:
            table.add_row(f'{player.id}', f'{player.name}', f'{player.player_positions}', f'{player.get_rating()}', f'{player.total_avaliacoes}')

        console = Console()
        console.print(table)