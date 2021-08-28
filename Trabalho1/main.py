from Aluno import Aluno
from AluEnsinoMedio import AluEnsinoMedio
from AlunoGraduacao import AlunoGraduacao



a1 = Aluno("Cod1234", "Dalto", "Mat032111")
a1.imprimir()

print ("------Aluno Ensino Médio------")

A2 = AluEnsinoMedio("Cod1234", "Dalto", "Mat032111", "Ano2020")
A2.imprimir()

print ("------Aluno Graduação------")

A3 = AlunoGraduacao("Cod1234", "Dalto", "Mat032111", "Ano2020", "1º Semestre")
A3.imprimir()