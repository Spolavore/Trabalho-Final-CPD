import time
import pandas as pd
from Hash import Hash
from Trie import Trie


if __name__== '__main__':
    start_time = time.time()
    # pré-processamento #
    jogadores = Hash(10000)
    users = Hash(10000)

    #adicionando o jogador e suas características
    with open('./tables/players.csv') as players:
        next(players)
        for linha in players:
            data = linha.split(',', 2)
            jogadores.add(data, 'Player')


    ratings = pd.read_csv('./tables/rating.csv')
    print(ratings)


    # # adicionando a nota e os usuários (essa parte do codigo ta demorando um pouco pra rodar)
    # with open('./tables/rating.csv') as rating:
    #     next(rating)

    #     ids_already_searched = []
    #     players_already_searched = []
    #     index = -1

    #     for linha in rating:
    #         # pegando e separando informações contidas na linhas

    #         infos = linha.split(',', 3)
    #         userId = infos[0]
    #         fifaId = infos[1]
    #         rating =  float(infos[2])

    #         # consultado qual player deve ter a nota alterada
    #         if fifaId not in ids_already_searched:
    #             player = jogadores.consulta(fifaId)
    #             ids_already_searched.append(fifaId)
    #             players_already_searched.append(player)
    #             #mudando o rating desse jogador pego
    #             player.set_rating(rating)
    #             index += 1
    #         else:
    #             player = players_already_searched[index]
    #             player.set_rating(rating)

            
            #inserindo usuários
            #busca o usuário na lista
            # user_on_search = users.consulta(userId)

            # # caso ele não esteja ainda na hash adiciona ele
            # if user_on_search == None:
            #     users.add(userId, 'User', (player, player.rating))
            # else:
            #     # se o user já foi inserido então apenas adiciona a nova nota dada
            #     # a determinado jogador na lista de ratings
            #     user_on_search.add_rating((player, player.rating))

        #verificar pois nao deveria aparecer tantos elemento

    print(time.time() - start_time, 's')
