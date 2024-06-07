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

# Erklärung

1) Logik für die Kartendarstellung:

Standorte:
<h2> Unser Standort auf der Streetmap! </h2>
        <iframe width="600" height="450" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
            src="https://www.openstreetmap.org/export/embed.html?bbox=10.51087686252092%2C52.24981701179856%2C10.53087686252092%2C52.26981701179856&amp;layer=mapnik&amp;marker=52.25981701179856%2C10.52087686252092"
            style="border: 1px solid black"></iframe>
        <br>
        <small><a href="https://www.openstreetmap.org/?mlat=52.25981701179856&mlon=10.52087686252092#map=16/52.2598/10.5209">Größere Karte anzeigen</a></small>

* Marker-Parameter: Die Koordinaten 52.25981701179856 (Breitengrad) und 10.52087686252092 (Längengrad) platzieren den Marker an einer spezifischen Stelle (Braunschweig). 
* %2C: Repräsentiert ein Komma in der URL.
* Bounding Box (bbox): Definiert die Sichtgrenzen der Karte, um den Standort sichtbar zu machen.


2) Logik Formular Daten:


3) Logik Verfügbare Autos:

def get_available_cars(start_date, end_date):
    with get_session() as session:
        rented_cars = session.query(Rental.car_name).filter(
            (Rental.start_date <= end_date) & (Rental.end_date >= start_date)
        ).all()
        rented_car_names = [car_name for (car_name,) in rented_cars]
        available_cars = session.query(Car).filter(~Car.autoname.in_(rented_car_names)).all()
    return available_cars
