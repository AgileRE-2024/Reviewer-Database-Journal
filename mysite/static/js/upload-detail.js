document.addEventListener('DOMContentLoaded', function () {
    const manuscriptForm = document.getElementById('manuscriptForm');

    manuscriptForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Mencegah reload halaman

        // Lakukan panggilan ke endpoint yang mengolah dan mencocokkan data
        fetch('/recommend-reviewers/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                title: document.getElementById('journal-title').value,
                abstract: document.getElementById('abstract').value
            })
        })
        .then(response => response.json())
        .then(data => {
            // Simpan data rekomendasi di Session Storage
            sessionStorage.setItem('recommendations', JSON.stringify(data));
            // Redirect ke halaman baru
            window.location.href = '/recommendation/';
        })
        .catch(error => console.error('Error:', error));
    });
});
