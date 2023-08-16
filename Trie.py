class Nodo:
    def __init__(self):
        self.filhos = []    #Lista de tuplas (letra, nodo_filho)
        self.fim_da_palavra = False
        self.player_id = None  # ID do jogador associado a este nó

class Trie:
    def __init__(self):
        self.raiz = Nodo()

    def insere(self, player_id, word):  # Adiciona o ID do jogador também
        nodo = self.raiz
        for letra in word:
            found = False
            for char, filho in nodo.filhos:
                if char == letra:
                    nodo = filho
                    found = True
                    break
            if not found:
                novo_nodo = Nodo()
                nodo.filhos.append((letra, novo_nodo))
                nodo = novo_nodo
        nodo.player_id = player_id  # Adiciona o ID do jogador a este nó
        nodo.fim_da_palavra = True

    def busca_prefixo(self, word):
        nodo = self.raiz
        for letra in word:
            found = False
            for char, filho in nodo.filhos:
                if char == letra:
                    nodo = filho
                    found = True
                    break
            if not found:
                return []
        return self.busca_palavras_com_prefixo(nodo, word)

    def busca_palavras_com_prefixo(self, nodo, prefixo):
        results = set()  # Usar um conjunto para evitar duplicação de IDs
        if nodo.fim_da_palavra:
            results.add(nodo.player_id)  # Adiciona os IDs dos jogadores associados
        for letra, nodo_filho in nodo.filhos:
            results.update(self.busca_palavras_com_prefixo(nodo_filho, prefixo+letra))
        return list(results)
