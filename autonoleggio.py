import csv
from Auto import Auto
from Noleggio import Noleggio


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
            with open(file_path, 'r', encoding='utf-8') as infile: # apetura file automobili
                reader = csv.reader(infile, delimiter=',')
                # inserimento dei dati di automobili nella classe Auto
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
            if a.codiceUnivoco == codiceUnivoco: # verifica del condice univoco per vedere se l'auto è gia presente nel catalogo

                return f' gia presente nel catalogo'
        auto_nuova = Auto(codiceUnivoco, marca, modello, anno, posti)
        self.lista_auto.append(auto_nuova)
        return f' {auto_nuova} aggiunta al catalogo'


    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        return sorted(self.lista_auto, key=lambda x: x.marca)



    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""

        auto_trovata = None # inizializza l'auto come none e in seguito se è none scaturisce errore
        for a in self.lista_auto:
            if a.codiceUnivoco == id_automobile:
                auto_trovata = a #aggiorno lo stato dell'auto per non scaturire errore se l'auto esiste
                break

        if auto_trovata is None:
            raise ValueError(f"L'auto con ID {id_automobile} non è presente nel catalogo.") # scaturisce errore se l'auto rimane None, cioè se non è nel catalogo


        for n in self.auto_noleggiate:
            if n.id_automobile == id_automobile:# verifica che l'auto non sia già noleggiata
                raise ValueError(f"L'auto con ID {id_automobile} è già noleggiata.") # scaturisce errore se l'auto è gia nella lista delle auto noleggiate

        # crea il noleggio
        id_noleggio = f"N{len(self.auto_noleggiate) + 1}" # crea il codice di noleggio N1,N2,....
        nuovo_noleggio = Noleggio(id_noleggio, data, id_automobile, cognome_cliente) # aggiunge l'auto alla lista delle auto noleggiate
        self.auto_noleggiate.append(nuovo_noleggio)

        return f"Noleggio creato con successo! ID_noleggio: {id_noleggio}"


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        for automobili in self.auto_noleggiate:
            if automobili.id_noleggio == id_noleggio: # verifica che il noleggio in questione esista
                self.auto_noleggiate.remove(automobili)
                return f'Noleggio di {automobili.id_noleggio} terminato'

        return f'{id_noleggio} non trovato'




