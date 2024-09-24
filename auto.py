import math

from autokonfigurator import Auto  # Importiert die Klasse Auto aus dem Modul autokonfigurator
import random  # Importiert das random-Modul zur Generierung von Zufallswerten
import csv  # Importiert das csv-Modul, um mit CSV-Dateien zu arbeiten
from datetime import *  # Importiert alle Funktionen aus dem datetime-Modul zur Verarbeitung von Datum und Zeit
import pandas as pd  # Importiert pandas zur Datenanalyse und -verarbeitung
import matplotlib.pyplot as plt  # Importiert matplotlib.pyplot zum Erstellen von Diagrammen
import seaborn as sns  # Importiert seaborn zur Erstellung von fortgeschrittenen Visualisierungen

# Initialisierung von globalen Variablen
data = []  # Leere Liste zum Speichern von Angeboten (Daten)
plz = 0  # Variable für die Postleitzahl des Benutzers
name = ""  # Variable für den Namen des Benutzers


# Funktion zur Anzeige des Hauptmenüs
def startMenue():
    # Ausgabe
    print("##################################################################")
    print("Willkommen zum HTW Autokonfigurator")  # Begrüßungsnachricht
    print("##################################################################")
    print("Menü:")  # Menüanzeige
    print("1 - Wähle einer der folgende mercedes-benz Autos (Fahrzeugkonfiguration starten).")
    print("2 - Angebote")  # Anzeige aller aktuellen Angebote
    print("3 - Angebote durchsuchen/filtern")  # Funktion zum Durchsuchen oder Filtern von Angeboten
    print("4 - Häufigsten gekauften Modelle")  # Zeigt die am häufigsten gekauften Automodelle an
    print("5 - Statistische Auswertung")  # Zeigt statistische Diagramme an
    print("6 - Exit.")  # Beenden des Programms
    # Eingabe --> vom Typ String
    eingabe = input("Wahl: --> ")  # Fordert den Benutzer auf, eine Menüoption auszuwählen

    # im Fall, keine Zahl eingibt --> z.B. fatima --> "fatima" Als String eingegeben
    # X = Y
    # Validierung der Benutzereingabe

    # in der while-Schleife wird zuerst überprüft, ob die Eingabe keine Zahl ist
    # eingabe.isdigit() eine Methode die überprüft, ob die Varaible eingabe nur aus Ziffern[0-9] besteht
    # wenn es der Fall ist, dann wird True zurückgegeben ansonsten False
    # True --> wenn die Eingabe aus Ziffern besteht
    # False --> ansonsten
    # not ist die Negation von einer Bedingung --> not (True) --> Ergebnis : False
    #                                          --> not (False) --> Ergebnis : True
    # 1- not eingabe.isdigit() --> wenn die Eingabe keine Zahl ist
    # 2- int(eingabe) > 6
    # 3- int(eingabe) < 1

    # or --> wenn einer der bedingungen erfüllt wird dann werden die Zeilen ausgeführt
    # die umwandlung --> wichtig da wir jetzt Zahlen vergleichen
    # ==, != , >, >=, <, <=
    # In der Regel : [A] op [B] --> [A] und [B] müssen den selben Datentyp haben
    # "7" > 6
    # int(Wert/Variable) --> der Wert/Variable wird zu int umgewandelt
    # int("7") --> 7
    while not eingabe.isdigit() or int(eingabe) > 6 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Funktionen ( 1, 2, 3, 4, 5 oder 6 )")
        eingabe = input()  # Fordert erneut eine Eingabe an, falls die Eingabe ungültig ist


    eingabe = int(eingabe)  # Konvertiert die Eingabe in einen Integer
    # Aufrufen der entsprechenden Funktion basierend auf der Benutzereingabe
    if eingabe == 1:
        autoArt = subMenue()  # Zeigt das Untermenü zur Auswahl des Autos an
        # X = Y
        #  autoArt = subMenue()
        #  autoArt = 2
        wahlBearbeiten(autoArt)  # Verarbeitet die Auswahl des Autos
        autoEinstellen()  # Startet den Auto-Konfigurationsprozess

    # wir haben zwei Arten von Funktionen / Methoden
    # 1- mit Datentyp --> die Methode gibt am Ende was zurück --> die Methode hat das Schlüsseöwort return am Ende
    # Aufruf --> Variabel = NameDerMethode(Werte für die Parameters)
    # 2- mit Void --> die Methode gibt nix am Ende was zurück --> die Methode hat nicht das Schlüsseöwort return am Ende
    # Aufruf --> NameDerMethode(Werte für die Parameters)

    # Parameter :
    # wir haben eine Methode add, die die Addition zwischen zwei ganze Zahlen zurückgibt
    # Parameter sind was die Methode braucht um ihre Aufgabe erfolgreich zu machen
    # die Methode braucht zwei ganze Zahlen --> dafür hat die Methode 2 Parameter (zwei ganze Zahlen)
    # die Parameter werden wie folgt geschrieben --> NameDerMethode(Parameter_1, Parameter_2, ... Parameter_n)
    elif eingabe == 2:
        zeigenAngebote()  # Zeigt alle verfügbaren Angebote an # yassmin
    elif eingabe == 3:
        sucheAngebote()  # Ermöglicht das Durchsuchen der Angebote # yassmin
    elif eingabe == 4:
        zeigenHaeufigsteGekaufteModelle()  # Zeigt die am häufigsten gekauften Modelle an
    elif eingabe == 5:
        zeigeDiagramma()  # Zeigt statistische Auswertungen (Diagramme) an # yassmin
    else:
        print("Auf Wiedersehen :)")  # Verabschiedet den Benutzer
        exit(0)  # Beendet das Programm


# Funktion zur Anzeige von Diagrammen basierend auf Verkaufsdaten
def zeigeDiagramma():
    print("Diagramm : ")  # Zeigt den Diagrammmodus an
    print("Wähle einer der folgende Diagramms : ")
    print("1 - Verkaufszahlen pro Modell.")  # Option zur Anzeige der Verkaufszahlen pro Automodell
    print("2 - Durchschnittlicher Preis pro Automodell")  # Option zur Anzeige des durchschnittlichen Preises pro Modell
    print("3 - Verkäufe im Zeitverlauf.")  # Option zur Anzeige der Verkäufe im Zeitverlauf
    eingabe = input("Wahl: --> ")  # Benutzer gibt die Auswahl ein

    # Validierung der Benutzereingabe
    while not eingabe.isdigit() or int(eingabe) > 3 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Autos ( 1, 2 oder 3 )")
        eingabe = input()  # Fordert erneut eine Eingabe an, falls die Eingabe ungültig ist
    eingabe = int(eingabe)  # Konvertiert die Eingabe in einen Integer

    # Liest die Daten aus der CSV-Datei 'autos.csv'
    daten = pd.read_csv('autos.csv', delimiter=';', encoding='utf-8')

    # Verarbeitung der Diagrammauswahl
    if eingabe == 1:  # Verkaufszahlen pro Modell

        plt.figure()  # Erstellt eine neue Grafik
        verkaufProModell = daten.groupby('Gewählte Automodell').size().reset_index(name='Verkäufe')  # Gruppiert die Daten nach Automodell und zählt die Verkäufe
        print(verkaufProModell)
        sns.barplot(x='Gewählte Automodell', y='Verkäufe', data=verkaufProModell)  # Erstellt ein Balkendiagramm
        plt.title('Verkaufszahlen pro Automodell')  # Setzt den Titel des Diagramms
        plt.xlabel('Automodell')  # Beschriftet die X-Achse
        plt.ylabel('Verkäufe')  # Beschriftet die Y-Achse
        plt.show()  # Zeigt das Diagramm an

    elif eingabe == 2:  # Durchschnittlicher Preis pro Automodell
        plt.figure()  # Erstellt eine neue Grafik
        durchschnittlicherPreis = daten.groupby('Gewählte Automodell')['Der Endpreis ist'].mean().reset_index()  # Berechnet den Durchschnittspreis pro Automodell
        print(durchschnittlicherPreis)
        sns.barplot(x='Gewählte Automodell', y='Der Endpreis ist',
                    data=durchschnittlicherPreis)  # Erstellt ein Balkendiagramm
        plt.title('Durchschnittlicher Verkaufspreis pro Automodell')  # Setzt den Titel des Diagramms
        plt.xlabel('Automodell')  # Beschriftet die X-Achse
        plt.ylabel('Durchschnittlicher Preis (in Euro)')  # Beschriftet die Y-Achse
        plt.show()  # Zeigt das Diagramm an

    else:  # Verkäufe im Zeitverlauf
        plt.figure()  # Erstellt eine neue Grafik
        verkaufen_Zeit = daten.groupby('Bestellung-Datum').size().reset_index(name='Verkäufe')  # Gruppiert die Verkäufe nach Datum
        print(verkaufen_Zeit)
        sns.lineplot(x='Bestellung-Datum', y='Verkäufe', data=verkaufen_Zeit)  # Erstellt ein Liniendiagramm
        plt.title('Verkäufe im Zeitverlauf')  # Setzt den Titel des Diagramms
        plt.xlabel('Datum')  # Beschriftet die X-Achse
        plt.ylabel('Verkäufe')  # Beschriftet die Y-Achse
        plt.show()  # Zeigt das Diagramm an


# Funktion zur Anzeige der am häufigsten gekauften Modelle
def zeigenHaeufigsteGekaufteModelle():
    # Initialisierung von Variablen für die Zählung der verkauften Modelle
    zahlDerKaeuferModell_1 = 0 # SY C-Klasse
    zahlDerKaeuferModell_2 = 0 # FW E-Klasse
    zahlDerKaeuferModell_3 = 0 # DBW SLR

    # Wenn es noch keine Verkäufe gibt
    if len(data) == 0:
        print("Momentan wurde kein Auto verkauft")  # Ausgabe einer Nachricht, dass keine Verkäufe vorhanden sind
    else:
        # Durchlaufen aller vorhandenen Angebote
        for angebot in data:
            # Zählen der Verkäufe für jedes Automodell
            if angebot['Gewählte Automodell'] == 'SY C-Klasse':
                zahlDerKaeuferModell_1 = zahlDerKaeuferModell_1 + 1
            if angebot['Gewählte Automodell'] == 'FW E-Klasse':
                zahlDerKaeuferModell_2 = zahlDerKaeuferModell_2 + 1
            if angebot['Gewählte Automodell'] == 'DBW SLR':
                zahlDerKaeuferModell_3 = zahlDerKaeuferModell_3 + 1

        # Sortieren der Zählungen, um das meistverkaufte Modell zu finden
        l1 = [zahlDerKaeuferModell_1, zahlDerKaeuferModell_2, zahlDerKaeuferModell_3]
        # l1 = [ Anzahl_Alle_Angebote_Mit_Der_Klasse_SY C-Klasse, Anzahl_Alle_Angebote_Mit_Der_Klasse_FW E-Klasse, Anzahl_Alle_Angebote_Mit_Der_Klasse_DBW SLR]
        print(l1)
        l1.sort()
        print(l1)

        hModelle = []  # Liste der häufigsten Modelle
        # index = -1 --> bedeutet das letzte Element
        # index = -2 --> das vorletzte Element
        # Überprüfen, welches Modell am häufigsten gekauft wurde

        # zahlDerKaeuferModell_1 = 1
        # zahlDerKaeuferModell_2 = 9
        # zahlDerKaeuferModell_3 = 9
        # l1 = [1 , 9, 9]
        if l1[-1] == zahlDerKaeuferModell_1:
            print("Am häufigsten gekauften Automodell ist SY C-Klasse : wurde " + str(
                zahlDerKaeuferModell_1) + " Mal gekauft.")
            hModelle.append('SY C-Klasse')
        if l1[-1] == zahlDerKaeuferModell_2:
            print("Am häufigsten gekauften Automodell ist FW E-Klasse : wurde " + str(
                zahlDerKaeuferModell_2) + " Mal gekauft.")
            hModelle.append('FW E-Klasse')
        if l1[-1] == zahlDerKaeuferModell_3:
            print("Am häufigsten gekauften Automodell ist DBW SLR : wurde " + str(
                zahlDerKaeuferModell_3) + " Mal gekauft.")
            hModelle.append('DBW SLR')

        # hModelle = [FW E-Klasse, DBW SLR]
        # Berechnung des durchschnittlichen Verkaufspreises für jedes Modell
        for e in hModelle:
            anzahl = 0
            preis = 0
            for angebot in data:
                if angebot['Gewählte Automodell'] == e:
                    anzahl = anzahl + 1
                    preis = preis + int(angebot['Der Endpreis ist'])
            print('Modell : ' + e)
            print("durchschnittlichen Verkaufspreis : " + str(preis / anzahl))


# Funktion zum Durchsuchen der Angebote basierend auf dem Namen des Käufers
def sucheAngebote(): # Yassmin
    global name
    print("\nAngebote : ")  # Anzeige des Titels
    if len(data) == 0:  # Wenn keine Angebote vorhanden sind
        print("Momentan gibt es keine Angebote")  # Ausgabe einer Nachricht, dass keine Angebote vorhanden sind
    else:
        namekaeufer = input("Geben Sie der Name des gesuchten Käufers ein :")  # Benutzer gibt den Namen des Käufers ein
        nummerDesAngebotes = 0
        kaeuferAngebote = []  # Liste, um Angebote des gesuchten Käufers zu speichern
        kaeuferGefunden = False  # Flag, um festzustellen, ob der Käufer gefunden wurde

        # namekaeufer = Ali
        """
                nummerDesAngebotes = 0

        1- Index = 0 : Sara    Nein nummerDesAngebotes = 1
        2- Index = 1 : Ali     Ja kaeuferAngebote[1] nummerDesAngebotes = 2
        3- Index = 2 : Alaa    Nein nummerDesAngebotes = 3
        4- Index = 3 : Aya     Nein nummerDesAngebotes = 4
        5- Index = 4 : Yassmin Nein nummerDesAngebotes = 5
        6- Index = 5 : Ali     Ja kaeuferAngebote[1, 5] nummerDesAngebotes = 6
        
        
        eingabe = 4 --> gültig oder nicht ? was gültig ist [1, 5]
        int(eingabe) - 1 not in kaeuferAngebote
        eingabe = 6 -->  int(eingabe) - 1 -->  int("6") - 1 --> 6 - 1 --> 5 not in kaeuferAngebote
        """
        # Durchlaufen der vorhandenen Daten, um den Käufer zu finden
        for angebot in data:
            if namekaeufer == angebot['Name des Verkäufers']:
                print("Der gesuchte Käufer hat folgendes gekauft: ")  # Ausgabe der gekauften Fahrzeuge
                print("---------------------------------------------------")
                info = ""
                for e in data[nummerDesAngebotes]:
                    info += e + " : " + angebot[e] + '\n'  # Ausgabe der Details des Angebots
                print(str(nummerDesAngebotes + 1) + " - " + info)
                kaeuferGefunden = True
                kaeuferAngebote.append(nummerDesAngebotes)  # Speichern der Angebotsnummer
            nummerDesAngebotes = nummerDesAngebotes + 1 # = 1

        if kaeuferGefunden:  # Wenn der Käufer gefunden wurde
            print("Gebe die Nummer des ausgewählten Angebot ein : ")  # Benutzer wird aufgefordert, eine Angebotsnummer auszuwählen
            eingabe = input("Wahl: --> ")
            # Validierung der Eingabe
            while not eingabe.isdigit() or int(eingabe) - 1 not in kaeuferAngebote:
                print("Bitte geben Sie nur die Nummer einer der oben stehenden Angebote ein!!")
                eingabe = input()
            eingabe = int(eingabe)

            # Ausgabe der Details des ausgewählten Angebots
            info = []
            for e in data[eingabe - 1]:
                info.append(data[eingabe - 1][e])

            info.pop(0)  # Entfernen der ersten und letzten Elemente (Name und Datum)
            info.pop()

            name = input("Geben Sie Ihr Name ein : ")  # Benutzer gibt seinen Namen ein
            kaufbestaetigen(info)  # Aufruf der Kaufbestätigungsfunktion
        else:
            print("Käufer ist nicht gefunden!")  # Nachricht, wenn der Käufer nicht gefunden wird


# Funktion zum Anzeigen aller aktuellen Angebote
def zeigenAngebote():
    global name
    print("\nAngebote : ")  # Ausgabe des Titels
    if len(data) == 0:  # Wenn keine Angebote vorhanden sind
        print("Momentan gibt es keine Angebote")  # Nachricht, dass keine Angebote vorhanden sind
    else:
        nummerDesAngebotes = 1
        # Durchlaufen aller vorhandenen Angebote und Ausgabe der Details
        for angebot in data:
            # angebot =  {'Name des Verkäufers': 'Sara', 'Gewählte Automodell': 'DBW SLR', 'PS': '258', 'Autofarbe': 'Grau', 'Raeder': '43.2 - 5-Speichen-Design', 'Reifentyp': 'Winterreifen', 'Scheinwerfer': 'Digital Light', 'Mit Panorama-Schiebedach': 'True', 'Mit einem wärmedämmend dunkel getöntes Glas': 'True', 'Polster': 'Ledernachbildung schwarz', 'Mit Sitzheizung': 'False', 'Mit Sitzklimatisierung': 'True', 'Lenkradfarbe': 'Grau', 'Mit Lenkradheizung': 'True', 'Mit einer Ambientebeleuchtung': 'True', 'Mit einem Fußmatten': 'True', 'Innenhimmelfarbe': 'Innenhimmel Kristall grau', 'Mit digitalen Tacho': 'True', 'Mit einem Premium-Navigationssystem': 'True', 'Mit einem Feuerlöscher': 'True', 'Mit einem Keyless-Go': 'True', 'Der Endpreis ist': '106353', 'Rabatt durch einen Code': 'False', 'Rabatt durch PLZ': 'False', 'Bestellung-Datum': '2024-09-08'}
            # angebot =  {'Name des Verkäufers': 'Ali', 'Gewählte Automodell': 'DBW SLR', 'PS': '258', 'Autofarbe': 'Grau', 'Raeder': '43.2 - 5-Speichen-Design', 'Reifentyp': 'Sommerreifen',
            info = ""
            for e in angebot: # e --> schlüssel , angebot[e] --> der Wert von dieser SChüssel
                info += e + " : " + angebot[e] + '\n'
            # info += Name des Verkäufers : Ali
            #         Gewählte Automodell : DBW SLR
            #                          PS : 258
            print(str(nummerDesAngebotes) + " - " + info)
            print("---------------------------\n")
            nummerDesAngebotes += 1 # = 2 # = 3 # am Ende nummerDesAngebotes = 15

        print("Gebe die Nummer des ausgewählten Angebot ein : ")  # Benutzer wird aufgefordert, eine Angebotsnummer auszuwählen
        eingabe = input("Wahl: --> ")

        # Validierung der Benutzereingabe
        while not eingabe.isdigit() or int(eingabe) > nummerDesAngebotes or int(eingabe) < 1:
            print("Bitte geben Sie nur die Nummer einer der oben stehenden Angebote ein!!")
            eingabe = input()

        eingabe = int(eingabe)
        info = []
        for e in data[eingabe - 1]:
            info.append(data[eingabe - 1][e])

        info.pop(0)  # Entfernen des ersten und letzten Eintrags (Name und Datum)
        info.pop()

        name = input("Geben Sie Ihr Name ein : ")  # Benutzer gibt seinen Namen ein
        kaufbestaetigen(info)  # Bestätigung des Kaufs


# Funktion zur Anzeige des Untermenüs zur Auswahl des Autos
def subMenue():
    print("1 - SY C-Klasse ab 47.000 Euro (Autom. 9-Gang, 4 Türen und 5 Sitzer)")  # Option für C-Klasse
    print("2 - FW E-Klasse ab 64.000 Euro (Autom. 6-Gang, 4 Türen und 5 Sitzer)")  # Option für E-Klasse
    print("3 - DBW SLR ab 87.000 Euro (Autom. 9-Gang, 2 Türen und 2 Sitzer)")  # Option für SLR
    eingabe = input("Wahl: --> ")  # Benutzer gibt die Auswahl ein
    # Validierung der Benutzereingabe
    while not eingabe.isdigit() or int(eingabe) > 3 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Autos ( 1, 2 oder 3 )")
        eingabe = input()
    # jede Eingabe hat den Datentyp --> String
    # eingabe --> "2" ist keine Zahl sondern ein String
    # damit wir die Eingabe als Zahl haben, --> müssen umwandeln vom String zu int
    eingabe = int(eingabe)  # Konvertiert die Eingabe in einen Integer
    return eingabe  # Gibt die Auswahl des Benutzers zurück


# Funktion zum Verarbeiten der Auswahl des Autos
def wahlBearbeiten(autoArt):
    # autoArt = 2
    global auto
    # d.h. global --> ist nötwendig, da wenn wir diese Variabel/Liste/... ändern, dann wird überall geändert


    # Initialisiert das Auto-Objekt basierend auf der Auswahl des Benutzers
    if autoArt == 1:
        auto = Auto(47000, 1, "SY C-Klasse")  # C-Klasse
    elif autoArt == 2:
        auto = Auto(65000, 2, "FW E-Klasse")  # E-Klasse
    else:
        auto = Auto(87000, 3, "DBW SLR")  # SLR


# Funktion zum Konfigurieren des Autos (Ausstattungsoptionen)
def autoEinstellen():
    # get_preis() ist eine Methode von der Klasse Auto
    # um eine Methode von einer Klasse aufzurufen, wie folgt;
    # NameEinesObjektVonDerKlasse.NameDerMethode(Werte für die Parameter)
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")  # Zeigt den aktuellen Preis des Autos an
    motor()  # Benutzer wählt den Motor
    # Form einer Funktion --> Name(Werte für Parameter)
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    farbe()  # Benutzer wählt die Farbe # sevda
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    raeder()  # Benutzer wählt die Räder # sevda
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    reifen()  # Benutzer wählt die Reifen # sevda
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    scheinwerfer()  # Benutzer wählt die Scheinwerfer # sevda
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    autoExterieur()  # Benutzer konfiguriert das Exterieur # sevda
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    polster()  # Benutzer wählt die Polsterung # sevda
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    autoPolster = auto.get_polster()  # Speichert die gewählte Polsterung # sevda
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    if autoPolster == 'Leder Schwarz' or autoPolster == 'Leder Weiss':  # Wenn die Polsterung Leder ist, fragt nach Sitzheizung
        sitzHeizung() # sevda
        print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    sitzklimatisierung()  # Benutzer wählt Sitzklimatisierung # sevda
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    lenkradFarbe()  # Benutzer wählt die Lenkradfarbe # fatima
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    lenkradheizung()  # Benutzer wählt Lenkradheizung # fatima
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    ambiente()  # Benutzer wählt Ambientebeleuchtung # fatima
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    fussmatten()  # Benutzer wählt Fußmatten # fatima
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    innenhimmelFarbe()  # Benutzer wählt die Innenhimmelfarbe # fatima
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    tacho()  # Benutzer wählt einen digitalen Tacho # fatima
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    if auto.get_mit_digitalen_tacho():  # Wenn digitaler Tacho gewählt wurde, fragt nach Navigationssystem
        premiumNavigationssystem() # fatima
        print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    feuerloescher()  # Benutzer wählt Feuerlöscher # fatima
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    keyless_go()  # Benutzer wählt Keyless-Go # fatima
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    persoenlicheInfo()  # Benutzer gibt persönliche Informationen ein # weddad
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")
    rabatt()  # Rabattverarbeitung # weddad
    print("Aktueller Preis : " + str(auto.get_preis()) + " Euro")

    # Speichern der Konfiguration des Autos als Liste
    info = [auto.get_modell(), str(auto.get_ps()), auto.get_farbe(),
            str(auto.get_raeder_breite()) + " - " + auto.get_raeder_design_type(),
            auto.get_reifen_type(), auto.get_schein_werfer_type(), str(auto.get_mit_panorama_schiebedach()),
            str(auto.get_mit_w_glas()), auto.get_polster(), str(auto.get_mit_sitzheizung()),
            str(auto.get_mit_sitzklimatisierung()), auto.get_lenkrad_farbe(), str(auto.get_mit_lenkradheizung()),
            str(auto.get_mit_ambientebeleuchtung()), str(auto.get_mit_fussmatten()), auto.get_innenhimmel_farbe(),
            str(auto.get_mit_digitalen_tacho()), str(auto.get_mit_premium_navigationssystem()),
            str(auto.get_mit_feuerloescher()), str(auto.get_mit_keyless_go()), str(auto.get_preis()),
            str(auto.get_rabatt_code()), str(auto.get_rabatt_plz())]
    # info = ["FW E-Klasse", "313", "Weiss", "43.2 - 5-Speichen-Design", "Winterreifen", "Digital Light",
    # in jede Liste stehen Elemente
    # Positionen oder Index fängt von 0 bis n-1 nach rechts , wobei n ist die Anzahl der Elemente
    # l1 = [e1, e2, e3, e4, ...., en]
    #       0   1    2  3         n-1
    # z.B.
    # l1 = ["Sevda", "Fatima", "Yassmin"]
    #          0         1          2
    # l1[2] --> "Yassmin"

    kaufbestaetigen(info)  # Bestätigungsprozess


# Funktion zur Bestätigung des Kaufs und Speichern der Konfiguration
def kaufbestaetigen(info):
    print("Ausgewähltes Auto - Modell : " + info[0])  # Zeigt das ausgewählte Modell an
    print("Konfigurationsoptionen : ")  # Zeigt alle Konfigurationsoptionen an

    # Ausgabe aller Konfigurationsdetails
    print("PS : " + info[1])
    print("Autofarbe : " + info[2])
    print("Räder : " + info[3])
    print("Reifentyp : " + info[4])
    print("Scheinwerfer : " + info[5])
    print("Mit Panorama-Schiebedach : " + info[6])
    print("Mit einem wärmedämmend dunkel getöntes Glas : " + info[7])
    print("Polster : " + info[8])
    print("Mit Sitzheizung : " + info[9])
    print("Mit Sitzklimatisierung : " + info[10])
    print("Lenkradfarbe : " + info[11])
    print("Mit Lenkradheizung : " + info[12])
    print("Mit einer Ambientebeleuchtung : " + info[13])
    print("Mit einem Fußmatten : " + info[14])
    print("Innenhimmelfarbe : " + info[15])
    print("Mit digitalen Tacho : " + info[16])
    print("Mit einem Premium-Navigationssystem : " + info[17])
    print("Mit einem Feuerlöscher : " + info[18])
    print("Mit einem Keyless-Go : " + info[19])
    print("Der Endpreis ist : " + info[20])
    print("Rabatt durch einen Code : " + info[21])
    print("Rabatt durch PLZ : " + info[22])
    datum = date.today()  # Aktuelles Datum
    print("Bestellung-Datum : " + str(datum))  # Zeigt das Bestelldatum an
    print("--------------------------------------------------------------------")
    print("Bestätigen Sie den Kauf des Autos : ")  # Fordert den Benutzer auf, den Kauf zu bestätigen
    print("1 - Ja")
    print("2 - Nein")

    eingabe = input("Wahl: --> ")  # Benutzer trifft eine Wahl
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)  # Konvertiert die Eingabe in einen Integer

    # Wenn der Benutzer den Kauf bestätigt, wird das Angebot gespeichert
    if eingabe == 1:
        data.append({"Name des Verkäufers": str(name), "Gewählte Automodell": info[0], "PS": info[1],
                     "Autofarbe": info[2], "Raeder": info[3],
                     "Reifentyp": info[4], "Scheinwerfer": info[5],
                     "Mit Panorama-Schiebedach": info[6],
                     "Mit einem wärmedämmend dunkel getöntes Glas": info[7],
                     "Polster": info[8],
                     "Mit Sitzheizung": info[9],
                     "Mit Sitzklimatisierung": info[10],
                     "Lenkradfarbe": info[11],
                     "Mit Lenkradheizung": info[12],
                     "Mit einer Ambientebeleuchtung": info[13],
                     "Mit einem Fußmatten": info[14],
                     "Innenhimmelfarbe": info[15],
                     "Mit digitalen Tacho": info[16],
                     "Mit einem Premium-Navigationssystem": info[17],
                     "Mit einem Feuerlöscher": info[18],
                     "Mit einem Keyless-Go": info[19],
                     "Der Endpreis ist": info[20],
                     "Rabatt durch einen Code": info[21],
                     "Rabatt durch PLZ": info[22],
                     "Bestellung-Datum": str(datum)
                     })
        speichereAngebot(data)  # Speichern der Daten in die CSV-Datei


# Funktion zum Speichern des Angebots in einer CSV-Datei
def speichereAngebot(data):
    with open('autos.csv', mode='w', newline='', encoding='utf-8') as csvfile:  # Öffnet die CSV-Datei zum Schreiben
        fieldnames = data[0].keys()  # Feldnamen aus den Schlüsseln des ersten Datensatzes
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")  # Erstellt ein DictWriter-Objekt
        writer.writeheader()  # Schreibt die Kopfzeile in die CSV-Datei
        for row in data:  # Durchläuft die Daten und schreibt jede Zeile in die CSV-Datei
            writer.writerow(row)
        """
        data
        Index = 0 : {'Name des Verkäufers': 'Sara', 'Gewählte Automodell': 'DBW SLR', 'PS': '258', 'Autofarbe': 'Grau', 'Raeder': '43.2 - 5-Speichen-Design', 'Reifentyp': 'Winterreifen', 'Scheinwerfer': 'Digital Light', 'Mit Panorama-Schiebedach': 'True', 'Mit einem wärmedämmend dunkel getöntes Glas': 'True', 'Polster': 'Ledernachbildung schwarz', 'Mit Sitzheizung': 'False', 'Mit Sitzklimatisierung': 'True', 'Lenkradfarbe': 'Grau', 'Mit Lenkradheizung': 'True', 'Mit einer Ambientebeleuchtung': 'True', 'Mit einem Fußmatten': 'True', 'Innenhimmelfarbe': 'Innenhimmel Kristall grau', 'Mit digitalen Tacho': 'True', 'Mit einem Premium-Navigationssystem': 'True', 'Mit einem Feuerlöscher': 'True', 'Mit einem Keyless-Go': 'True', 'Der Endpreis ist': '106353', 'Rabatt durch einen Code': 'False', 'Rabatt durch PLZ': 'False', 'Bestellung-Datum': '2024-09-08'}
        Index = 1 : {'Name des Verkäufers': 'Ali', 'Gewählte Automodell': 'DBW SLR', 'PS': '258', 'Autofarbe': 'Grau', 'Raeder': '43.2 - 5-Speichen-Design', 'Reifentyp': 'Sommerreifen', 'Scheinwerfer': 'LED High Perfomance-Scheinwerfer', 'Mit Panorama-Schiebedach': 'True', 'Mit einem wärmedämmend dunkel getöntes Glas': 'True', 'Polster': 'Ledernachbildung schwarz', 'Mit Sitzheizung': 'False', 'Mit Sitzklimatisierung': 'True', 'Lenkradfarbe': 'Schwarz', 'Mit Lenkradheizung': 'False', 'Mit einer Ambientebeleuchtung': 'False', 'Mit einem Fußmatten': 'False', 'Innenhimmelfarbe': 'Innenhimmel Kristall grau', 'Mit digitalen Tacho': 'True', 'Mit einem Premium-Navigationssystem': 'True', 'Mit einem Feuerlöscher': 'False', 'Mit einem Keyless-Go': 'True', 'Der Endpreis ist': '104030', 'Rabatt durch einen Code': 'False', 'Rabatt durch PLZ': 'False', 'Bestellung-Datum': '2024-09-0'}
        
        ersten Durchlauf : row = index = 0 => {'Name des Verkäufers': 'Sara', 'Gewählte Automodell': 'DBW SLR', 'PS': '258', 'Autofarbe': 'Grau', 'Raeder': '43.2 - 5-Speichen-Design', 'Reifentyp': 'W ....
        zweiten Durchlauf : row = index = 1 => {'Name des Verkäufers': 'Ali', 'Gewählte Automodell': 'DBW SLR', 'PS': '258', 'Autofarbe': 'Grau', 'Raeder': '43.2 - 5-Speichen-Design', 'Reifentyp': 'Sommerreifen', 'Scheinw ...
        csv datei:
        Name des Verkäufers;Gewählte Automodell;PS;Autofarbe;Raeder;Reifentyp;Scheinwerfer;Mit Panorama-Schiebedach;Mit einem wärmedämmend dunkel getöntes Glas;Polster;Mit Sitzheizung;Mit Sitzklimatisierung;Lenkradfarbe;Mit Lenkradheizung;Mit einer Ambientebeleuchtung;Mit einem Fußmatten;Innenhimmelfarbe;Mit digitalen Tacho;Mit einem Premium-Navigationssystem;Mit einem Feuerlöscher;Mit einem Keyless-Go;Der Endpreis ist;Rabatt durch einen Code;Rabatt durch PLZ;Bestellung-Datum
        Sara;DBW SLR;258;Grau;43.2 - 5-Speichen-Design;Winterreifen;Digital Light;True;True;Ledernachbildung schwarz;False;True;Grau;True;True;True;Innenhimmel Kristall grau;True;True;True;True;106353;False;False;2024-09-08
        Ali;DBW SLR;258;Grau;43.2 - 5-Speichen-Design;Sommerreifen;LED High Perfomance-Scheinwerfer;True;True;Ledernachbildung schwarz;False;True;Schwarz;False;False;False;Innenhimmel Kristall grau;True;True;False;True;104030;False;False;2024-09-0
        """


# Funktion zur Bearbeitung von Rabatten
def rabatt():
    print("Haben Sie einen Rabatt-Code : ")
    print("1 - Ja")
    print("2 - Nein")

    eingabe = input("Wahl: --> ")  # Benutzer gibt eine Auswahl ein
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    if eingabe == 1:  # Wenn der Benutzer einen Rabatt-Code hat
        code = int(input("Geben Sie den Rabatt-Code (Ziffern) ein : "))  # Benutzer gibt den Rabatt-Code ein
        if code > 9999 and code < 100000:  # Gültigkeitsprüfung des Codes
            reduzierterBetrag = 0  # Initialisierung des reduzierten Betrags
            # Regel --> abcde : reduzierter Betrag = a + b + c + d + e
            # 12345 : reduzierter Betrag = 5 + 4 + 3 + 2 + 1  = 15
            # abcde
            # 54632 : reduzierter Betrag = 2 + 3 + 6 + 4 + 5 = 20


            # Regel : wie kann ich auf die letzte Ziffer zugreifen :
            # Zahl % 10 = gibt uns die letzte Ziffer (rechts)
            # z.B. 23137 % 10 = 7
            # Regel : wie kann ich die letzte Ziffer entfernen :
            # zahl / 10 = die selbe Zahl ohne die letzt Ziffer (rechts)
            # z.B. 23137 / 10 = 2313

            # 54632 rabatt - code:
            # reduzierter Betrag = 2 + 3 + 6 + 4 + 5
            # code = 54632
            while code > 0:  # Berechnung des Rabatts
                # reduzierterBetrag = 0 + int(54632 % 10) = 0 + 2 = 2
                # reduzierterBetrag = 2 + int(5463 % 10) = 2 + 3 = 5
                # reduzierterBetrag = 5 + int(546 % 10) = 5 + 6 = 11
                # reduzierterBetrag = 11 + int(54 % 10) = 11 + 4 = 15
                # reduzierterBetrag = 15 + int(5 % 10) = 15 + 5 = 20
                reduzierterBetrag += int(code % 10)
                # code = 5463
                # code = 546
                # code = 54
                # code = 5
                # code = 0
                code = int(code / 10)
            # reduzierterBetrag = 20
            # reduzierterBetrag = int(20 * 100) = 2000
            reduzierterBetrag = int(reduzierterBetrag * 100)

            auto.rabattAuto(reduzierterBetrag)  # Rabatt wird auf den Auto-Preis angewendet
            auto.set_rabatt_code(True)  # Rabatt-Code wird gesetzt


# Funktion zur Eingabe persönlicher Informationen
def persoenlicheInfo():
    global name, plz
    print("Persönliche Informationen : ")  # Ausgabe des Titels
    name = input("Geben Sie Ihr Name ein : ")  # Benutzer gibt seinen Namen ein
    plz = input("Geben Sie Ihre PLZ ein : ")  # Benutzer gibt seine Postleitzahl ein
    if int(plz) == 66123:  # Wenn die PLZ einem bestimmten Wert entspricht, wird ein Rabatt angewendet
        auto.rabattAuto(2000)  # Rabatt von 2000 Euro
        auto.set_rabatt_plz(True)  # Rabatt wird auf die PLZ angewendet


# Funktion zur Auswahl des Motors
def motor():
    global auto
    print("Wähle einer des folgenden Motors")
    print("1 - 170 ps")  # Option für 170 PS
    print("2 - 258 ps")  # Option für 258 PS
    print("3 - 313 ps")  # Option für 313 PS
    eingabe = input("Wahl: --> ")  # Benutzer wählt einen Motor
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 3 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Autos ( 1, 2 oder 3 )")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen des PS-Wertes basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_ps(170)
    elif eingabe == 2:
        auto.set_ps(258)
    else:
        auto.set_ps(313)


# Funktion zur Auswahl der Farbe
def farbe():
    print("Wähle einer der folgenden Farben")
    print("1 - Schwarz")  # Option für Schwarz
    print("2 - Weiss")  # Option für Weiß
    print("3 - Grau")  # Option für Grau
    print("4 - Blau")  # Option für Blau
    print("5 - Rot")  # Option für Rot
    eingabe = input("Wahl: --> ")  # Benutzer wählt eine Farbe
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 5 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Farben ( 1, 2, 3, 4 oder 5 )")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen der Autofarbe basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_frabe('Schwarz')
    elif eingabe == 2:
        auto.set_frabe('Weiss')
    elif eingabe == 3:
        auto.set_frabe('Grau')
    elif eingabe == 4:
        auto.set_frabe('Blau')
    else:
        auto.set_frabe('Rot')


# Funktion zur Auswahl der Räder
def raeder():
    print("Wähle einer der folgenden Räder")
    print("1 - 43.2 cm (17) Leichtmetallräder im 5-Speichen-Design")  # Option für 43,2 cm Leichtmetallräder
    print("2 - 45.7 cm (18) Leichtmetallräder im 5-Doppelspeichen-Design")  # Option für 45,7 cm Leichtmetallräder
    eingabe = input("Wahl: --> ")  # Benutzer wählt die Räder
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Räder ( 1 oder 2 )")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen der Räder basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_raeder('5-Speichen-Design', 43.2)
    else:
        auto.set_raeder('5-Doppelspeichen-Design', 45.7)


# Funktion zur Auswahl der Reifen
def reifen():
    print("Wähle einer der folgenden Reifen")
    print("1 - Sommerreifen")  # Option für Sommerreifen
    print("2 - Winterreifen")  # Option für Winterreifen
    print("3 - Sportreifen")  # Option für Sportreifen
    eingabe = input("Wahl: --> ")  # Benutzer wählt die Reifen
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 3 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Reifen ( 1, 2 oder 3 )")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen des Reifentyps basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_reifen('Sommerreifen')
    elif eingabe == 2:
        auto.set_reifen('Winterreifen')
    else:
        auto.set_reifen('Sportreifen')


# Funktion zur Auswahl der Scheinwerfer
def scheinwerfer():
    print("Wähle einer der folgenden Scheinwerfer")
    print("1 - LED High Perfomance-Scheinwerfer")  # Option für LED High Performance
    print("2 - Digital Light")  # Option für Digital Light
    eingabe = input("Wahl: --> ")  # Benutzer wählt die Scheinwerfer
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Scheinwerfer ( 1 oder 2 )")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen des Scheinwerfers basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_scheinwerfer('LED High Perfomance-Scheinwerfer')
    else:
        auto.set_scheinwerfer('Digital Light')


# Funktion zur Konfiguration des Exterieurs
def autoExterieur():
    print("Exterieur:")
    print("_________")
    print("Wünschen Sie sich ein Panorama-Schiebedach ? ")
    print("1 - Ja")  # Option für Panorama-Schiebedach
    print("2 - Nein")  # Option ohne Panorama-Schiebedach
    eingabe = input("Wahl: --> ")  # Benutzer wählt die Option
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen des Panorama-Schiebedachs basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_panorama_schiebedach(True)
    else:
        auto.set_panorama_schiebedach(False)

    print("Wünschen Sie sich ein wärmedemmend dunkel getöntes Glas ? ")
    print("1 - Ja")  # Option für wärmedämmendes Glas
    print("2 - Nein")  # Option ohne getöntes Glas
    eingabe = input("Wahl: --> ")  # Benutzer wählt die Option
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen des wärmedämmenden Glases basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_w_glas(True)
    else:
        auto.set_w_glas(False)


# Funktion zur Auswahl der Polster
def polster():
    print("Wähle einer der folgenden Polster")
    print("1 - Ledernachbildung schwarz")  # Option für Ledernachbildung
    print("2 - Alcantara schwarz")  # Option für Alcantara
    print("3 - Leder Schwarz")  # Option für Leder Schwarz
    print("4 - Leder Weiss")  # Option für Leder Weiß
    eingabe = input("Wahl: --> ")  # Benutzer wählt die Polster
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 4 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Polster ( 1, 2, 3 oder 4 )")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen der Polster basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_polster('Ledernachbildung schwarz')
    elif eingabe == 2:
        auto.set_polster('Alcantara schwarz')
    elif eingabe == 3:
        auto.set_polster('Leder Schwarz')
    else:
        auto.set_polster('Leder Weiss')


# Funktion zur Auswahl der Sitzheizung
def sitzHeizung():
    print("Wünschen Sie sich eine Sitzheizung ?")
    print("1 - Ja")  # Option für Sitzheizung
    print("2 - Nein")  # Option ohne Sitzheizung
    eingabe = input("Wahl: --> ")  # Benutzer wählt die Option
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen der Sitzheizung basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_sitzHeizung(True)
    else:
        auto.set_sitzHeizung(False)


# Funktion zur Auswahl der Sitzklimatisierung
def sitzklimatisierung():
    print("Wünschen Sie sich eine Sitzklimatisierung ?")
    print("1 - Ja")  # Option für Sitzklimatisierung
    print("2 - Nein")  # Option ohne Sitzklimatisierung

    eingabe = input("Wahl: --> ")  # Benutzer wählt die Option
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen der Sitzklimatisierung basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_sitzklimatisierung(True)
    else:
        auto.set_sitzklimatisierung(False)
        auto.set_sitzHeizung(True)


# Funktion zur Auswahl der Lenkradfarbe
def lenkradFarbe():
    print("Wähle einer der folgenden Farben für den Lenkrad")
    print("1 - Grau")  # Option für graues Lenkrad
    print("2 - Schwarz")  # Option für schwarzes Lenkrad
    eingabe = input("Wahl: --> ")  # Benutzer wählt die Lenkradfarbe
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Farben für den Lenkrad ( 1 oder 2)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen der Lenkradfarbe basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_lenkrad_farbe('Grau')
    else:
        auto.set_lenkrad_farbe('Schwarz')


# Funktion zur Auswahl der Lenkradheizung
def lenkradheizung():
    print("Wünschen Sie sich eine Lenkradheizung ?")
    print("1 - Ja")  # Option für Lenkradheizung
    print("2 - Nein")  # Option ohne Lenkradheizung

    eingabe = input("Wahl: --> ")  # Benutzer wählt die Lenkradheizung
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen der Lenkradheizung basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_lenkradheizung(True)
    else:
        auto.set_lenkradheizung(False)


# Funktion zur Auswahl der Ambientebeleuchtung
def ambiente():
    print("Wünschen Sie sich eine Ambientebeleuchtung ?")
    print("1 - Ja")  # Option für Ambientebeleuchtung
    print("2 - Nein")  # Option ohne Ambientebeleuchtung

    eingabe = input("Wahl: --> ")  # Benutzer wählt die Ambientebeleuchtung
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen der Ambientebeleuchtung basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_ambientebeleuchtung(True)
    else:
        auto.set_ambientebeleuchtung(False)


# Funktion zur Auswahl der Fußmatten
def fussmatten():
    print("Wünschen Sie sich einen Fußmatten ?")
    print("1 - Ja")  # Option für Fußmatten
    print("2 - Nein")  # Option ohne Fußmatten

    eingabe = input("Wahl: --> ")  # Benutzer wählt die Fußmatten
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen der Fußmatten basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_fussmatten(True)
    else:
        auto.set_fussmatten(False)


# Funktion zur Auswahl der Innenhimmelfarbe
def innenhimmelFarbe():
    print("Wähle einer der folgenden Farben für den Innenhimmel")
    print("1 - Innenhimmel Kristall grau")  # Option für Kristallgrau
    print("2 - Innenhimmel Schwarz")  # Option für Schwarz
    eingabe = input("Wahl: --> ")  # Benutzer wählt die Innenhimmelfarbe
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur die Nummer einer der oben stehenden Farben für den Innenhimmel ( 1 oder 2 )")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen der Innenhimmelfarbe basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_innenhimmel_farbe('Innenhimmel Kristall grau')
    else:
        auto.set_innenhimmel_farbe('Innenhimmel Schwarz')


# Funktion zur Auswahl des Tachos
def tacho():
    print("Wünschen Sie sich einen digitalen Tacho ?")
    print("1 - Ja")  # Option für digitalen Tacho
    print("2 - Nein")  # Option ohne digitalen Tacho

    eingabe = input("Wahl: --> ")  # Benutzer wählt den digitalen Tacho
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen des digitalen Tachos basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_digitalen_tacho(True)
    else:
        auto.set_digitalen_tacho(False)


# Funktion zur Auswahl des Premium-Navigationssystems
def premiumNavigationssystem():
    print("Wünschen Sie sich ein Premium-Navigationssystem ?")
    print("1 - Ja")  # Option für Premium-Navigationssystem
    print("2 - Nein")  # Option ohne Premium-Navigationssystem

    eingabe = input("Wahl: --> ")  # Benutzer wählt das Navigationssystem
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen des Premium-Navigationssystems basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_premium_navigationssystem(True)
    else:
        auto.set_premium_navigationssystem(False)


# Funktion zur Auswahl des Feuerlöschers
def feuerloescher():
    print("Wünschen Sie sich einen Feuerloescher ?")
    print("1 - Ja")  # Option für Feuerlöscher
    print("2 - Nein")  # Option ohne Feuerlöscher

    eingabe = input("Wahl: --> ")  # Benutzer wählt den Feuerlöscher
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen des Feuerlöschers basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_feuerloescher(True)
    else:
        auto.set_feuerloescher(False)


# Funktion zur Auswahl von Keyless-Go
def keyless_go():
    print("Wünschen Sie sich ein Keyless-Go ?")
    print("1 - Ja")  # Option für Keyless-Go
    print("2 - Nein")  # Option ohne Keyless-Go

    eingabe = input("Wahl: --> ")  # Benutzer wählt Keyless-Go
    # Validierung der Eingabe
    while not eingabe.isdigit() or int(eingabe) > 2 or int(eingabe) < 1:
        print("Bitte geben Sie nur 1 (für ja) oder 2 (für nein)")
        eingabe = input()
    eingabe = int(eingabe)

    # Setzen von Keyless-Go basierend auf der Auswahl des Benutzers
    if eingabe == 1:
        auto.set_keyless_go(True)
    else:
        auto.set_keyless_go(False)


# Funktion zum Einlesen der Angebote aus einer CSV-Datei
def einleseAngebote():
    global data
    with open('autos.csv', newline='', encoding='utf-8') as csvfile:  # Öffnet die CSV-Datei zum Lesen
        csvreader = csv.DictReader(csvfile, delimiter=';')  # Erstellt einen CSV-Reader mit ';' als Trennzeichen
        for row in csvreader:  # Durchläuft jede Zeile der CSV-Datei
            #print(row)
            data.append(row)  # Fügt jede Zeile den Daten hinzu
        #print(data)


# Hauptprogramm, das die Angebote einliest und das Menü startet
# Eine Main Methode
if __name__ == "__main__":
    einleseAngebote()  # Liest die vorhandenen Angebote ein
    print(data)
    while True:  # Endlos-Schleife zur Anzeige des Menüs
        startMenue()  # Zeigt das Startmenü an




'''
while [Bedingung]:
    Anweisungen
'''