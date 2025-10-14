// script.js
document.getElementById('registrationForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value.trim();
    const errorMessage = document.getElementById('errorMessage');

    const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$/;

    if (!regex.test(password)) {
    errorMessage.textContent = 'La contraseña debe contener al menos una letra y un número.';
    errorMessage.style.color = 'wing';
    return;
    }

    if (password !== confirmPassword) {
    errorMessage.textContent = 'Las contraseñas no coinciden.';
    errorMessage.style.color = 'wing';
    return;
    }

    errorMessage.textContent = '';
    alert('Registro exitoso!');
    this.reset();

    window.location.href = 'login.html';
});
