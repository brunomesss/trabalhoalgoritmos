from No import No

class ListaDuplaEncadeada:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    
    def adicionar(self, dado):

        
        no = No(dado, None, None)

        
        if self.inicio is None:
            self.inicio = no
            self.fim = no

        
        else:
            
            no.anterior = self.fim
            
            no.proximo = None
            
            self.fim.proximo = no
           
            self.fim = no


    def imprimir(self):
        
        print("Lista duplamente encadeada na ordem dos elementos adicionados: ")

        
        no_atual = self.inicio

        no = ""
        
        while no_atual is not None:
            if no_atual.anterior is None:
                no += "None "
            no += " | " + str(no_atual.dado) + " | "
            if no_atual.proximo is None:
                no += "None"

            no_atual = no_atual.proximo
        print(no)
        print()



    def imprimir_invertido(self): 

        
        print("Lista duplamente encadeada em ordem invertida: ")

        
        no_atual = self.fim

        no = ""
        
        while no_atual is not None:
            if no_atual.proximo is None:
                no += "None "
            no += " | " + str(no_atual.dado) + " | "
            if no_atual.anterior is None:
                no += "None"

            no_atual = no_atual.anterior
        print(no)
        print()