// Rolagem suave para links de navegação
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// Formulário de contato (exemplo de validação simples)
document.querySelector('form').addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Mensagem enviada com sucesso!');
  this.reset();
});