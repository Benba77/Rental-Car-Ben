function sendCarName() {
    const form = document.getElementById('rentalForm');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    fetch('/submit-form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response => {
        if (response.ok) {
            alert('Form submitted successfully!');
        } else {
            alert('Error submitting form.');
        }
    });
}