from sqlalchemy import create_engine, Column, Integer, String, Date
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
    date = Column(Date, nullable=False)
    car_name = Column(String(80), nullable=False)

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Datum: {self.date}, Automodell: {self.car_name} '

    def __repr__(self):
        return str(self)

class Autos(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    autoname = Column(String)

    def __str__(self):
        return f'Auto'

engine = create_engine('sqlite:///rentals.db')
Base.metadata.create_all(engine)

def get_Rentals():
    with sessionmaker(bind=engine)() as session:
        result = session.query(Rental).all()
    tabelle= '\n<br>'.join(map(str,result))
    return tabelle
    
def get_submit_form(data):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_rental = Rental(
            name=data['name'],
            email=data['email'],
            date=datetime.strptime(data['date'], '%Y-%m-%d'),
            car_name=data['car_name']
        )
        session.add(new_rental)
        session.commit()
    return {'message': 'Form submitted successfully!'}

if __name__== '__main__':
    pass