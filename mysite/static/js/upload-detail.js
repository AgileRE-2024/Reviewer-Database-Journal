document.addEventListener('DOMContentLoaded', function () {
    const manuscriptForm = document.getElementById('manuscriptForm');
  
    // Save form data to sessionStorage
    function saveFormData() {
        const formData = {
            title: document.getElementById('journal-title').value,
            abstract: document.getElementById('abstract').value,
            terms: document.getElementById('terms').checked
        };
        sessionStorage.setItem('formData', JSON.stringify(formData));
    }
  
    // Load form data from sessionStorage
    function loadFormData() {
        const savedFormData = JSON.parse(sessionStorage.getItem('formData'));
        if (savedFormData) {
            document.getElementById('journal-title').value = savedFormData.title || '';
            document.getElementById('abstract').value = savedFormData.abstract || '';
            document.getElementById('terms').checked = savedFormData.terms || false;
        }
    }
  
    // Load data on page load
    if (manuscriptForm) {
        loadFormData();
  
        // Save data when input changes
        manuscriptForm.addEventListener('input', saveFormData);
  
        manuscriptForm.addEventListener('submit', function (event) {
            event.preventDefault();
            saveFormData(); // Ensure last data is saved
            window.location.href = '/confirmation/';
        });
    }
});