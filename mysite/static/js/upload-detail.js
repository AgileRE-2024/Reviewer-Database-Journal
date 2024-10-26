document.addEventListener('DOMContentLoaded', function () {
    const manuscriptForm = document.getElementById('manuscriptForm');
  
    // Fungsi untuk menyimpan data form ke sessionStorage tanpa kategori
    function saveFormData() {
        const formData = {
            title: document.getElementById('journal-title').value,
            publishDate: document.getElementById('publish-date').value,
            abstract: document.getElementById('abstract').value,
            terms: document.getElementById('terms').checked
        };
        sessionStorage.setItem('formData', JSON.stringify(formData));
    }
  
    // Fungsi untuk memuat data form dari sessionStorage tanpa kategori
    function loadFormData() {
        const savedFormData = JSON.parse(sessionStorage.getItem('formData'));
        if (savedFormData) {
            document.getElementById('journal-title').value = savedFormData.title || '';
            document.getElementById('publish-date').value = savedFormData.publishDate || '';
            document.getElementById('abstract').value = savedFormData.abstract || '';
            document.getElementById('terms').checked = savedFormData.terms || false;
        }
    }
  
    // Memuat data form saat halaman "Upload Detail" dimuat
    if (manuscriptForm) {
        loadFormData();
  
        // Menyimpan data setiap kali input berubah
        manuscriptForm.addEventListener('input', saveFormData);
  
        manuscriptForm.addEventListener('submit', function (event) {
            event.preventDefault();
            saveFormData(); // Pastikan data terakhir tersimpan
            window.location.href = '/confirmation/'; // Ganti dengan URL halaman konfirmasi Anda
        });
    }
  });
  