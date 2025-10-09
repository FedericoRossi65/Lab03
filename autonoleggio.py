import csv
from Auto import Auto
from Noleggio import Noleggio

# INSERIRE GESTIONE DEGLI ERRORI IN TUTTO IL PROGRAMMA
class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.lista_auto = []
        self.nome = nome
        self.responsabile = responsabile
        self.auto_noleggiate = []





    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""

        try:
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
        except FileNotFoundError:
            print('File inesistente')





    def aggiungi_automobile(self, marca, modello, anno, posti,codiceUnivoco):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        for a in self.lista_auto:
            if a.codiceUnivoco == codiceUnivoco:

                return f' gia presente nel catalogo'
        auto_nuova = Auto(codiceUnivoco, marca, modello, anno, posti)
        self.lista_auto.append(auto_nuova)
        return f' {auto_nuova} aggiunta al catalogo'


    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        return sorted(self.lista_auto, key=lambda x: x.marca)



    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        id_noleggio= f'N{len(self.auto_noleggiate)+1}'
        nuovo_noleggio = Noleggio(id_noleggio,data,id_automobile,cognome_cliente)
        self.auto_noleggiate.append(nuovo_noleggio)
        return f'ID del noleggio effeuttuato: {id_noleggio}'




    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        for automobili in self.auto_noleggiate:
            if automobili.id_noleggio == id_noleggio:
                self.auto_noleggiate.remove(automobili)  # attenzione devo ancora mdificare questa funzione perchè nel main non mi da errore anche se il codice noleggio non esiste
                return f'Noleggio di {automobili.id_noleggio} terminato'

        return f'{id_noleggio} non trovato'




