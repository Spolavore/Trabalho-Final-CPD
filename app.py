import time
import csv
from Hash import Hash
from Trie import Trie


if __name__== '__main__':
    start_time = time.time()
    # pré-processamento #
    jogadores = Hash(3613)
    users = Hash(3613)


    # #adicionando o jogador e suas características
    with open('./tables/players.csv') as players:
        next(players)
        for linha in players:
            linha = linha[0:len(linha) - 1] # utilizado para remover o \n
            data = linha.split(',', 3)
            jogadores.add(data, 'Player')

    # adicionando a nota e os usuários (essa parte do codigo ta demorando um pouco pra rodar)
    with open('./tables/rating.csv', 'r') as rating:
        csvreader = csv.reader(rating)
        next(csvreader)
    

        lastIdChecked = None # responsável por saber qual último sofifa_id visitado
        players_cache = []  # lista que guardará o cache dos players, ou seja, seu Módulo
        index = -1          # index utilizável por apontar para o modulo certo do player, so será mudado quando 
                            # um sofifa_id diferente for encontrado

        player_aux = None      # cópia do player pego

       
        for row in csvreader:
            # dados do csv
            userId = int(row[0])
            sofifa_id = int(row[1])
            rating = float(row[2])
            

            users.add(userId, 'User', sofifa_id, rating)
            
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


teste = users.consulta(52505)
print(teste.players_ratings)
print(time.time() - start_time)
                    
                    

        
 