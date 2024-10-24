document.addEventListener('DOMContentLoaded', function () {
    const goBackBtn = document.getElementById('goBackBtn');
    const okeBtn = document.getElementById('OkeBtn');
  
    // Menavigasi kembali ke halaman "Upload Detail" ketika tombol "No, Go Back" ditekan
    if (goBackBtn) {
        goBackBtn.addEventListener('click', function () {
            const url = this.getAttribute('data-url');
            window.location.href = url;
        });
    }
  
    // Menavigasi ke halaman "Reviewer" dan hapus data form ketika tombol "Yes, Find My Reviewer" ditekan
    if (okeBtn) {
        okeBtn.addEventListener('click', function () {
            const url = this.getAttribute('data-url');
            window.location.href = url;
            sessionStorage.removeItem('formData'); // Hapus data setelah pengguna melanjutkan ke halaman reviewer
        });
    }
  });
  