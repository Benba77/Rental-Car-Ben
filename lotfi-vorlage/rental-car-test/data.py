from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

def init_db():
    engine = create_engine('sqlite:///cars.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

Session = init_db()