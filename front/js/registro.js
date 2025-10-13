// script.js
document.getElementById('registrationForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const errorMessage = document.getElementById('errorMessage');

    if (password !== confirmPassword) {
    errorMessage.textContent = 'Las contraseñas no coinciden.';
    } else {
    errorMessage.textContent = '';
    alert('¡Registro exitoso!');
    // Aquí puedes agregar lógica para enviar los datos al servidor
    this.reset();
    }
});
