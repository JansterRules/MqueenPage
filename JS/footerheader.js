// Función para cargar el footer
function cargarFooter() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("footer-container").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "footer.html", true);
    xhttp.send();
}

// Función para cargar la barra de navegación
function cargarNavbar() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("navbar-container").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "navbar.html", true);
    xhttp.send();
}

// Llamar a las funciones para cargar el footer y la barra de navegación cuando se cargue la página
document.addEventListener("DOMContentLoaded", function() {
    cargarFooter();
    cargarNavbar();
});
