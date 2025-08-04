document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = loginForm.email.value.trim();
      const password = loginForm.password.value;

      if (!email || !password) {
        alert('Veuillez remplir tous les champs.');
        return;
      }

      try {
        const response = await fetch('https://your-api-url/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email, password }),
        });

        if (response.ok) {
          const data = await response.json();

          // Stocker le token JWT dans un cookie (expire dans 1 jour ici)
          const token = data.access_token;
          const expires = new Date();
          expires.setTime(expires.getTime() + 24 * 60 * 60 * 1000);
          document.cookie = `token=${token}; expires=${expires.toUTCString()}; path=/`;

          // Redirection vers la page principale
          window.location.href = 'index.html';
        } else {
          // Gestion erreur (exemple simple)
          const errorData = await response.json();
          alert('Échec de la connexion : ' + (errorData.message || response.statusText));
        }
      } catch (error) {
        alert('Erreur réseau ou serveur : ' + error.message);
      }
    });
  }
});


function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}
