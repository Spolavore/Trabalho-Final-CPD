from Players import Players

class ListaEncadeada:
    lista_consultas = []

    def __init__(self):
        self.inicio = None  

    def insere_no_inicio(self, novo_id ,novo_content):
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
        qtd_consultas = 0
        aux = self.inicio
        while aux != None:
            if aux.id == id:
                ListaEncadeada.lista_consultas.append(qtd_consultas)                
                return (aux, qtd_consultas)
            else:
                aux = aux.proximo
                qtd_consultas+=1

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
        if key not in Hash.posicoes_usadas:
            Hash.posicoes_usadas.append(key)

        return key
        

    # vai precisar ser mudado
    def add(self, infos):
        id = int(infos[0])
        content = infos[1:]
        # pega a posicao que o dado deve ser inserido com base na funcao hash
        position = self.get_position(id) 
        self.hash_table[position].insere_no_inicio(id, content)
    
    def consulta(self, id):
        key = int(id)
        position = self.get_position(key)
        print( self.hash_table[position].getInfos(id))