# die Klassen representieren Objekte, wie
# als int --> 12, Variable hat Datentyp int
# wir wollen eine Person erstllen
# zuerst was hat die Person als Eigenschaften/Attribute
# name, alter, adresse

# Auto --> Klasse schreiben
# wenn wir ein Eingschafte/Attribut erwähnen -->
# self.NameDerEingenschaft/Attribut

# Jede Klasse hat --> 1) Attribute stehen im Konstruktor
#                     2) Konstruktor
#                     3) Methoden/Funktionen

# Der Konstruktor von jeder Klasse wird wie folgt geschrieben:
# def __init__(self, Parameters):


class Auto:
    """
    Diese Klasse repräsentiert ein Auto, das verschiedene Konfigurationsoptionen wie PS, Farbe, Räder usw. hat.
    Der Preis wird je nach Auswahl der Optionen angepasst.
    """
    # wann verwenden wir den Konstruktor --> wenn wir ein Auto erstellen
    # jetzt merken wir, dass um ein Auto zu erstellen müssen zuerst entscheiden
    # was ist der Preis, die ID, der Modell davon ist
    # wie kann man ein Auto von dieser Erstelllen
    # Regel: NameEinesObjekt(beliebig) = NameDerKlasse(Werte für die Parameter im Konstruktor)
    # 2 - FW E-Klasse ab 64.000 Euro (Autom. 6-Gang, 4 Türen und 5 Sitzer)
    # a1 = Auto(64000, 2, "FW E-Klasse") --> haben ein Objekt a1 von der Klasse Auto, d.h. a1 ist ein Auto
    # Eigenschaften : self.id = 2  ,   self.preis =       , self.modell =
    # a2 = Auto(47000, 1, "SY C-Klasse") -->
    # Eigenschaften : self.id = 1  ,   self.preis =       , self.modell =
    # Am Anfang alle Eingeschaften oder Attrbiute haben keinen Wert
    def __init__(self, preis, id, modell):
        """
        Konstruktor für die Auto-Klasse. Initialisiert das Auto mit einem Grundpreis, einer ID und einem Modellnamen.
        Zusätzlich werden viele andere Attribute mit Standardwerten versehen.
        """
        self.id = id  # Eindeutige ID des Autos
        self.preis = preis  # Grundpreis des Autos
        self.modell = modell  # Modellname des Autos
        self.ps = None  # PS-Leistung des Autos
        self.farbe = None  # Farbe des Autos
        self.raeder_design_type = None  # Design der Räder
        self.raeder_breite = None  # Breite der Räder
        self.reifen_type = None  # Reifentyp des Autos
        self.schein_werfer_type = None  # Scheinwerfertyp des Autos
        self.mit_panorama_schiebedach = False  # Panorama-Schiebedach
        self.mit_w_glas = False  # Wärmedämmendes Glas
        self.polster = None  # Polsterart des Autos
        self.mit_sitzheizung = False  # Sitzheizung
        self.mit_sitzklimatisierung = False  # Sitzklimatisierung
        self.lenkrad_farbe = None  # Farbe des Lenkrads
        self.mit_lenkradheizung = False  # Lenkradheizung
        self.mit_ambientebeleuchtung = False  # Ambientebeleuchtung
        self.mit_fussmatten = False  # Fußmatten
        self.innenhimmel_farbe = None  # Innenhimmelfarbe
        self.mit_digitalen_tacho = False  # Digitaler Tacho
        self.mit_premium_navigationssystem = False  # Premium-Navigationssystem
        self.mit_feuerloescher = False  # Feuerlöscher
        self.mit_keyless_go = False  # Keyless-Go Funktion
        self.rabatt_code = False  # Rabattcode angewendet
        self.rabatt_plz = False  # Rabatt durch PLZ

        # 2 --> int long
        # 2.0, 2.1, 2.2 --> double float

    # Getter-Methoden
    def get_preis(self):
        """Gibt den aktuellen Preis des Autos zurück."""
        return self.preis

    def get_modell(self):
        """Gibt das Modell des Autos zurück."""
        return self.modell

    def get_ps(self):
        """Gibt die PS-Leistung des Autos zurück."""
        return self.ps

    def get_farbe(self):
        """Gibt die Farbe des Autos zurück."""
        return self.farbe

    def get_raeder_design_type(self):
        """Gibt den Design-Typ der Räder zurück."""
        return self.raeder_design_type

    def get_raeder_breite(self):
        """Gibt die Breite der Räder zurück."""
        return self.raeder_breite

    def get_reifen_type(self):
        """Gibt den Reifentyp des Autos zurück."""
        return self.reifen_type

    def get_schein_werfer_type(self):
        """Gibt den Scheinwerfertyp des Autos zurück."""
        return self.schein_werfer_type

    def get_mit_panorama_schiebedach(self):
        """Gibt zurück, ob das Auto ein Panorama-Schiebedach hat."""
        return self.mit_panorama_schiebedach

    def get_mit_w_glas(self):
        """Gibt zurück, ob das Auto wärmedämmendes Glas hat."""
        return self.mit_w_glas

    def get_polster(self):
        """Gibt die Polsterart des Autos zurück."""
        return self.polster

    def get_mit_sitzheizung(self):
        """Gibt zurück, ob das Auto eine Sitzheizung hat."""
        return self.mit_sitzheizung

    def get_mit_sitzklimatisierung(self):
        """Gibt zurück, ob das Auto eine Sitzklimatisierung hat."""
        return self.mit_sitzklimatisierung

    def get_lenkrad_farbe(self):
        """Gibt die Farbe des Lenkrads zurück."""
        return self.lenkrad_farbe

    def get_mit_lenkradheizung(self):
        """Gibt zurück, ob das Auto eine Lenkradheizung hat."""
        return self.mit_lenkradheizung

    def get_mit_ambientebeleuchtung(self):
        """Gibt zurück, ob das Auto eine Ambientebeleuchtung hat."""
        return self.mit_ambientebeleuchtung

    def get_mit_fussmatten(self):
        """Gibt zurück, ob das Auto Fußmatten hat."""
        return self.mit_fussmatten

    def get_innenhimmel_farbe(self):
        """Gibt die Farbe des Innenhimmels zurück."""
        return self.innenhimmel_farbe

    def get_mit_digitalen_tacho(self):
        """Gibt zurück, ob das Auto einen digitalen Tacho hat."""
        return self.mit_digitalen_tacho

    def get_mit_premium_navigationssystem(self):
        """Gibt zurück, ob das Auto ein Premium-Navigationssystem hat."""
        return self.mit_premium_navigationssystem

    def get_mit_feuerloescher(self):
        """Gibt zurück, ob das Auto einen Feuerlöscher hat."""
        return self.mit_feuerloescher

    def get_mit_keyless_go(self):
        """Gibt zurück, ob das Auto eine Keyless-Go Funktion hat."""
        return self.mit_keyless_go

    def get_rabatt_code(self):
        """Gibt zurück, ob ein Rabattcode angewendet wurde."""
        return self.rabatt_code

    def get_rabatt_plz(self):
        """Gibt zurück, ob ein Rabatt durch die PLZ angewendet wurde."""
        return self.rabatt_plz

    # Setter-Methoden, die auch den Preis anpassen
    def set_ps(self, ps):
        """Setzt die PS-Leistung und passt den Preis entsprechend an."""
        print("Alter Preis : " + str(self.preis))
        # self.ps = None
        self.ps = ps
        if self.ps == 258:
            print("zusätzlich : " + str(12000))
            self.preis += 12000
        if self.ps == 313:
            print("zusätzlich : " + str(22000))
            self.preis += 22000
            # self.preis = self.preis + 22000 = 65000 + 22000 = 87000

    def set_frabe(self, farbe):
        """Setzt die Autofarbe und passt den Preis für bestimmte Farben an."""
        print("Alter Preis : " + str(self.preis))
        self.farbe = farbe
        if self.farbe == 'Grau':
            print("zusätzlich : " + str(600))
            self.preis += 600
        elif self.farbe == 'Blau' or self.farbe == 'Rot':
            print("zusätzlich : " + str(900))
            self.preis += 900

    def set_raeder(self, raeder_design_type, raeder_breite):
        """Setzt das Raddesign und die Breite und passt den Preis für bestimmte Radgrößen an."""
        print("Alter Preis : " + str(self.preis))
        self.raeder_design_type = raeder_design_type # self.Attribut = Parameter
        self.raeder_breite = raeder_breite
        if self.raeder_breite == 45.7:
            print("zusätzlich : " + str(654))
            self.preis += 654

    def set_reifen(self, reifen_type):
        """Setzt den Reifentyp und passt den Preis für bestimmte Reifentypen an."""
        print("Alter Preis : " + str(self.preis))
        self.reifen_type = reifen_type
        if self.reifen_type == 'Winterreifen':
            print("zusätzlich : " + str(190))
            self.preis += 190
        elif self.reifen_type == 'Sportreifen':
            print("zusätzlich : " + str(350))
            self.preis += 350

    def set_scheinwerfer(self, scheinwerfer):
        """Setzt den Scheinwerfertyp und passt den Preis für spezielle Scheinwerfer an."""
        print("Alter Preis : " + str(self.preis))
        self.schein_werfer_type = scheinwerfer
        if self.schein_werfer_type == 'Digital Light':
            print("zusätzlich : " + str(1600))
            self.preis += 1600

    def set_panorama_schiebedach(self, mit_panorama_schiebedach):
        """Setzt die Panorama-Schiebedach-Option und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.mit_panorama_schiebedach = mit_panorama_schiebedach
        if mit_panorama_schiebedach:
            print("zusätzlich : " + str(2100))
            self.preis += 2100

    def set_w_glas(self, mit_w_glas):
        """Setzt die Wärmedämmglas-Option und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.mit_w_glas = mit_w_glas
        if mit_w_glas:
            print("zusätzlich : " + str(440))
            self.preis += 440

    def set_polster(self, polster):
        """Setzt die Polsterart und passt den Preis für bestimmte Polsterarten an."""
        print("Alter Preis : " + str(self.preis))
        self.polster = polster
        if self.polster == 'Leder Schwarz':
            print("zusätzlich : " + str(1900))
            self.preis += 1900
        if self.polster == 'Leder Weiss':
            print("zusätzlich : " + str(2100))
            self.preis += 2100

    def set_sitzHeizung(self, mit_sitzheizung):
        """Setzt die Sitzheizung."""
        self.mit_sitzheizung = mit_sitzheizung

    def set_sitzklimatisierung(self, mit_sitzklimatisierung):
        """Setzt die Sitzklimatisierung und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.mit_sitzklimatisierung = mit_sitzklimatisierung
        if mit_sitzklimatisierung:
            print("zusätzlich : " + str(1060))
            self.preis += 1060

    def set_lenkrad_farbe(self, lenkrad_farbe):
        """Setzt die Farbe des Lenkrads."""
        self.lenkrad_farbe = lenkrad_farbe

    def set_lenkradheizung(self, mit_lenkradheizung):
        """Setzt die Lenkradheizung und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.mit_lenkradheizung = mit_lenkradheizung
        if mit_lenkradheizung:
            print("zusätzlich : " + str(50))
            self.preis += 50

    def set_ambientebeleuchtung(self, mit_ambientebeleuchtung):
        """Setzt die Ambientebeleuchtung und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.mit_ambientebeleuchtung = mit_ambientebeleuchtung
        if mit_ambientebeleuchtung:
            print("zusätzlich : " + str(333))
            self.preis += 333

    def set_fussmatten(self, mit_fussmatten):
        """Setzt die Fußmatten und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.mit_fussmatten = mit_fussmatten
        if mit_fussmatten:
            print("zusätzlich : " + str(20))
            self.preis += 20

    def set_innenhimmel_farbe(self, innenhimmel_farbe):
        """Setzt die Innenhimmelfarbe und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.innenhimmel_farbe = innenhimmel_farbe
        if innenhimmel_farbe == 'Innenhimmel Schwarz':
            print("zusätzlich : " + str(400))
            self.preis += 400

    def set_digitalen_tacho(self, mit_digitalen_tacho):
        """Setzt den digitalen Tacho und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.mit_digitalen_tacho = mit_digitalen_tacho
        if mit_digitalen_tacho: # if mit_digitalen_tacho <--> if mit_digitalen_tacho == True
            print("zusätzlich : " + str(90))
            self.preis += 90

    def set_premium_navigationssystem(self, mit_premium_navigationssystem):
        """Setzt das Premium-Navigationssystem und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.mit_premium_navigationssystem = mit_premium_navigationssystem
        if mit_premium_navigationssystem:
            print("zusätzlich : " + str(90))
            self.preis += 90

    def set_feuerloescher(self, mit_feuerloescher):
        """Setzt den Feuerlöscher und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.mit_feuerloescher = mit_feuerloescher
        if mit_feuerloescher:
            print("zusätzlich : " + str(130))
            self.preis += 130

    def set_keyless_go(self, mit_keyless_go):
        """Setzt die Keyless-Go Funktion und passt den Preis an."""
        print("Alter Preis : " + str(self.preis))
        self.mit_keyless_go = mit_keyless_go
        if mit_keyless_go:
            print("zusätzlich : " + str(650))
            self.preis += 650

    def rabattAuto(self, reduzierterBetrag):
        """Setzt einen Rabatt auf den Preis des Autos."""
        self.preis -= reduzierterBetrag

    def set_rabatt_code(self, mit_rabatt_code):
        """Aktiviert den Rabattcode."""
        self.rabatt_code = mit_rabatt_code

    def set_rabatt_plz(self, mit_rabatt_plz):
        """Aktiviert den Rabatt durch die Postleitzahl."""
        self.rabatt_plz = mit_rabatt_plz
