function sendCarName() {
    const carName = document.getElementById('car_name').value;

    fetch('/add_car', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: carName })
    }).then(response => {
        if (response.ok) {
            alert('Car name saved!');
        } else {
            alert('Error saving car name.');
        }
    });
}