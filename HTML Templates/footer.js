document.addEventListener("DOMContentLoaded", function() {
    var footerDiv = document.getElementById('footerDiv'); // Elemento de la clase para el div.
    if (footerDiv) {
        footerDiv.innerHTML = `
        <div class="container-fluid pieDePagina">
            <h1 style="text-align: center;">¡Contáctanos en TALLER MQUEEN!</h1>
            <div class="row">
                <div class="col-12 col-md-12">
                    <ul>
                        <li><a href="#" style="color: white;">Términos y condiciones</a></li>
                        <li><a href="#" style="color: white;">Política de privacidad</a></li>
                        <li><a href="#" style="color: white;">Contacto</a></li>
                    </ul>
                </div>
            </div>
        </div>
        `;
    }
});
