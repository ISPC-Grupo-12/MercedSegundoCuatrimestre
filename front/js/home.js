const form = document.getElementById('newsletterForm');
const message = document.getElementById('message');

form.addEventListener('submit', function(e) {
    e.preventDefault(); // evita que se recargue la página

    const email = document.getElementById('emailInput').value;

    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(regex.test(email)) {
        message.style.display = 'block';
        message.innerText = `¡Gracias por suscribirte, ${email}!`;
        form.reset();
    } else {
        alert('Por favor, ingresá un correo válido.');
    }
});
