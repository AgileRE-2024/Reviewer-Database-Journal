const data = [
    { id: '00001', paperTitle: 'Optimizing Cloud Computing Performance Using Load Balancing Algorithms', date: '2023-09-04', type: 'Technology', status: 'Completed' },
    { id: '00002', paperTitle: 'Blockchain Technology for Secure Digital Identity Management', date: '2024-05-28', type: 'Technology', status: 'Processing' },
    { id: '00003', paperTitle: 'Machine Learning Applications in Predicting Student Performance in E-Learning Platforms', date: '2023-11-23', type: 'Technology', status: 'Processing' },
    { id: '00004', paperTitle: 'The Role of Gamification in Enhancing Student Engagement in Higher Education', date: '2022-02-05', type: 'Education', status: 'Completed' },
    { id: '00005', paperTitle: 'Impact of Blended Learning on Academic Achievement in University Settings', date: '2024-07-29', type: 'Education', status: 'Processing' },
    { id: '00006', paperTitle: 'Integrating Critical Thinking Skills in Language Learning Curricula', date: '2024-08-15', type: 'Education', status: 'Completed' },
    { id: '00007', paperTitle: 'The Influence of Corporate Social Responsibility on Brand Loyalty: A Case Study in the Food Industry', date: '2023-12-21', type: 'Economy', status: 'Processing' },
    { id: '00008', paperTitle: 'Financial Technology (FinTech) Adoption among SMEs: Opportunities and Challenges', date: '2024-04-30', type: 'Economy', status: 'Completed' },
    { id: '00009', paperTitle: 'Analyzing the Impact of Leadership Styles on Employee Motivation and Productivity', date: '2024-01-09', type: 'Economy', status: 'Completed' },
    // Add more entries to test pagination...
];

const dateFilter = document.getElementById('dateFilter');
const typeFilter = document.getElementById('typeFilter');
const statusFilter = document.getElementById('statusFilter');
const entriesPerPage = document.getElementById('entriesPerPage');
const tableBody = document.querySelector('#paperTable tbody');
const tableInfo = document.getElementById('tableInfo');
const pageInfo = document.getElementById('pageInfo');
const prevPageBtn = document.getElementById('prevPage');
const nextPageBtn = document.getElementById('nextPage');

let currentPage = 1;
let filteredData = [];

function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { day: '2-digit', month: 'short', year: 'numeric' };
    return date.toLocaleDateString('en-GB', options);
}

function updateTable() {
    filteredData = data.filter(item => {
        return (!dateFilter.value || item.date === dateFilter.value) &&
               (!typeFilter.value || item.type === typeFilter.value) &&
               (!statusFilter.value || item.status === statusFilter.value);
    });

    const pageSize = parseInt(entriesPerPage.value);
    const totalPages = Math.ceil(filteredData.length / pageSize);

    if (currentPage > totalPages) {
        currentPage = totalPages || 1;
    }

    const start = (currentPage - 1) * pageSize;
    const end = start + pageSize;
    const paginatedData = filteredData.slice(start, end);

    tableBody.innerHTML = paginatedData.map(item => `
        <tr class="${item.status.toLowerCase()}">
            <td>${item.id}</td>
            <td>${item.paperTitle}</td>
            <td>${formatDate(item.date)}</td>
            <td>${item.type}</td>
            <td>${item.status}</td>
        </tr>
    `).join('');

    tableInfo.textContent = `Showing ${start + 1} to ${Math.min(end, filteredData.length)} of ${filteredData.length} entries (filtered from ${data.length} total entries)`;
    pageInfo.textContent = `Page ${currentPage} of ${totalPages}`;

    prevPageBtn.disabled = currentPage === 1;
    nextPageBtn.disabled = currentPage === totalPages;
}

function resetFilters() {
    dateFilter.value = '';
    typeFilter.value = '';
    statusFilter.value = '';
    currentPage = 1;
    updateTable();
}

function changePage(direction) {
    currentPage += direction;
    updateTable();
}

dateFilter.addEventListener('change', () => { currentPage = 1; updateTable(); });
typeFilter.addEventListener('change', () => { currentPage = 1; updateTable(); });
statusFilter.addEventListener('change', () => { currentPage = 1; updateTable(); });
entriesPerPage.addEventListener('change', () => { currentPage = 1; updateTable(); });

updateTable();
