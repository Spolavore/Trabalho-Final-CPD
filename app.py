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

    # adicionando a nota e os usuários (essa parte do codigo ta demorando um pouco pra rodar)
    with open('./tables/rating.csv', 'r') as rating:
        csvreader = csv.reader(rating)
        next(csvreader)
        

        lastIdChecked = None # responsável por saber qual último sofifa_id visitado
        players_cache = []  # lista que guardará o cache dos players, ou seja, seu Módulo
        index = -1          # index utilizável por apontar para o modulo certo do player, so será mudado quando 
                            # um sofifa_id diferente for encontrado

        users_already_add = [] # registra os usuários que já foram registrados
        player_aux = None      # cópia do player pego

        for row in csvreader:
            # dados do csv
            userId = int(row[0])
            sofifa_id = int(row[1])
            rating = float(row[2])
            
            if lastIdChecked != sofifa_id:
                lastIdChecked = sofifa_id
                player = jogadores.consulta(sofifa_id)
                player.set_rating(rating)
                players_cache.append(player)
                player_aux = player
                index += 1
               
            else:
                player = players_cache[index]
                player.set_rating(rating)
                player_aux = player
        
            user = users.consulta(userId)

            if user == None:
                users.add(userId, 'User', (player_aux, rating))
      
            

        

                
    with open('./tables/tags.csv', 'r') as tags:
        csvreader = csv.reader(tags)
        next(csvreader)

        lastIdChecked = None
        sofifa_id_cache = []
        players_cache = []
        index = -1

        for row in csvreader:
            sofifa_id = int(row[1])
            tag = row[2]

            if lastIdChecked != sofifa_id:
                player = jogadores.consulta(sofifa_id)
                players_cache.append(player)
                index +=1
                if tag not in player.tags:
                    player.tags.append(tag)
            else:
                player = players_cache[index]
                if tag not in player.tag:
                    player.tags.append(tag)
    print(time.time() - start_time)
    print(users.consulta(41241))

                    
                  #a  

        
 