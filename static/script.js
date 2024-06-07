document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('rentalForm'); // Holt das Formular-Element

    form.addEventListener('submit', async function (event) {
        event.preventDefault(); // Verhindert das standardmäßige Absenden des Formulars
        const formData = new FormData(form); // Erstellt ein FormData-Objekt aus dem Formular

        const data = {
            name: formData.get('name'), // Holt den Namen aus dem Formular
            email: formData.get('email'), // Holt die E-Mail aus dem Formular
            start_date: formData.get('start_date'), // Holt das Startdatum aus dem Formular
            end_date: formData.get('end_date'), // Holt das Enddatum aus dem Formular
            car_name: formData.get('car_name') // Holt den Namen des Autos aus dem Formular
        };

        const response = await fetch('/submit-form', {
            method: 'POST', // HTTP-Methode ist POST
            headers: {
                'Content-Type': 'application/json' // Der Inhaltstyp ist JSON
            },
            body: JSON.stringify(data) // Die Daten werden als JSON gesendet
        });
        
        const result = await response.json(); // Holt die Antwort als JSON
        alert(result.message); // Zeigt eine Nachricht an, die aus der Antwort kommt
    });
});

async function updateAvailableCars() {
    const startDate = document.getElementById('start_date').value; // Holt das Startdatum
    const endDate = document.getElementById('end_date').value; // Holt das Enddatum
    const carSelect = document.getElementById('car_name'); // Holt das Dropdown-Menü für die Autos

    if (new Date(startDate) < new Date().setHours(0, 0, 0, 0) || new Date(endDate) < new Date().setHours(0, 0, 0, 0)) {
        alert('Datum in der Vergangenheit ist nicht erlaubt.'); // Warnung, wenn das Datum in der Vergangenheit liegt
        carSelect.innerHTML = '<option value="-">-</option>'; // Setzt das Dropdown-Menü zurück
        return; // Beendet die Funktion
    }

    if (new Date(startDate) > new Date(endDate)) {
        alert('Startdatum muss vor dem Enddatum liegen.'); // Warnung, wenn das Startdatum nach dem Enddatum liegt
        carSelect.innerHTML = '<option value="-">-</option>'; // Setzt das Dropdown-Menü zurück
        return; // Beendet die Funktion
    }

    const response = await fetch(`/api/available-cars?start_date=${startDate}&end_date=${endDate}`); // Holt die verfügbaren Autos vom Server
    const availableCars = await response.json(); // Holt die Antwort als JSON
    carSelect.innerHTML = '<option value="-">-</option>'; // Setzt das Dropdown-Menü zurück
    availableCars.forEach(car => {
        const option = document.createElement('option'); // Erstellt ein neues Option-Element
        option.value = car; // Setzt den Wert des Option-Elements
        option.textContent = car; // Setzt den Text des Option-Elements
        carSelect.appendChild(option); // Fügt das Option-Element zum Dropdown-Menü hinzu
    });
}

function sendCarName() {
    const carName = document.getElementById('car_name').value; // Holt den ausgewählten Autonamen
    alert(`Selected car model: ${carName}`); // Zeigt eine Nachricht mit dem ausgewählten Autonamen an
}

// •	document.addEventListener('DOMContentLoaded', function () {...}): Wartet, bis das DOM vollständig geladen ist, bevor der Code ausgeführt wird.
// •	form.addEventListener('submit', async function (event) {...}): Fügt einen Event-Listener für das Absenden des Formulars hinzu und verhindert das Standardverhalten, um eigene Logik auszuführen.
// •	const formData = new FormData(form): Erstellt ein FormData-Objekt, um die Formulardaten zu sammeln.
// •	const data = {...}: Erstellt ein Objekt mit den Formulardaten.
// •	const response = await fetch(...): Sendet die Formulardaten asynchron an den Server und wartet auf die Antwort.
// •	const result = await response.json(): Holt die Antwort vom Server und konvertiert sie in ein JSON-Objekt.
// •	alert(result.message): Zeigt die Nachricht aus der Serverantwort an.
// •	async function updateAvailableCars() {...}: Aktualisiert die verfügbaren Autos im Dropdown-Menü basierend auf den ausgewählten Start- und Enddaten.
// •	function sendCarName() {...}: Zeigt eine Nachricht mit dem ausgewählten Autonamen an.