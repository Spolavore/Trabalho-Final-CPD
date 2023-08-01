from Hash import Hash
class Nodo:
    def __init__(self):
        self.filhos = {}
        self.fim_da_palavra = False

class Trie:
    def __init__(self):
        self.raiz = Nodo()

    def insere(self, word):
        nodo = self.raiz
        for letra in word:
            if letra not in nodo.filhos:
                nodo.filhos[letra] = Nodo()
            nodo = nodo.filhos[letra]
        nodo.fim_da_palavra = True

    def busca(self, word):
        nodo = self.raiz
        for letra in word:
            if letra not in nodo.filhos:
                return False
            nodo = nodo.filhos[letra]
        return nodo.fim_da_palavra

    def busca_prefixo(self, prefixo):
        nodo = self.raiz
        for letra in prefixo:
            if letra not in nodo.filhos:
                return False
            nodo = nodo.filhos[letra]
            teste = nodo.filhos
            print(teste.keys())

        return True