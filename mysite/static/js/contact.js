const contacts = [
    { name: "Kevin Nathaneal", email: "customerservice1@gmail.com", photo: "https://example.com/photo1.jpg" },
    { name: "Dimas Respati", email: "customerservice2@gmail.com", photo: "https://example.com/photo2.jpg" },
    { name: "Nadia Risky", email: "customerservice3@gmail.com", photo: "https://example.com/photo3.jpg" },
    { name: "Rosie Glover", email: "customerservice4@gmail.com", photo: "https://example.com/photo4.jpg" },
    { name: "Patrick Greer", email: "customerservice5@gmail.com", photo: "https://example.com/photo5.jpg" },
    { name: "Darrell Ortega", email: "customerservice6@gmail.com", photo: "https://example.com/photo6.jpg" }
];

function createContactCard(contact) {
    return `
        <div class="contact-card">
            <img src="${contact.photo}" alt="${contact.name}">
            <div class="contact-info">
                <h3>${contact.name}</h3>
                <p>${contact.email}</p>
                <button class="message-btn" onclick="sendEmail('${contact.email}')">Message</button>
            </div>
        </div>
    `;
}

function renderContacts() {
    const contactGrid = document.getElementById('contactGrid');
    contactGrid.innerHTML = contacts.map(createContactCard).join('');
}

function sendEmail(email) {
    window.location.href = `mailto:${email}`;
}

renderContacts();
