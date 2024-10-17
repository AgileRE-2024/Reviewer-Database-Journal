document.addEventListener('DOMContentLoaded', function () {
  const manuscriptForm = document.getElementById('manuscriptForm');

  manuscriptForm.addEventListener('submit', function (event) {
      event.preventDefault(); // Mencegah form dari pengiriman default

      // Logika untuk memproses data form (jika diperlukan) bisa ditambahkan di sini

      // Mengarahkan ke halaman konfirmasi
      window.location.href = '/confirmation/'; // Ganti dengan URL halaman konfirmasi Anda
  });
});
