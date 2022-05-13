const sendRequest = $("#request").on("click", () => {
    let formData = new FormData();
    let request = new XMLHttpRequest();
    let filesForm = document.getElementById("files");

    if (filesForm.files.length == 0) {
        Swal.fire({
            icon: 'warning',
            title: 'Alto',
            text: 'Por favor selecciona tus archivos antes de continuar',
            confirmButtonColor: '#FFC479',
        });
    }
    else {
        for (let i = 0; i < filesForm.files.length; i++) {
            formData.append('files', filesForm.files[i]);
        }
        request.open('POST', '/savedata');
        request.send(formData)
        request.onload = () => {
            let status = request.status
            if (status == 200) {
                console.log("ok")
            }
        }
    }
});