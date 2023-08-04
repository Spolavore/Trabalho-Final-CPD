import time
import csv
from Hash import Hash
from Trie import Trie


if __name__== '__main__':
    start_time = time.time()
    # pré-processamento #
    jogadores = Hash(15000)
    users = Hash(10000)

    # #adicionando o jogador e suas características
    with open('./tables/players.csv') as players:
        next(players)
        for linha in players:
            data = linha.split(',', 2)
           
            jogadores.add(data, 'Player')

    # # adicionando a nota e os usuários (essa parte do codigo ta demorando um pouco pra rodar)
    consulta = 0
    with open('./tables/rating.csv', 'r') as rating:
        csvreader = csv.reader(rating)
        next(csvreader)
        

        lastIdChecked = None
        players_cache = []
        index = -1
        for row in csvreader:
            userId = int(row[0])
            sofifa_id = int(row[1])
            rating = float(row[2])

            if lastIdChecked != sofifa_id:
                lastIdChecked = sofifa_id
                player = jogadores.consulta(sofifa_id)
                player.set_rating(rating)
                players_cache.append(player)
                index += 1
               
            else:
                player = players_cache[index]
                player.set_rating(rating)
           
        

                
      
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

    print(jogadores.consulta(158023).get_rating())
    print(time.time() - start_time, 's')