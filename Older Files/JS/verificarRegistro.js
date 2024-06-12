$(document).ready(function() {
    $('#registerForm').submit(function(event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto
        
        $('.invalid-feedback').text(''); // Limpiar mensajes de error
        $('.form-control').removeClass('is-invalid'); // Remover clases de invalid

        var rut = $('#rut').val();
        var k = $('#k').val();
        var nombres = $('#nombres').val();
        var apellidos = $('#apellidos').val();
        var email = $('#email').val();
        var contrasena = $('#contrasena').val();
        var confirmarContrasena = $('#confirmarContrasena').val();

        // Validar el RUT
        if (rut.trim() === '') {
            $('#rut').addClass('is-invalid');
            $('#rut').siblings('.invalid-feedback').text('El RUT es requerido.');
            return;
        }

        // Validar el dígito verificador
        if (k.trim() === '') {
            $('#k').addClass('is-invalid');
            $('#k').siblings('.invalid-feedback').text('El dígito verificador es requerido.');
            return;
        }

        // Validar los nombres
        if (nombres.trim() === '') {
            $('#nombres').addClass('is-invalid');
            $('#nombres').siblings('.invalid-feedback').text('Ingrese su nombre.');
            return;
        }

        // Validar los apellidos
        if (apellidos.trim() === '') {
            $('#apellidos').addClass('is-invalid');
            $('#apellidos').siblings('.invalid-feedback').text('Ingrese sus apellidos.');
            return;
        }

        // Validar el formato de correo electrónico
        if (!validateEmail(email)) {
            $('#email').addClass('is-invalid');
            $('#email').siblings('.invalid-feedback').text('Introduzca un correo electrónico válido.');
            return;
        }

        // Validar la contraseña
        if (contrasena.trim() === '') {
            $('#contrasena').addClass('is-invalid');
            $('#contrasena').siblings('.invalid-feedback').text('La contraseña es requerida.');
            return;
        }

        // Validar la longitud de la contraseña
        if (contrasena.length < 8) {
            $('#contrasena').addClass('is-invalid');
            $('#contrasena').siblings('.invalid-feedback').text('La contraseña debe tener al menos 8 caracteres.');
            return;
        }

        if (contrasena !== confirmarContrasena) {
            $('#confirmarContrasena').addClass('is-invalid');
            $('#confirmarContrasena').siblings('.invalid-feedback').text('Las contraseñas deben coincidir.');
            return;
        }

        alert('Formulario validado con éxito.');
    });

    function validateEmail(email) {
        var reqCaracterEmail = /\S+@\S+\.\S+/;
        return reqCaracterEmail.test(email);
    }
});
