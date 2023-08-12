import time
import csv
from Hash import Hash
from Trie import Trie
from rich.table import Table
from rich.console import Console
from rich.progress import Progress



console = Console()
if __name__== '__main__':
    start_time = time.time()
    console.print('Iniciando pré-processamento...', style='bold red')
    # pré-processamento #
    jogadores = Hash(3613)
    users = Hash(3613)
    trie = Trie()
    # #adicionando o jogador e suas características
    console.print('->Populando a Hash dos jogadores', style='red')
    with open('./tables/players.csv') as players:
        next(players)
        for linha in players:
            linha = linha[0:len(linha) - 1] # utilizado para remover o \n
            data = linha.split(',', 2)
            jogadores.add(data, 'Player')
            #print("Dados: "+str(data))
            trie.insere(int(data[0]),data[1])
    console.print('     --Processo 1 concluído', style='green italic')

    # adicionando a nota e os usuários (essa parte do codigo ta demorando um pouco pra rodar)
    console.print('->Populando a Hash dos jogadores com suas respectivas notas e populando Hash dos usuários', style='dark_orange')
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
            
            users.add(userId, 'User', player_aux, rating)

           
    console.print('     --Processo 2 concluído', style='green italic')

    console.print('->Populando a tabela Hash dos jogadores com suas tags', style='yellow')       
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
    console.print('     --Processo 3 concluído', style='green italic')


time = time.time() - start_time
console.print(f'Processamento terminado em : {time} :smile:',style='cyan')
print('\n\n\n')


functions = Table(title='Comandos', title_style='bold red')
functions.add_column('Pesquisa sobre os nomes de jogadores', style='cyan')
functions.add_column('Players revisados por usuários')
functions.add_column('Pesquisas sobre tags de jogadores')
functions.add_column('Pesquisas sobre os melhores jogadores de uma determinada posição')

functions.add_row('player <nome ou prefixo>','user id_do_usuário','tags tag1, tag2, tag3, etc...',' top<n> <position>+' , style='cyan')
functions.add_row('\n-Exemplo: player Fer', '\n-Exemplo: user 65733','\n-Exemplo: tags Brazil,Clinical Finisher,etc', '\nExemplo: top10 ST', style='italic light_sky_blue3')

console.print(functions)
console.print('Para sair escreva "quit()" ', style='grey69',width=50)

command = ''
while True:
    command = input()
    aux = command.split(' ',1)
    if aux[0] == 'user':
        aux = aux[1:len(aux)]
        if len(aux) > 2:
            console.print('ERRO: COMANDO MAL FORMATADO :angry:', style='bold red')
        else:
            userId = int(aux[0])
            users.get_user_top20(userId)
    elif aux[0] == 'tags':
        tags = ''.join(aux[1:len(aux)])
        jogadores.tags(tags)
    elif aux[0] == 'commands':
        console.print(functions)
        console.print('Para sair escreva "quit()" ', style='grey69',width=50)
    elif aux[0] == 'player':
        jogadores_c_prefixo = trie.busca_prefixo(aux[1])
        jogadores.jogadores_com_prefixo(jogadores_c_prefixo)
    elif aux[0][0:3] == 'top':
        if aux[0][3:].isnumeric():
            n = int(aux[0][3:])
            position = aux[1] if len(aux) > 1 else ''
            jogadores.top_n_jogadores(n, position)
        else:
            console.print('ERRO: COMANDO MAL FORMATADO :angry:', style='bold red')

    elif aux[0] == 'quit()':
        console.print('\nFINALIZANDO O PROGRAMA ... :smiley:\n', style='bold blue')
        break
    else:
        console.print('ERRO: COMANDO MAL FORMATADO :angry:', style='bold red')
