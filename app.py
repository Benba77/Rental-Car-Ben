from flask import Flask, request, jsonify, render_template
from data import get_Rentals, get_submit_form, get_cars, get_available_cars, init_cars
from datetime import datetime

init_cars()  # Initialisiert die Datenbank mit Autos, falls noch keine vorhanden sind

app = Flask(__name__)  # Erstellt eine neue Flask-Anwendung

@app.route('/')
def index():
    cars = get_cars()  # Holt alle Autos aus der Datenbank
    return render_template('index.html', cars=cars)  # Rendert die index.html und übergibt die Autos

@app.route('/admin')
def admin():
    all_rental_data = get_Rentals()  # Holt alle Mietdaten aus der Datenbank
    return render_template('admin.html', all_rentals=all_rental_data)  # Rendert die admin.html und übergibt die Mietdaten

@app.route('/api/available-cars')
def available_cars():
    start_date = request.args.get('start_date')  # Holt das Startdatum aus den URL-Parametern
    end_date = request.args.get('end_date')  # Holt das Enddatum aus den URL-Parametern
    available_cars = get_available_cars(start_date, end_date)  # Holt die verfügbaren Autos für den Zeitraum
    return jsonify([car.autoname for car in available_cars])  # Gibt die verfügbaren Autos als JSON zurück

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()  # Holt die JSON-Daten aus der POST-Anfrage
    result = get_submit_form(data)  # Verarbeitet die Formulardaten und fügt sie zur Datenbank hinzu
    return jsonify(result)  # Gibt das Ergebnis als JSON zurück

if __name__ == '__main__':
    app.run(debug=True)  # Startet die Flask-Anwendung im Debug-Modus


	# 1.	init_cars(): Diese Funktion wird aufgerufen, um die Datenbank mit Autos zu initialisieren, falls noch keine vorhanden sind.
	# 2.	app = Flask(__name__): Erstellt eine neue Flask-Anwendung.
	# 3.	@app.route('/'): Definiert die Route für die Startseite. Diese Funktion rendert die index.html-Vorlage und übergibt eine Liste von Autos an die Vorlage.
	# 4.	@app.route('/admin'): Definiert die Route für die Admin-Seite. Diese Funktion rendert die admin.html-Vorlage und übergibt eine Liste aller Mietdaten an die Vorlage.
	# 5.	@app.route('/api/available-cars'): Definiert die Route für die API, die die verfügbaren Autos für einen bestimmten Zeitraum zurückgibt. Diese Funktion holt das Start- und Enddatum aus den URL-Parametern und gibt die verfügbaren Autos als JSON zurück.
	# 6.	@app.route('/submit-form', methods=['POST']): Definiert die Route für das Absenden des Formulars. Diese Funktion holt die JSON-Daten aus der POST-Anfrage, verarbeitet sie und fügt sie zur Datenbank hinzu, und gibt das Ergebnis als JSON zurück.
	# 7.	if __name__ == '__main__':: Wenn das Skript direkt ausgeführt wird, startet es die Flask-Anwendung im Debug-Modus.