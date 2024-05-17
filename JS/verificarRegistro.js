$(document).ready(function() {
    $('#registerForm').submit(function(event) {
        event.preventDefault(); // Evitar elementos en blanco

        $('.invalid-feedback').text(''); // Eliminar mensaje sde error
        // Recibir valores dentro de cada input.
        var rut = $('#rut').val();
        var k = $('#k').val();
        var nombres = $('#nombres').val();
        var apellidos = $('#apellidos').val();
        var email = $('#email').val();
        var contrasena = $('#contrasena').val();
        var confirmarContrasena = $('#confirmarContrasena').val();

        // Siblings: Busca los elementos que sean "Hermanos", esto es
        // debido a la jerarquía de los divs dentro del DOM.

        // Validar el RUT
        if (rut.trim() === '') { // Elimina los espacios en blancos del campo para evitar que esté rellenado con espacios en blanco.
            $('#rut').addClass('is-invalid'); // Selecciona y verifica el elemento "rut" desde el DOM
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
            $('#email').siblings('.invalid-feedback').text('Introduzca un correo electrónico válido');
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

        // Validar que las contraseñas coincidan
        if (contrasena !== confirmarContrasena) {
            $('#confirmarContrasena').addClass('is-invalid');
            $('#confirmarContrasena').siblings('.invalid-feedback').text('Las contraseñas deben coincidir.');
            return;
        }
    });

    // Función para validar el formato del correo electrónico
    function validateEmail(email) {
        var requerimientos = /\S+@\S+\.\S+/;
        return requerimientos.test(email);
    }
});
