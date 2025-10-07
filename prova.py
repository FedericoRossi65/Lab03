import csv
from Auto import Auto


def carica_file_automobili( file_path):
    """Carica le auto dal file"""
    with open(file_path, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=',')
        lista_auto = []
        for row in reader:
            codiceUnivoco = row[0]
            marca = row[1]
            model = row[2]
            annoImm = row[3]
            posti = row[4]
            auto = Auto(codiceUnivoco, marca, model, annoImm, posti)
            lista_auto.append(auto)
    return lista_auto
def automobili_ordinate_per_marca(self,lista_auto):
        """Ordina le automobili per marca in ordine alfabetico"""
        lista_ordinate = []
        for a in lista_auto:
            lista_ordinate.append(a.marca)
        return sorted(lista_ordinate)
def main():
    file_path = 'automobili.csv'
    a = carica_file_automobili(file_path)



main()