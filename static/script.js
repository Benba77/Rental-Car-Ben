async function sendCarName() {
    // Holt das Formular-Element
    const form = document.getElementById('rentalForm');
    
    // Holt alle Daten aus dem Formular
    const formData = new FormData(form);
    
    // Wandelt die Formulardaten in ein JSON-Objekt um
    const data = Object.fromEntries(formData.entries());

    // Senden der Daten an den Server
    const response = await fetch('/submit-form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data) // Konvertiert das Daten-Objekt in einen JSON-String
    });

    // Überprüft, ob die Anfrage erfolgreich war
    if (response.ok) {
        alert('Form submitted successfully!'); // Erfolgreiche Rückmeldung
    } else {
        alert('Error submitting form.'); // Fehler-Rückmeldung
    }
}