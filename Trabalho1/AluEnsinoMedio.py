from Aluno import Aluno

class AluEnsinoMedio(Aluno):
    
        def __init__(self, codigo, nome, matricula, Ano):
            super().__init__(codigo, nome, matricula)
            self.Ano = Ano

        def imprimir(self):
                super().imprimir()
                print( "Ano: ", self.Ano)
