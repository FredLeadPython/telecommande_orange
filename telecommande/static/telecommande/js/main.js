document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.remote-btn');

    // Fonction pour récupérer le token CSRF depuis les cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    buttons.forEach(button => {
        button.addEventListener('click', async () => {
            const key = button.dataset.key;
            if (!key) return;

            try {
                const response = await fetch(sendCommandUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify({ key: key })
                });

                const result = await response.json();

                if (response.ok) {
                    console.log('Succès:', result.message);
                    // Animation visuelle pour le clic
                    button.classList.add('clicked');
                    setTimeout(() => button.classList.remove('clicked'), 150);
                } else {
                    console.error('Erreur:', result.message);
                    alert(`Erreur de commande : ${result.message}`);
                }
            } catch (error) {
                console.error('Erreur réseau ou serveur:', error);
                alert("Impossible de contacter le serveur Django ou le décodeur.");
            }
        });
    });
});
