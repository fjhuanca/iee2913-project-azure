    $('#toggle').bootstrapToggle("off")    
    console.log("ready");
    // let socket2 = new WebSocket(
    //     (window.location.protocol == 'https:' ? 'ws://' : 'ws://')
    //     + 'localhost:8000/wss/receiver/led/');
        
    socket2 = new WebSocket(
            (window.location.protocol == 'https:' ? 'wss://' : 'wss://')
                + 'iee2913-g10-project.southcentralus.cloudapp.azure.com/wss/receiver/info/');

    socket3 = new WebSocket(
                    (window.location.protocol == 'https:' ? 'wss://' : 'wss://')
                        + 'iee2913-g10-project.southcentralus.cloudapp.azure.com/wss/sender/info/');
    socket3.onmessage = function(e){
        // console.log(e.data);
        var recData = JSON.parse(e.data)
        isOn = parseInt(recData.led);
        val =  ($('#toggle').prop('checked')) ? 1: 0;
        if (isOn && isOn != val) $('#toggle').bootstrapToggle("on");
        else if(!isOn && (isOn != val)) $('#toggle').bootstrapToggle("off");
    };
            // Send to Everyone on channel test123
    const checkbox = document.getElementById("toggle");
    checkbox.onchange = function (event){
        val =  ($('#toggle').prop('checked')) ? 1: 0;
        if (socket2.readyState) socket2.send(JSON.stringify({led: val, new_message: 0}));
        // console.log("here");
    };