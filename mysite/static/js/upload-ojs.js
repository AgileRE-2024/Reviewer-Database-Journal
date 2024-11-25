document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('upload-form');
    const goBtn = document.getElementById('go-btn');
    const stopBtn = document.getElementById('stop-btn');
    const stats = document.getElementById('scraping-stats');
    let scrapingInProgress = false;

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
            } else {
                alert('File upload failed!');
            }
        })
        .catch(error => {
            console.error('Error during file upload:', error);
        });
    });

    goBtn.addEventListener('click', function() {
        if (!scrapingInProgress) {
            alert('Scraping started!');
            scrapingInProgress = true;
            stopBtn.disabled = false;

            fetch('/scrape-reviewers/', { method: 'GET' })
                .then(response => response.json())
                .then(data => {
                    alert('Scraping completed or stopped!');
                    stats.textContent = `Added Reviewers: ${data.added_reviewers}, Added Papers: ${data.added_papers}`;
                })
                .catch(error => console.error('Error during scraping:', error))
                .finally(() => {
                    scrapingInProgress = false;
                    stopBtn.disabled = true;
                });
        }
    });

    stopBtn.addEventListener('click', function() {
        if (scrapingInProgress) {
            fetch('/stop-scraping/', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    alert('Scraping stopped!');
                    stats.textContent = `Added Reviewers: ${data.added_reviewers}, Added Papers: ${data.added_papers}`;
                })
                .catch(error => console.error('Error stopping scraping:', error))
                .finally(() => {
                    scrapingInProgress = false;
                    stopBtn.disabled = true;
                });
        }
    });
});
