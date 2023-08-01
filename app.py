from Hash import Hash
from Trie import Trie

if __name__== '__main__':
    # pré-processamento
    jogadores = Hash(8000)
    
    with open('./tables/players.csv') as players:
        lines = players.readlines()
        for i in range(1, len(lines)):
            jogadores.add(lines[i][0:len(lines[i])-1])

    jogadores.consulta(210202)
    trie = Trie()
    trie.insere('Lionel Messi')
    trie.insere('Neymar Junior')
    trie.insere('Neyaldina Junior')

