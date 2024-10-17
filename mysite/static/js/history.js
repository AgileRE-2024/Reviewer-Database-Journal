document.addEventListener("DOMContentLoaded", function () {
    // Fungsionalitas kalender
    let currentDate = new Date();
    let currentMonth = currentDate.getMonth();
    let currentYear = currentDate.getFullYear();

    function populateCalendar(month, year) {
        const calendarDays = document.getElementById('calendarDays');
        const currentMonthElement = document.getElementById('currentMonth');

        currentMonthElement.textContent = `${currentDate.toLocaleString('default', { month: 'long' })} ${year}`;
        calendarDays.innerHTML = ''; // Kosongkan isi sebelumnya

        const firstDay = new Date(year, month, 1).getDay();
        const lastDate = new Date(year, month + 1, 0).getDate();

        // Tambahkan hari kosong untuk menggeser tanggal ke kanan
        for (let i = 0; i < firstDay; i++) {
            const emptyCell = document.createElement('div');
            calendarDays.appendChild(emptyCell);
        }

        // Tambahkan tanggal
        for (let date = 1; date <= lastDate; date++) {
            const dayCell = document.createElement('div');
            dayCell.textContent = date;
            dayCell.addEventListener('click', function() {
                document.querySelector('.date-input').value = `${date} ${currentDate.toLocaleString('default', { month: 'long' })} ${year}`;
                document.querySelector('.calendar').style.display = 'none'; // Menyembunyikan kalender setelah memilih tanggal
            });
            calendarDays.appendChild(dayCell);
        }
    }

    populateCalendar(currentMonth, currentYear);

    document.getElementById('prevMonth').addEventListener('click', function() {
        currentMonth--;
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear--;
        }
        populateCalendar(currentMonth, currentYear);
    });

    document.getElementById('nextMonth').addEventListener('click', function() {
        currentMonth++;
        if (currentMonth > 11) {
            currentMonth = 0;
            currentYear++;
        }
        populateCalendar(currentMonth, currentYear);
    });

    document.querySelector('.date-input').addEventListener('click', function() {
        const calendar = document.querySelector('.calendar');
        calendar.style.display = calendar.style.display === 'none' ? 'block' : 'none';
    });

    // Fungsionalitas status
    const statusElements = document.querySelectorAll(".status");

    statusElements.forEach(status => {
        status.addEventListener("click", function () {
            const currentStatus = this.textContent.trim();
            // Hanya mengizinkan dua pilihan: "Completed" atau "Processing"
            const newStatus = currentStatus === "Completed" ? "Processing" : "Completed";

            this.textContent = newStatus;
            // Update class berdasarkan status baru
            this.className = "status " + (newStatus.toLowerCase() === "completed" ? "completed" : "processing");
        });
    });

    // Fungsionalitas filter status
    document.getElementById("statusFilter").addEventListener("change", function() {
        const selectedStatus = this.value;
        const rows = document.querySelectorAll("tbody tr"); // Ganti dengan selector yang sesuai untuk tabel Anda

        rows.forEach(row => {
            const statusCell = row.querySelector(".status");
            const statusText = statusCell.textContent.trim();

            // Tampilkan atau sembunyikan baris berdasarkan status yang dipilih
            if (selectedStatus === "" || statusText === selectedStatus) {
                row.style.display = ""; // Tampilkan baris
            } else {
                row.style.display = "none"; // Sembunyikan baris
            }
        });
    });
});
