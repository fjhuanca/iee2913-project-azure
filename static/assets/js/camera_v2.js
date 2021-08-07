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
        var header_received = false;
        var starflag = 0xAA;
        var endflag = 0xFF;
        var receiving = false;
        var binary = '';
        if(socket){
            socket.onopen = function(){
                alert("conectado");
            }
            socket.onmessage = function(msg){
                // alert("recibiendo");
                // var recData = JSON.parse(msg.data);
                // bytes = _base64ToArrayBuffer(recData.bytes);
                console.log(msg);
                bytes = new Uint8Array(msg.data);
                // console.log(bytes);
                // var binary= '';
                var len = bytes.byteLength;
                // console.log("here0");
                console.log(len);
                if (len==1 && bytes[0]==starflag ){
                    binary = '';
                    receiving = true;
                    // console.log("here1");
                }
                else if (len==1 && bytes[0]==endflag && receiving){
                    // console.log("here3")
                    receiving = false;
                    var img = document.getElementById('live');
                    img.src = 'data:image/jpg;base64,'+window.btoa(binary);
                    img.style.width = '35%'
                    img.style.height = '35%'
                }
                else if (receiving){
                    for (var i = 0; i < len; i++) {
                        binary += String.fromCharCode(bytes[i]);
                    }
                    // console.log("here2");
                }
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