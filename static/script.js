document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('rentalForm');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        const formData = new FormData(form);

        const data = {
            name: formData.get('name'),
            email: formData.get('email'),
            start_date: formData.get('start_date'),
            end_date: formData.get('end_date'),
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

async function updateAvailableCars() {
    const startDate = document.getElementById('start_date').value;
    const endDate = document.getElementById('end_date').value;
    const carSelect = document.getElementById('car_name');

    if (new Date(startDate) < new Date().setHours(0, 0, 0, 0) || new Date(endDate) < new Date().setHours(0, 0, 0, 0)) {
        alert('Datum in der Vergangenheit ist nicht erlaubt.');
        carSelect.innerHTML = '<option value="-">-</option>';
        return;
    }

    if (new Date(startDate) > new Date(endDate)) {
        alert('Startdatum muss vor dem Enddatum liegen.');
        carSelect.innerHTML = '<option value="-">-</option>';
        return;
    }

    const response = await fetch(`/api/available-cars?start_date=${startDate}&end_date=${endDate}`);
    const availableCars = await response.json();
    carSelect.innerHTML = '<option value="-">-</option>';
    availableCars.forEach(car => {
        const option = document.createElement('option');
        option.value = car;
        option.textContent = car;
        carSelect.appendChild(option);
    });
}

function sendCarName() {
    const carName = document.getElementById('car_name').value;
    alert(`Selected car model: ${carName}`);
}