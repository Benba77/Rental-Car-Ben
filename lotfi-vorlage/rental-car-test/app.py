from flask import Flask, request, jsonify, render_template
from data import * 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_car', methods=['POST'])
def add_car():
    data = request.get_json()
    session = Session()
    new_car = Car(name=data['name'])
    session.add(new_car)
    session.commit()
    session.close()
    return jsonify({'message': 'Car name saved!'})

if __name__ == '__main__':
    app.run(debug=True)