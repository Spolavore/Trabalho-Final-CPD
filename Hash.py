from Players import Players
from User import User

class ListaEncadeada:
    lista_consultas = []

    def __init__(self):
        self.inicio = None  

    def insere_no_inicio(self, novo_id, novo_content='', type='Players', playerInfos=None):
        if type == 'User':
            novoNodo = User(novo_id)
            novoNodo.add_rating(playerInfos)
        elif type == 'Players':
            novoNodo = Players(novo_id, novo_content)
       
        novoNodo.proximo = self.inicio
        self.inicio = novoNodo
 
    def tamanho_lista(self):
        contador = 0
        aux = self.inicio
        while(aux != None): 
            contador+=1           
            aux = aux.proximo
        return contador

    def getInfos(self, id):
        aux_nodo = self.inicio
        while aux_nodo != None:
            if id == aux_nodo.id:
                return aux_nodo
            else:
                aux_nodo = aux_nodo.proximo

    def printa_lista(self):
        aux = self.inicio
        while aux != None:
            print(aux.id)
            aux = aux.proximo

# Definicao da class hash,
# recebe na inicializacao o tamanho dela
class Hash:
    posicoes_usadas = []
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.hash_table = [ListaEncadeada() for i in range(self.tamanho)] # cria uma lista de listas encadeadas independentes
     
    

# Função de Hash para definir o local, retorna a key de onde o valor
# está ou deve ser inserido
    def get_position(self, id):
        key = (id % self.tamanho) # modulo do id pelo tamanho
        return key
        

    # vai precisar ser mudado
    def add(self, infos, type='Player', playerInfos=None):
        if type == 'Player':
            id = int(infos[0])
            content = infos[1:]
            # pega a posicao que o dado deve ser inserido com base na funcao hash
            position = id % self.tamanho
            self.hash_table[position].insere_no_inicio(id, content)
        elif type == 'User':
            #infos == id
            position = self.get_position(infos)
            position = int(id) % self.tamanho

            self.hash_table[position].insere_no_inicio(novo_id=infos, type='User', playerInfos=playerInfos)
    

    def consulta(self, id):
        key = int(id)
        position = self.get_position(key)
        return self.hash_table[position].getInfos(key)