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
* Donnerstag: Ziel fertig werden & verstehen
* Freitag: Schöner machen, Notes bearbeiten & Azure Deployen mit David`s Hilfe

1) 2xDatenbank bauen: 
    * 1 für Namen, Email, Wunschtermin, Fahrzeugmodell(ForeignKey)
    * 1 für Autonamen, frei/besetzt, Wunschtermin(ForeignKey?) (optional: Preis)
        (* Test-Aufruf von AutoModell Datenbank -> Anzeigen auf HTML Seite mithilfe von Flask render)

2) Drop Down Menü Automodelle: Verbunden mit Datenbank 
    2.1) Nur freiwählbare Autos werden angezeigt, je nachdem welcher Tag gewählt

3) Bei Buchung im Kalender freies Datum/gebuchte Termine anzeigen 

4) Nicht gleiches Datum auswählen können bei gleichem Automodell

5) Fertig!

Unbedingt Verstehen!:
1) Drop down Menü:
 <select class="form-control" id="car_name" name="car_name">
                <option value="-">-</option>
                {% for car in cars %}
                <option value="{{ car.autoname }}">{{ car.autoname }} - {{ car.price_per_day }} €/Tag</option>
                {% endfor %}
            </select>

2) data.py
class Rental(Base):
    __tablename__ = 'rentals'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False)
    date = Column(Date, nullable=False)
    car_name = Column(String(80), nullable=False)

Erklärung: 
name = Column(String(80), nullable=False)
name: Eine String-Spalte mit einer maximalen Länge von 80 Zeichen. nullable=False bedeutet, dass dieser Wert nicht null sein darf, d.h., es muss immer ein Wert vorhanden sein.

3)
Schritt 1: Erweiterung der Car-Tabelle um Standortinformationen
Füge die Felder latitude und longitude zur Car-Tabelle hinzu:

4)
Schritt 2: Anpassung der HTML- und JavaScript-Dateien
In der index.html-Datei fügst du ein div-Element für die Karte hinzu und passt das Dropdown-Menü an:

In der script.js-Datei fügst du die Logik für die Kartendarstellung hinzu:

Standorte:
* Wolfsburg
    * Lat: 52.4227° N
    * Lon: 10.7865° E

* Braunschweig
    * Lat: 52° 15' 57.38" N
    * Lon: 10° 31' 36.23" E

* Salzgitter:
    * Lat: 52.4227° N
    * Lon: 10.7865° E