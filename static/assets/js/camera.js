jQuery(function($){
    if (!('WebSocket' in window)) {
        alert('Your browser does not support web sockets');
    }
    else{
        setup();
    }
    function setup(){
        var host = (window.location.protocol == 'https:' ? 'wss://' : 'wss://') + 'iee2913-g10-project.southcentralus.cloudapp.azure.com/wss/sender/cam/';
        // var host = 'ws://localhost:8000/wss/sender/cam/'
        var socket = new WebSocket(host);
        socket.binaryType = 'arraybuffer';
        if(socket){
            socket.onopen = function(){alert("conectado");}
            socket.onmessage = function(msg){
                // alert("recibiendo");
                var recData = JSON.parse(msg.data);
                var bytes = _base64ToArrayBuffer(recData.bytes);
                console.log(bytes);
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

function _base64ToArrayBuffer(base64) {
    var binary_string = window.atob(base64);
    var len = binary_string.length;
    var bytes = new Uint8Array(len);
    for (var i = 0; i < len; i++) {
        bytes[i] = binary_string.charCodeAt(i);
    }
    return bytes;
}