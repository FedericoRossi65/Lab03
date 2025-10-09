#creazione classe auto
class Auto:
    def __init__(self, codiceUnivoco,marca,modello,annoImm,posti):
        self.codiceUnivoco = codiceUnivoco
        self.marca = marca
        self.modello = modello
        self.annoImm = annoImm
        self.posti = posti
    # metodo per avere un print pulito
    def __str__(self):
        return f'Codice Univoco:{self.codiceUnivoco},Marca:{self.marca},Modello:{self.modello},Anno di Immatricolazione:{self.annoImm},Numero posti:{self.posti}'
