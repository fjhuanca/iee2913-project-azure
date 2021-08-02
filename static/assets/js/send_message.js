socket = new WebSocket(
    (window.location.protocol == 'https:' ? 'wss://' : 'wss://')
        + 'iee2913-g10-project.southcentralus.cloudapp.azure.com/wss/receiver/info/');

function sendUpdate(){
    socket.send(JSON.stringify({led: 0, new_message: 1}))
}