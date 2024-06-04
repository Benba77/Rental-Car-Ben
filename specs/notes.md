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
* Sql Alchemy checken
    * 2xDatenbank: 
        * 1 für Namen, Email, Wunschtermin, Fahrzeugmodell(ForeignKey)
        * 1 für Automodell, frei/besetzt, Wunschtermin(ForeignKey) (optional: Preis)
    * Test-Aufruf von AutoModell Datenbank -> Anzeigen auf HTML Seite mithilfe von Flask
* HTML Formular eingeben -> Speichern in Datenbank 
    * Testbutton zum Anzeigen von allen Benutzern & deren Modelle & Buchungen
* Drop Down Menü Automodelle: Verbunden mit Datenbank (Nur freiwählbare Autos werden angezeigt, je nachdem welcher Tag gewählt)
