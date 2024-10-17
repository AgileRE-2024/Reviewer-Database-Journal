document.addEventListener('DOMContentLoaded', function () {
  const loginForm = document.getElementById('loginForm');

  loginForm.addEventListener('submit', function (event) {
      event.preventDefault(); // Mencegah form dari pengiriman default

      // Anda dapat menambahkan logika autentikasi di sini jika diperlukan
      // Untuk saat ini, kita langsung mengarahkan ke dashboard

      window.location.href = '/dashboard/'; // Ganti dengan URL dashboard Anda
  });
});
