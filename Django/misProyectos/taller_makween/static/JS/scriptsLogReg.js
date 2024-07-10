document.addEventListener('DOMContentLoaded', (event) => {
    const popupMessage = document.getElementById('popupMessage');
    if (popupMessage) {
        setTimeout(() => {
            popupMessage.style.display = 'none';
        }, 3000); // Duracióm de 3 secs
    }
});
