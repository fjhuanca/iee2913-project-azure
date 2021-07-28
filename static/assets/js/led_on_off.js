function startLedSocket(){
    $('#toggle').bootstrapToggle("off")
    
    console.log("ready");
    alert("ready");
    // let socket2 = new WebSocket(
    //     (window.location.protocol == 'https:' ? 'ws://' : 'ws://')
    //     + 'localhost:8000/wss/receiver/led/');
        
    let socket = new WebSocket(
            (window.location.protocol == 'https:' ? 'wss://' : 'wss://')
                + 'iee2913-g10-project.southcentralus.cloudapp.azure.com/wss/receiver/led/');
            // Send to Everyone on channel test123
    t = setInterval(function() {
        val =  ($('#toggle').prop('checked')) ? 1: 0;
        socket2.send(JSON.stringify({status: val}));
        console.log("here");
    }, 5000 );
}