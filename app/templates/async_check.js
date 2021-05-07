fetch('/json_class_view')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        console.log(text);
    })