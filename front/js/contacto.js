document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contactForm');
  const feedback = document.getElementById('feedback');

  const phoneRegex = /^\+?[0-9\s\-]{7,15}$/;
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    feedback.innerHTML = ''; 

    const data = {
      name: form.name.value.trim(),
      apellido: form.apellido.value.trim(),
      email: form.email.value.trim(),
      telefono: form.telefono.value.trim(),
      asunto: form.asunto.value.trim(),
      message: form.message.value.trim()
    };

    // validaciones básicas
    if (!data.name || !data.apellido || !data.email || !data.telefono || !data.asunto || !data.message) {
      feedback.innerHTML = `<div class="alert alert-danger" role="alert">Por favor completá todos los campos.</div>`;
      return;
    }

    if (!emailRegex.test(data.email)) {
      feedback.innerHTML = `<div class="alert alert-danger" role="alert">Ingresá un correo válido.</div>`;
      form.email.focus();
      return;
    }

    if (!phoneRegex.test(data.telefono)) {
      feedback.innerHTML = `<div class="alert alert-danger" role="alert">Ingresá un teléfono válido (ej: +54 11 1234-5678).</div>`;
      form.telefono.focus();
      return;
    }

    feedback.innerHTML = `<div class="alert alert-success" role="alert">Gracias ${data.name}, tu mensaje fue enviado correctamente.</div>`;

    
    form.submit();

    
  });
});
