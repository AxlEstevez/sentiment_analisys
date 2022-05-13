$(document).on('load', function () {
    let request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:5000/sendRequets')
    request.send()
    let result = request.responseText
    let newImage = document.createElement('img')
    newImage.src = "./../images/icon.jpg";
    document.appendChild(newImage)
});
