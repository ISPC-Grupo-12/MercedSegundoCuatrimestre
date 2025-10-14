document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('loginForm');
  const feedback = document.getElementById('feedback');

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    feedback.innerHTML = '';

    const email = form.email.value.trim();
    const password = form.password.value;

    if (!email || !password) {
      feedback.innerHTML = `<div class="alert alert-danger">Completá todos los campos</div>`;
      return;
    }

    // simple validación de email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      feedback.innerHTML = `<div class="alert alert-danger">Correo inválido</div>`;
      return;
    }
  
  //Credenciales hardcodeadas
  const usuarioValido = "usuario@merced.com";
  const contrasenaValida = "12345678";

  if (email === usuarioValido && password === contrasenaValida) {
    alert("Inicio de sesión exitoso ✅");
    window.location.href = "index.html"; // Redirigir a la página principal
  } else {
    feedback.innerHTML = `<div class="alert alert-danger">Credenciales inválidas</div>`;
  }
  });
  
  // redes sociales
  document.querySelector('.btn-google').addEventListener('click', () => alert('Google login (simulado)'));
  document.querySelector('.btn-facebook').addEventListener('click', () => alert('Facebook login (simulado)'));
  document.querySelector('.btn-x').addEventListener('click', () => alert('X login (simulado)'));
});
