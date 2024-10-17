document.addEventListener('DOMContentLoaded', function() {
  const uploadBtn = document.querySelector('.upload-button');
  const uploadArea = document.querySelector('.upload-area');
  const fileInput = document.getElementById('fileInput');
  const browseLink = document.querySelector('.browse-link');
  const fileNameDisplay = document.querySelector('.file-name');
  const goBtn = document.querySelector('#go-btn');
  const uploadPage = document.getElementById('upload-page');
  const reviewerScrapingPage = document.getElementById('reviewer-scraping-page');

  function showPage(page) {
      uploadPage.classList.add('hidden');
      reviewerScrapingPage.classList.add('hidden');
      page.classList.remove('hidden');
  }

  browseLink.addEventListener('click', function(e) {
      e.preventDefault();
      fileInput.click();
  });

  fileInput.addEventListener('change', function() {
      if (fileInput.files.length > 0) {
          fileNameDisplay.textContent = `Selected file: ${fileInput.files[0].name}`;
      }
  });

  uploadBtn.addEventListener('click', function() {
      if (fileInput.files.length > 0) {
          alert('Uploading files...');
          setTimeout(() => {
              showPage(reviewerScrapingPage);
          }, 1000);
      } else {
          alert('Please select a file before uploading.');
      }
  });

  uploadArea.addEventListener('dragover', function(e) {
      e.preventDefault();
      this.style.border = '2px dashed #4F46E5';
  });

  uploadArea.addEventListener('dragleave', function() {
      this.style.border = 'none';
  });

  uploadArea.addEventListener('drop', function(e) {
      e.preventDefault();
      this.style.border = 'none';
      if (e.dataTransfer.files.length > 0) {
          fileInput.files = e.dataTransfer.files;
          fileNameDisplay.textContent = `Selected file: ${fileInput.files[0].name}`;
      }
      alert('Files dropped. Uploading...');
      setTimeout(() => {
          showPage(reviewerScrapingPage);
      }, 1000);
  });

  goBtn.addEventListener('click', function() {
      alert('Starting reviewer scraping process...');
  });

  // Show upload page by default
  showPage(uploadPage);
});