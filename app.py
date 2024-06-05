from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    all_rental_data= data.get_Rentals()
    return render_template('admin.html', all_rentals=all_rental_data)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()
    with sessionmaker(bind=engine)() as session:
        new_rental = Rental(
            name=data['name'],
            email=data['email'],
            date=datetime.strptime(data['date'], '%Y-%m-%d'),
            car_name=data['fahrzeugmodell']
        )
        session.add(new_rental)
        session.commit()
    return jsonify({'message': 'Form submitted successfully!'})


if __name__ == '__main__':
    app.run(debug=True)

