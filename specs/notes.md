Rental Car: 
* Die zur Verfügung stehenden Fahrzeuge, deren Spezifikationen und Buchungen, sollen in
einer Datenbank hinterlegt werden.( z.B.)
* Folgende Features sollen in ihrer Webapp umgesetzt sein:
    ● Buchung eines freien Fahrzeugs auf der Website.   
* Kalender mit Bootsstrap KW22
* Features:
    * Kalender eintragen
    * Administration (Aufruf Verfügbarkeit v. Fahrzeugen)
    * (Rabattcodes)
    * (Rechnung erstellen CSV als Zusammenfassung)
    * (Landkarte)
    * (Email)

Tipps:
* https://bitbucket.org/qualidy/python_f73/src/main/Python02/KW23_Jun03-07_Projektwoche_Autobuchung/README.md

# To-Do Liste
* Mitwoch: Ziel fertig werden

1) 2xDatenbank bauen: 
    * 1 für Namen, Email, Wunschtermin, Fahrzeugmodell(ForeignKey)
    * 1 für Autonamen, frei/besetzt, Wunschtermin(ForeignKey?) (optional: Preis)
        (* Test-Aufruf von AutoModell Datenbank -> Anzeigen auf HTML Seite mithilfe von Flask render)

2) Drop Down Menü Automodelle: Verbunden mit Datenbank 
    2.1) Nur freiwählbare Autos werden angezeigt, je nachdem welcher Tag gewählt

3) Bei Buchung im Kalender freies Datum/gebuchte Termine anzeigen 

4) Administrationsseite, in der die Buchungen bzw. Verfügbarkeiten der Fahrzeuge
eingesehen werden können.

5) Fertig!

* Donnerstag: Alles verstehen

* Freitag: Kleine Veränderungen(Hauptdatei unberührt) -> Präsentieren
