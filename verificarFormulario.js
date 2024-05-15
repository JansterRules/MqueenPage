$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto
        $('.error-message').text(''); // Limpiar mensajes de errores
        
        var email = $('#exampleInputEmail1').val(); // Recuperamos email del campo de "email".
        var password = $('#exampleInputPassword1').val(); // Igualmente aquí, solamente el campo de password.

        if (!validarEmail(email)) {
            $('#emailError').text('Introduzca un corre electrónico válido.');
            return;
        }
        
        if (password.length < 8) {
            $('#passwordError').text('La contraseña debe tener al menos 8 caracteres.');
            return;
        }
    });

    function validarEmail(email) { // Función para validar email 
        var valoresRequeridos = /\S+@\S+\.\S+/; // Verificar valores antes del "@" y después del "@"
        return valoresRequeridos.test(email);
    }
});
