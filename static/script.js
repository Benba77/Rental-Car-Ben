document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('rentalForm');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        const formData = new FormData(form);

        const data = {
            name: formData.get('name'),
            email: formData.get('email'),
            date: formData.get('date'),
            car_name: formData.get('car_name')
        };

        try {
            const response = await fetch('/submit-form', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            alert(result.message);
        } catch (error) {
            console.error('Error:', error);
        }
    });
});

function sendCarName() {
    const carName = document.getElementById('car_name').value;
    alert(`Selected car model: ${carName}`);
}
