from Trie import Trie


name_list = ["ana", "anabela", "andre", "bruna", "bruno"]
trie = Trie()
i = 0
for name in name_list:
    trie.insere(i,name)
    i+=1

prefix = "ana"
matching_names = trie.busca_prefixo(prefix)
print(matching_names)