from Computador import Computador
from Desktop import Desktop
from Notebook import Notebook


d1 = Desktop("Dell", "branca", 3000.65, 150)
d1.getInformacoes()
d1.cadastrar()


print("---------------")

n1 = Notebook("Dell-A25P", "prata", 2850.00, 2)
n1.getInformacoes()
n1.cadastrar()