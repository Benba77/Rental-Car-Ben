from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

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

engine = create_engine('sqlite:///rentals.db')
Base.metadata.create_all(engine)

