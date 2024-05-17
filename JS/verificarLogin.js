$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto
        
        // Limpiar mensajes de errores
        $('.error-message').text('');
        
        var email = $('#exampleInputEmail1').val(); // Recuperamos email del campo de "email".
        var password = $('#exampleInputPassword1').val(); // Igualmente aquí, solamente el campo de password.

        if (!validarEmail(email)) {
            $('#emailError').text('Introduzca un correo electrónico válido.');
            return;
        }
        
        if (password.length < 8) {
            $('#passwordError').text('La contraseña debe tener al menos 8 caracteres.');
            return;
        }

        // Si los datos son válidos, puedes enviar el formulario o realizar otras acciones
        this.submit();
    });

    function validarEmail(email) { // Función para validar email 
        var emailPattern = /\S+@\S+\.\S+/; // Verificar valores antes del "@" y después del "@"
        return emailPattern.test(email);
    }
});

(function() {
    'use strict';
    var forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms)
        .forEach(function(form) {
            form.addEventListener('submit', function(event) {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                    
                    // Mostrar mensajes de error personalizados
                    $(form).find('.error-message').each(function() {
                        if (!$(this).prev().is(':valid')) {
                            $(this).text($(this).prev().attr('data-error-message'));
                        }
                    });
                }
                form.classList.add('was-validated');
            }, false);
        });
})();