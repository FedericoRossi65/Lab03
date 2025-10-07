import csv
from Auto import Auto
class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.lista_auto = []




    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        with open(file_path, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile, delimiter=',')

            for row in reader:
                codiceUnivoco =row[0]
                marca = row[1]
                model = row[2]
                annoImm = row[3]
                posti = row[4]
                auto = Auto(codiceUnivoco, marca, model, annoImm, posti)
                self.lista_auto.append(auto)
        return self.lista_auto





    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        lista_nuova = []
        for a in self.lista_auto:
            lista_nuova.append(a.marca)
        return sorted(lista_nuova)



    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
