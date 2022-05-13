/* 
 * --------------------------------------------------------
 * Validar que el correo electronico del usuario coincida
 * con el estandar de seguridad. 
 * --------------------------------------------------------
*/
const isValidateUser = $("#send-button").on("click", () => {
    const email = $("#email").val();
    const pass = $("#pass").val();
    const passDefault = "admin"
    const dominioEmail = "coppel.com"
    let emailSplit = email.split("@");

    if (email == "" || pass == "") {
        Swal.fire({
            icon: 'warning',
            title: '¡Cuidado!',
            text: 'Por favor ingresa tu correo y/o Contraseña',
            confirmButtonColor: '#FFC479',
        });
    }
    else if (emailSplit[1] != dominioEmail) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Tu correo es incorrecto',
            confirmButtonColor: '#FF6666',
        });
    }
    else if (pass != passDefault) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Contraseña incorrecta',
            confirmButtonColor: '#FF6666',
        });
    }
    else {
        $(location).attr('href', '/home')
    }
});
