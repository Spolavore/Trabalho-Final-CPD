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

    # adicionando a nota e os usuários (essa parte do codigo ta demorando um pouco pra rodar)
    with open('./tables/minirating.csv') as rating:
        next(rating)
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
            #busca o usuário na lista
            user_on_search = users.consulta(userId)

            # caso ele não esteja ainda na hash adiciona ele
            if user_on_search == None:
                users.add(userId, 'User', player)
            else:
                # se o user já foi inserido então apenas adiciona a nova nota dada
                # a determinado jogador na lista de ratings
                user_on_search.add_rating((player, player.rating))

        print(users.consulta(32010).players_rated)
    
