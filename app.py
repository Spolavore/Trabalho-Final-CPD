from Hash import Hash
from Trie import Trie

if __name__== '__main__':
    # pré-processamento #
    jogadores = Hash(10000)
    users = Hash(10000)

    #adicionando o jogador e suas características
    with open('./tables/players.csv') as players:
        next(players)
        for linha in players:
            data = linha.split(',', 2)
            jogadores.add(data, 'Player')

    # adicionando a nota e os usuários
    with open('./tables/minirating.csv') as rating:
        next(rating)
        users_ja_inserido = []
        for linha in rating:
            # pegando e separando informações contidas na linhas
            infos = linha.split(',', 3)
            userId = int(infos[0])
            fifaId = int(infos[1])
            rating = float(infos[2][0:len(infos[2]) -1])
            
            #consultado qual player deve ter a nota alterada
            player = jogadores.consulta(fifaId)
            #mudando o rating desse jogador pego
            player.set_rating(rating)
            
            #inserindo usuários
            if userId not in users_ja_inserido:
                users.add(userId, 'User', rating)
                users_ja_inserido.append(userId)

        print(users.consulta(57002).ratings)
    
