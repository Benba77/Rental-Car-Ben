from flask import Flask, request, jsonify, render_template
from data import get_Rentals, get_submit_form

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    all_rental_data = get_Rentals()
    return render_template('admin.html', all_rentals=all_rental_data)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()
    result = get_submit_form(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
