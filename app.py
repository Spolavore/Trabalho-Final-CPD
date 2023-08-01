from Hash import Hash
from Trie import Trie

if __name__== '__main__':
    # pré-processamento
    jogadores = Hash(8000)
    
    with open('./tables/players.csv') as players:
        next(players)
        for linha in players:
            data = linha.split(',',2)
            jogadores.add(data)


    jogadores.consulta(210202)


