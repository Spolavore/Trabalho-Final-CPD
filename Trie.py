class Nodo:
    def __init__(self):
        self.filhos = {}
        self.fim_da_palavra = False
        self.player_ids = []  # Lista de IDs de jogadores associados a este nó

class Trie:
    def __init__(self):
        self.raiz = Nodo()

    def insere(self, player_id, word):  # Adiciona o ID do jogador também
        nodo = self.raiz
        for letra in word:
            if letra not in nodo.filhos:
                nodo.filhos[letra] = Nodo()
            nodo = nodo.filhos[letra]
            nodo.player_ids.append(player_id)  # Adiciona o ID do jogador a este nó
        nodo.fim_da_palavra = True

    def busca_prefixo(self, word):
        nodo = self.raiz
        for letra in word:
            if letra not in nodo.filhos:
                return []
            nodo = nodo.filhos[letra]
        return self.busca_palavras_com_prefixo(nodo, word)

    def busca_palavras_com_prefixo(self, nodo, prefixo):
        results = set()  # Usar um conjunto para evitar duplicação de IDs
        if nodo.fim_da_palavra:
            results.update(nodo.player_ids)  # Adiciona os IDs dos jogadores associados
        for letra, nodo_filho in nodo.filhos.items():
            results.update(self.busca_palavras_com_prefixo(nodo_filho, prefixo+letra))
        return list(results)
