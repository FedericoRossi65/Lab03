class Auto:
    def __init__(self, codiceUnivoco,marca,modello,annoImm,posti):
        self.codiceUnivoco = codiceUnivoco
        self.marca = marca
        self.modello = modello
        self.annoImm = annoImm
        self.posti = posti
    def __str__(self):
        return f'Dati macchina: {self.codiceUnivoco} {self.marca} {self.modello} {self.annoImm} {self.posti}'
