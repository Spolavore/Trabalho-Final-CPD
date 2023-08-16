from Trie import Trie
import pandas as pd
import time
import csv
from rich.table import Table
from rich.console import Console



command = input()
aux = command.split(' ',1)

trie = Trie()
trie.insere(1,'abacaxi')
trie.insere(2,'abacate')
trie.insere(3,'acabar')
trie.insere(4,'jogo')
trie.insere(5,'seila')
print(trie.busca_prefixo(aux[1]))