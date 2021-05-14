setInterval(() => {
    var closestClass;
    function canGoToClass(date) {
        return date.getFullYear() === curTime.getFullYear() &&
                date.getMonth() === curTime.getMonth() &&
                date.getDate() === curTime.getDate() &&
                date.getDay() === curTime.getDay() &&
                date.getHours() === curTime.getHours() &&
                date.getMinutes() - curTime.getMinutes() <= 5 &&
                date.getMinutes() - curTime.getMinutes() >= 0
    }
    var curTime = new Date();
    fetch('/json_class_view')
        .then((res) => {
            return res.json();
        }).then((text) => {
            console.log(text);
            closestClass =  text[Object.keys(text)[0]];
            var date = new Date((closestClass[0]['start_time']));
            
            if (canGoToClass(date)) {
                    // window.open(closestClass[0]['class_link'], '_blank')
                    
                    var yon = prompt("Time to go to class! (y/n)")
                    switch (yon) {
                        case 'y':
                            //if done===true then stop
                            if (closestClass[0]['done'] === false) {
                                var miwindow = window.open(closestClass[0]['class_link'], "_blank");
                                var xhttp = new XMLHttpRequest();
                                xhttp.open("POST", "/done?", true);
                                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                                xhttp.send(`className=${closestClass[0]['done']}`)
                                break;
                            }
                            
                            // miwindow.write("<h1>GOOD LUCK IN CLASS</h1>")
                        default:
                            break;
                    }

                //add classdone prperty
                }
        });


    
}, 1000);
