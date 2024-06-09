document.addEventListener("DOMContentLoaded", function() { // Elementos bootstrap
    var head = document.head; // Implementación en el head
    var linkBootstrap = document.createElement("link");
    linkBootstrap.rel = "stylesheet";
    linkBootstrap.href = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css";
    linkBootstrap.integrity = "sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH";
    linkBootstrap.crossOrigin = "anonymous";
    head.appendChild(linkBootstrap);
 
    // Insertar el contenido del cuerpo (navbar)
    var navbarHtml = `
            <nav class="navbar navbar-expand-lg bg-dark border-bottom border-body" data-bs-theme="dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="index.html">
                    <img src="{% static '/IMG/archivoImg/logo.jpg' %}" alt="" width="80" height="74">
                </a>            
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <a class="navbar-brand" href="index.html">Taller Makween</a>
                </button>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="index.html">Inicio</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="galeria">Galería</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="faq">Preguntas frecuentes</a>
                        </li>
                    </ul>
                    <ul class="navbar-nav mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="login">Ingresar</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="register">Registrar</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    `;
    var body = document.body;
    body.insertAdjacentHTML('afterbegin', navbarHtml);
});
