const reviewers = [
  {
    name: "Christine Brooks",
    category: "Technology",
    papers: 63,
    institution: "Tech Institute of Innovation",
    researchPapers: [
      { title: "Knowledge Management Systems for Organizational Innovation: A Case Study of Leading Tech Companies", score: 88 },
      { title: "Enhancing Data Privacy in Cloud Computing: A Comparative Analysis of Encryption Techniques", score: 82 },
      { title: "Cybersecurity Threats and Countermeasures in the Age of IoT: A Comprehensive Review", score: 75 },
      { title: "Blockchain Technology Adoption in Supply Chain Management: Challenges and Opportunities", score: 71 },
      { title: "Machine Learning Applications in Predictive Analytics for Healthcare Management", score: 67 },
    ]
  },
  {
    name: "Dimas Respati",
    category: "Health",
    papers: 100,
    institution: "Tech Institute of Innovation",
    researchPapers: [
      { title: "Knowledge Management Systems for Organizational Innovation: A Case Study of Leading Tech Companies", score: 88 },
      { title: "Enhancing Data Privacy in Cloud Computing: A Comparative Analysis of Encryption Techniques", score: 82 },
      { title: "Cybersecurity Threats and Countermeasures in the Age of IoT: A Comprehensive Review", score: 75 },
      { title: "Blockchain Technology Adoption in Supply Chain Management: Challenges and Opportunities", score: 71 },
      { title: "Machine Learning Applications in Predictive Analytics for Healthcare Management", score: 67 },
    ]
  },
  {
    name: "Memoreza Sabana",
    category: "Health",
    papers: 30,
    institution: "Tech Institute of Innovation",
    researchPapers: [
      { title: "Knowledge Management Systems for Organizational Innovation: A Case Study of Leading Tech Companies", score: 88 },
      { title: "Enhancing Data Privacy in Cloud Computing: A Comparative Analysis of Encryption Techniques", score: 82 },
      { title: "Cybersecurity Threats and Countermeasures in the Age of IoT: A Comprehensive Review", score: 75 },
      { title: "Blockchain Technology Adoption in Supply Chain Management: Challenges and Opportunities", score: 71 },
      { title: "Machine Learning Applications in Predictive Analytics for Healthcare Management", score: 67 },
    ]
  },
];

function populateReviewersTable() {
  const tableBody = document.getElementById('reviewersTableBody');
  tableBody.innerHTML = '';

  reviewers.forEach((reviewer, index) => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${reviewer.name}</td>
      <td>${reviewer.category}</td>
      <td>${reviewer.papers}</td>
      <td>
        <i class="fas fa-file-alt" title="Data Analytics"></i>
        <i class="fas fa-shield-alt" title="Information Security"></i>
        <i class="fas fa-link" title="Blockchain Technology"></i>
      </td>
      <td>
        <button class="btn btn-primary" onclick="confirmChoose(${index})">Choose</button>
        <button class="btn btn-secondary" onclick="showReviewerDetails(${index})">Detail</button>
      </td>
    `;
    tableBody.appendChild(row);
  });
}

function showReviewerDetails(index) {
  const reviewer = reviewers[index];
  const popupOverlay = document.getElementById('popupOverlay');
  const reviewerCard = document.getElementById('reviewerCard');

  reviewerCard.innerHTML = `
    <div class="reviewer-header">
      <div class="reviewer-info">
        <h2>${reviewer.name}</h2>
        <p>${reviewer.institution}</p>
      </div>
      <div class="reviewer-skills">
        <i class="fas fa-file-alt" title="Data Analytics"></i>
        <i class="fas fa-shield-alt" title="Information Security"></i>
        <i class="fas fa-link" title="Blockchain Technology"></i>
      </div>
    </div>
    <div class="reviewer-papers">
      <h3>Previous research papers</h3>
      <ul>
        ${reviewer.researchPapers.map(paper => `
          <li>
            <span>${paper.title}</span>
            <div class="paper-score">
              <span>${paper.score}%</span>
              <div class="progress-bar">
                <div class="progress" style="width: ${paper.score}%"></div>
              </div>
            </div>
          </li>
        `).join('')}
      </ul>
    </div>
  `;

  popupOverlay.style.display = 'flex';
}

function closePopup() {
  const popupOverlay = document.getElementById('popupOverlay');
  popupOverlay.style.display = 'none';
}

let selectedReviewerIndex = null; // Variabel untuk menyimpan index reviewer yang dipilih

function confirmChoose(index) {
  selectedReviewerIndex = index; // Simpan index reviewer yang dipilih
  const confirmPopup = document.getElementById('confirmPopup');
  confirmPopup.style.display = 'flex'; // Tampilkan pop-up konfirmasi
}

document.getElementById('confirmChooseBtn').addEventListener('click', function() {
  // Logika untuk memilih reviewer
  const reviewer = reviewers[selectedReviewerIndex];
  
  // Hapus reviewer dari daftar
  reviewers.splice(selectedReviewerIndex, 1);
  
  // Perbarui tabel setelah menghapus reviewer
  populateReviewersTable();

  alert(`Reviewer ${reviewer.name} telah dipilih!`);
  closeConfirmPopup();
});

function closeConfirmPopup() {
  const confirmPopup = document.getElementById('confirmPopup');
  confirmPopup.style.display = 'none'; // Sembunyikan pop-up konfirmasi
}

// Inisialisasi halaman
document.addEventListener('DOMContentLoaded', () => {
  populateReviewersTable();
});

function redirectToHistory() {
  window.location.href = '/history'; // Ganti dengan URL yang sesuai untuk halaman history Anda
}

document.addEventListener('DOMContentLoaded', function() {
  const findReviewerBtn = document.getElementById('goBackBtn');
  if (findReviewerBtn) {
      findReviewerBtn.addEventListener('click', function() {
          const url = this.getAttribute('data-url');
          window.location.href = url;
      });
  }
});
document.addEventListener('DOMContentLoaded', function() {
  const findReviewerBtn = document.getElementById('OkeBtn');
  if (findReviewerBtn) {
      findReviewerBtn.addEventListener('click', function() {
          const url = this.getAttribute('data-url');
          window.location.href = url;
      });
  }
});
