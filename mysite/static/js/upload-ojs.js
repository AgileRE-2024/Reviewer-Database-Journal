document.addEventListener('DOMContentLoaded', function() {
    const goBtn = document.getElementById('go-btn');

    // Event listener for the Go button
    goBtn.addEventListener('click', function() {
        alert('Starting reviewer scraping process...');
        
        // Send a request to the Django backend
        fetch('/scrape-reviewers/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            alert('Scraping process completed!');
            // You can display or use the received data here
            console.log(data);
        })
        .catch(error => {
            console.error('Error during scraping:', error);
        });
    });
});
