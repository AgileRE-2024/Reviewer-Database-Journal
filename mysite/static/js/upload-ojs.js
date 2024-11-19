document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('upload-form');
    const goBtn = document.getElementById('go-btn');
    let fileUploaded = false;

    uploadForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(uploadForm);

        fetch('/upload-ojs-file/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('File uploaded successfully!');
                goBtn.disabled = false;
                fileUploaded = true;
            } else {
                alert('File upload failed!');
            }
        })
        .catch(error => {
            console.error('Error during file upload:', error);
        });
    });

    goBtn.addEventListener('click', function() {
        if (fileUploaded) {
            alert('Starting reviewer scraping process...');

            fetch('/scrape-reviewers/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);  // Menampilkan pesan kesalahan jika ada masalah dengan kolom
                } else {
                    alert('Scraping process completed!');
                    console.log(data);
                }
            })
            .catch(error => {
                console.error('Error during scraping:', error);
            });
        } else {
            alert('Please upload a file first.');
        }
    });
});
