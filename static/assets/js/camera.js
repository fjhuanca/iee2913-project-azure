jQuery(function($){
    if (!('WebSocket' in window)) {
        alert('Your browser does not support web sockets');
    }
    else{
        setup();
    }
    function setup(){
        var host = (window.location.protocol == 'https:' ? 'wss://' : 'ws://') + 'iee2913-g10-project.southcentralus.cloudapp.azure.com/wss/sender/cam/';
        // var host = 'ws://localhost:8001/wss/sender/cam/'
        var socket = new WebSocket(host);
        socket.binaryType = 'arraybuffer';
        if(socket){
            socket.onopen = function(){alert("conectado");}
            socket.onmessage = function(msg){
                // alert("recibiendo");
                var bytes = new Uint8Array(msg.data);
                var binary= '';
                var len = bytes.byteLength;
                for (var i = 0; i < len; i++) {
                    binary += String.fromCharCode(bytes[i]);
                }
                var img = document.getElementById('live');
                img.src = 'data:image/jpg;base64,'+window.btoa(binary);
            }
            socket.onclose = function(){
                showServerResponse('The connection has been closed.');
            }
        }
    }
}
);