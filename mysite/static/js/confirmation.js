document.addEventListener('DOMContentLoaded', function () {
    const goBackBtn = document.getElementById('goBackBtn');
    const okeBtn = document.getElementById('OkeBtn');

    // Fungsi untuk memuat data pratinjau dari sessionStorage tanpa kategori
    function loadPreviewData() {
        const savedFormData = JSON.parse(sessionStorage.getItem('formData'));
        if (savedFormData) {
            document.getElementById('preview-title').innerText = savedFormData.title || '';
            document.getElementById('preview-publish-date').innerText = savedFormData.publishDate || '';
            document.getElementById('preview-abstract').innerText = savedFormData.abstract || '';
        }
    }

    // Panggil fungsi pratinjau ketika halaman dimuat
    loadPreviewData();

    // Navigasi kembali ke halaman "Upload Detail" ketika tombol "No, Go Back" ditekan
    if (goBackBtn) {
        goBackBtn.addEventListener('click', function () {
            const url = this.getAttribute('data-url');
            window.location.href = url;
        });
    }

    // Navigasi ke halaman "Reviewer" dan hapus data form ketika tombol "Yes, Find My Reviewer" ditekan
    if (okeBtn) {
        okeBtn.addEventListener('click', function () {
            const url = this.getAttribute('data-url');
            window.location.href = url;
            sessionStorage.removeItem('formData'); // Hapus data setelah pengguna melanjutkan ke halaman reviewer
        });
    }
});
