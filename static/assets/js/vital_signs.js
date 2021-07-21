let socket_signs = new WebSocket(
    (window.location.protocol == 'https:' ? 'wss://' : 'wss://')
    + 'iee2913-g10-project.southcentralus.cloudapp.azure.com/wss/sender/signs/');

// socket.onopen = function(e){
//     alert('Conectado Exitosamente');
// };

socket_signs.onmessage = function(e){
    // console.log(e.data);
    var recData = JSON.parse(e.data);
    document.getElementById("bpm_inst").innerHTML = recData.bpm + "(LPM)";
    document.getElementById("temp_inst").innerHTML = recData.temp + "°C";
    document.getElementById("spo_inst").innerHTML = recData.spo + "%";
    document.getElementById("bf_inst").innerHTML = recData.bf + " BPM";
};

// socket.onclose = function(e){
//     alert("Desconectado");
// };