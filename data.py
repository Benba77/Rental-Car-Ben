from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Basisklasse für die Datenbanktabellen
Base = declarative_base()

# Definition der Rental-Tabelle
class Rental(Base):
    __tablename__ = 'rentals'  # Name der Tabelle in der Datenbank
    id = Column(Integer, primary_key=True)  # Primärschlüssel-Spalte
    name = Column(String(80), nullable=False)  # Name des Mieters, darf nicht leer sein
    email = Column(String(120), nullable=False)  # E-Mail des Mieters, darf nicht leer sein
    start_date = Column(Date, nullable=False)  # Startdatum der Miete, darf nicht leer sein
    end_date = Column(Date, nullable=False)  # Enddatum der Miete, darf nicht leer sein
    car_name = Column(String(80), nullable=False)  # Name des gemieteten Autos, darf nicht leer sein

# Definition der Car-Tabelle
class Car(Base):
    __tablename__ = 'cars'  # Name der Tabelle in der Datenbank
    id = Column(Integer, primary_key=True)  # Primärschlüssel-Spalte
    autoname = Column(String(80), nullable=False)  # Name des Autos, darf nicht leer sein
    available = Column(Boolean, nullable=False)  # Verfügbarkeit des Autos, darf nicht leer sein
    wish_date = Column(Date, nullable=True)  # Wunschdatum für die Miete, kann leer sein
    price_per_day = Column(Integer, nullable=False)  # Preis pro Tag, darf nicht leer sein

# Initialisierung der Datenbank
engine = create_engine('sqlite:///mycars.db')  # Erstellt eine SQLite-Datenbank
Base.metadata.create_all(engine)  # Erstellt alle Tabellen in der Datenbank

# Erstellung einer Session
SessionLocal = sessionmaker(bind=engine)  # Erstellt eine Session-Klasse, um Datenbankverbindungen zu verwalten

def get_session():
    return SessionLocal()  # Erstellt und gibt eine neue Session-Instanz zurück

def init_cars():
    session = get_session()  # Erstellt eine neue Session
    existing_cars = session.query(Car).count()  # Zählt die vorhandenen Autos in der Datenbank
    if existing_cars == 0:  # Falls noch keine Autos vorhanden sind, werden neue Autos hinzugefügt
        cars = [
            Car(autoname='Burgermobil', available=True, wish_date=None, price_per_day=500),
            Car(autoname='Audi A4', available=True, wish_date=None, price_per_day=70),
            Car(autoname='BMW 3', available=True, wish_date=None, price_per_day=80),
            Car(autoname='Mercedes C', available=True, wish_date=None, price_per_day=90),
        ]
        session.add_all(cars)  # Fügt die Autos zur Session hinzu
        session.commit()  # Speichert die Änderungen in der Datenbank
    session.close()  # Schließt die Session

def get_Rentals():
    with get_session() as session:  # Erstellt eine neue Session und schließt sie automatisch nach der Verwendung
        result = session.query(Rental).all()  # Holt alle Mietdatensätze aus der Datenbank
    rentals = [
        {
            'id': rental.id,
            'name': rental.name,
            'email': rental.email,
            'start_date': rental.start_date.strftime('%Y-%m-%d'),  # Formatiert das Datum als String
            'end_date': rental.end_date.strftime('%Y-%m-%d'),  # Formatiert das Datum als String
            'car_name': rental.car_name
        }
        for rental in result
    ]
    return rentals  # Gibt die Liste der Mietdatensätze zurück

def get_submit_form(data):
    with get_session() as session:  # Erstellt eine neue Session und schließt sie automatisch nach der Verwendung
        new_rental = Rental(
            name=data['name'],
            email=data['email'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),  # Wandelt den String in ein Datum um
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),  # Wandelt den String in ein Datum um
            car_name=data['car_name']
        )
        session.add(new_rental)  # Fügt den neuen Mietdatensatz zur Session hinzu
        session.commit()  # Speichert die Änderungen in der Datenbank
    return {'message': 'Ihre Buchung war erfolgreich! 🚙'}  # Gibt eine Erfolgsnachricht zurück

def get_cars():
    with get_session() as session:  # Erstellt eine neue Session und schließt sie automatisch nach der Verwendung
        return session.query(Car).all()  # Holt alle Autodatensätze aus der Datenbank

def get_available_cars(start_date, end_date):
    with get_session() as session:  # Erstellt eine neue Session und schließt sie automatisch nach der Verwendung
        rented_cars = session.query(Rental.car_name).filter(
            (Rental.start_date <= end_date) & (Rental.end_date >= start_date)  # Findet alle Autos, die im angegebenen Zeitraum gemietet sind
        ).all()
        rented_car_names = [car_name for (car_name,) in rented_cars]  # Extrahiert die Namen der gemieteten Autos
        available_cars = session.query(Car).filter(~Car.autoname.in_(rented_car_names)).all()  # Findet alle verfügbaren Autos
    return available_cars  # Gibt die Liste der verfügbaren Autos zurück

if __name__ == '__main__':
    init_cars()  # Initialisiert die Datenbank mit Autos, falls noch keine vorhanden sind




	# •	Die Klassen Rental und Car definieren die Tabellenstruktur für Miet- und Autodaten in der Datenbank.
	# •	Die Funktion init_cars fügt einige Autos zur Datenbank hinzu, wenn noch keine vorhanden sind.
	# •	Die Funktionen get_Rentals, get_submit_form, get_cars und get_available_cars ermöglichen das Abrufen und Hinzufügen von Daten zur Datenbank sowie das Überprüfen der Verfügbarkeit von Autos

    