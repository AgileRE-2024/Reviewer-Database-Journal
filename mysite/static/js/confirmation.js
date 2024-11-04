document.addEventListener('DOMContentLoaded', function () {
    const goBackBtn = document.getElementById('goBackBtn');
    const okeBtn = document.getElementById('OkeBtn');

    // Load preview data from sessionStorage
    function loadPreviewData() {
        const savedFormData = sessionStorage.getItem('formData');
        if (savedFormData) {
            const parsedData = JSON.parse(savedFormData);
            document.getElementById('preview-title').innerText = parsedData.title || '';
            document.getElementById('preview-abstract').innerText = parsedData.abstract || '';
        }
    }

    // "Go Back" button - navigate back to the upload page
    goBackBtn.addEventListener('click', function () {
        const url = goBackBtn.getAttribute('data-url');
        window.location.href = url;
    });

    // "Yes, Find My Reviewer" button - navigate to the reviewer page
    okeBtn.addEventListener('click', function () {
        const url = okeBtn.getAttribute('data-url');
        sessionStorage.removeItem('formData'); // Clear data when navigating forward
        window.location.href = url;
    });

    // Load data on page load
    loadPreviewData();
});