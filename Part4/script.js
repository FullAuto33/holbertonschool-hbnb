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


function checkAuthentication() {
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (!token) {
    loginLink.style.display = 'block';
  } else {
    loginLink.style.display = 'none';
    fetchPlaces(token);
  }
}



async function fetchPlaces(token) {
  try {
    const response = await fetch('https://your-api-url/places', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    if (!response.ok) {
      throw new Error('Erreur lors du chargement des lieux');
    }
    const places = await response.json();
    displayPlaces(places);
  } catch (error) {
    alert(error.message);
  }
}


document.getElementById('price-filter').addEventListener('change', (event) => {
  const maxPrice = event.target.value;
  const placesList = document.getElementById('places-list');
  const placeCards = placesList.getElementsByClassName('place-card');

  Array.from(placeCards).forEach(card => {
    const price = parseFloat(card.dataset.price);
    if (maxPrice === 'All' || price <= maxPrice) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
});


function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get('id'); // Assure-toi que l’URL est du type place.html?id=123
}


let jwtToken = null;
let placeId = null;

function checkAuthenticationAndLoad() {
  placeId = getPlaceIdFromURL();
  jwtToken = getCookie('token');
  const addReviewSection = document.getElementById('add-review');

  if (!jwtToken) {
    // Non authentifié : cacher le formulaire d'ajout de review
    addReviewSection.style.display = 'none';
    fetchPlaceDetails(null, placeId); // On peut quand même afficher les détails, sans token
  } else {
    // Authentifié : afficher le formulaire
    addReviewSection.style.display = 'block';
    fetchPlaceDetails(jwtToken, placeId);
  }
}


async function fetchPlaceDetails(token, placeId) {
  if (!placeId) {
    alert('ID du lieu manquant dans l’URL');
    return;
  }

  try {
    const headers = token ? { 'Authorization': `Bearer ${token}` } : {};

    const response = await fetch(`https://your-api-url/places/${placeId}`, { headers });

    if (!response.ok) {
      throw new Error('Erreur lors du chargement des détails');
    }

    const place = await response.json();
    displayPlaceDetails(place);

  } catch (error) {
    alert(error.message);
  }
}

function displayPlaceDetails(place) {
  const placeDetailsSection = document.getElementById('place-details');
  placeDetailsSection.innerHTML = ''; // Vider le contenu

  // Créer éléments d’affichage
  const title = document.createElement('h2');
  title.textContent = place.name;

  const price = document.createElement('p');
  price.textContent = `Prix par nuit : $${place.price}`;

  const description = document.createElement('p');
  description.textContent = place.description;

  const amenities = document.createElement('ul');
  amenities.textContent = 'Équipements :';
  place.amenities.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    amenities.appendChild(li);
  });

  // Section reviews
  const reviewsSection = document.createElement('div');
  reviewsSection.id = 'reviews';
  reviewsSection.innerHTML = '<h3>Avis</h3>';

  if (place.reviews && place.reviews.length > 0) {
    place.reviews.forEach(review => {
      const reviewCard = document.createElement('div');
      reviewCard.classList.add('review-card');
      reviewCard.innerHTML = `
        <p>"${review.comment}"</p>
        <p>Par : <strong>${review.user}</strong></p>
        <p>Note : ${review.rating} / 5</p>
      `;
      reviewsSection.appendChild(reviewCard);
    });
  } else {
    reviewsSection.innerHTML += '<p>Aucun avis pour ce lieu.</p>';
  }

  // Ajouter tous les éléments au conteneur principal
  placeDetailsSection.appendChild(title);
  placeDetailsSection.appendChild(price);
  placeDetailsSection.appendChild(description);
  placeDetailsSection.appendChild(amenities);
  placeDetailsSection.appendChild(reviewsSection);
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}

function getPlaceIdFromURL() {
  const params = new URLSearchParams(window.location.search);
  return params.get('id'); // attend URL du type add_review.html?id=123
}

function checkAuthentication() {
  const token = getCookie('token');
  if (!token) {
    // Redirige vers la page d'accueil si pas connecté
    window.location.href = 'index.html';
  }
  return token;
}

async function submitReview(token, placeId, reviewText, rating) {
  try {
    const response = await fetch(`https://your-api-url/places/${placeId}/reviews`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ comment: reviewText, rating: Number(rating) })
    });

    if (response.ok) {
      alert('Review submitted successfully!');
      return true;
    } else {
      const errorData = await response.json();
      alert('Failed to submit review: ' + (errorData.message || response.statusText));
      return false;
    }
  } catch (error) {
    alert('Error submitting review: ' + error.message);
    return false;
  }
}
