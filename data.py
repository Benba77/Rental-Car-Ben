from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Basisklasse für die Datenbanktabellen
Base = declarative_base()

# Definition der Rental-Tabelle
class Rental(Base):
    __tablename__ = 'rentals'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    car_name = Column(String(80), nullable=False)

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Zeitraum: {self.start_date} bis {self.end_date}, Automodell: {self.car_name}'

    def __repr__(self):
        return str(self)

# Definition der Car-Tabelle
class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    autoname = Column(String(80), nullable=False)
    available = Column(Boolean, nullable=False)
    wish_date = Column(Date, nullable=True)
    price_per_day = Column(Integer, nullable=False)

    def __str__(self):
        return f'Autoname: {self.autoname}, Frei: {"Ja" if self.available else "Nein"}, Wunschtermin: {self.wish_date}, Preis: {self.price_per_day}'

    def __repr__(self):
        return str(self)

# Initialisierung der Datenbank
engine = create_engine('sqlite:///mycars.db')
Base.metadata.create_all(engine)

# Erstellung einer Session
SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()

def init_cars():
    session = get_session()
    existing_cars = session.query(Car).count()
    if existing_cars == 0:
        cars = [
            Car(autoname='Golf 4', available=True, wish_date=None, price_per_day=50),
            Car(autoname='Golf 5', available=True, wish_date=None, price_per_day=60),
            Car(autoname='BMW 3', available=True, wish_date=None, price_per_day=80),
            Car(autoname='Audi A4', available=True, wish_date=None, price_per_day=70),
            Car(autoname='Mercedes C', available=True, wish_date=None, price_per_day=90),
        ]
        session.add_all(cars)
        session.commit()
    session.close()

def get_Rentals():
    with get_session() as session:
        result = session.query(Rental).all()
    rentals = [
        {
            'id': rental.id,
            'name': rental.name,
            'email': rental.email,
            'start_date': rental.start_date.strftime('%Y-%m-%d'),
            'end_date': rental.end_date.strftime('%Y-%m-%d'),
            'car_name': rental.car_name
        }
        for rental in result
    ]
    return rentals

def get_submit_form(data):
    with get_session() as session:
        new_rental = Rental(
            name=data['name'],
            email=data['email'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            car_name=data['car_name']
        )
        session.add(new_rental)
        session.commit()
    return {'message': 'Form submitted successfully!'}

def get_cars():
    with get_session() as session:
        return session.query(Car).all()

def get_available_cars(start_date, end_date):
    with get_session() as session:
        rented_cars = session.query(Rental.car_name).filter(
            (Rental.start_date <= end_date) & (Rental.end_date >= start_date)
        ).all()
        rented_car_names = [car_name for (car_name,) in rented_cars]
        available_cars = session.query(Car).filter(~Car.autoname.in_(rented_car_names)).all()
    return available_cars

if __name__ == '__main__':
    init_cars()