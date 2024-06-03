from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from data import *

app = Flask(__name__)

Base = declarative_base()

class Rental(Base):
    __tablename__ = 'rentals'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False)
    date = Column(Date, nullable=False)
    car_name = Column(String(80), nullable=False)

# Create an engine and a session
engine = create_engine('sqlite:///rentals.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()
    session = Session()
    new_rental = Rental(
        name=data['name'],
        email=data['email'],
        date=datetime.strptime(data['date'], '%Y-%m-%d'),
        car_name=data['fahrzeugmodell']
    )
    session.add(new_rental)
    session.commit()
    session.close()
    return jsonify({'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)