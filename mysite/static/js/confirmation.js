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
