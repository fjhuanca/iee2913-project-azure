
let socket = new WebSocket(
    (window.location.protocol == 'https:' ? 'wss://' : 'ws://')
        + 'iee2913-g10-project.southcentralus.cloudapp.azure.com:8001/ws/ecg');

socket.onopen = function(e){
    alert('Conectado Exitosamente');
};

socket.onmessage = function(e){
    // console.log(e.data);
    var recData = JSON.parse(e.data);
    dataObjNew = dataObj['data']['datasets'][0]['data'];
    dataObjNew.shift();
    dataObjNew.push(recData.value);
    dataObj['data']['datasets'][0]['data'] = dataObjNew;
    window.myLine.update();
};

socket.onclose = function(e){
    alert("Desconectado");
};

var dataObj = {
    type: 'line',
    data: {
        labels: [...(Array(50).fill('')).values()],
        datasets: [{
            label: 'ECG 2 canales',
            data: [...(Array(50).fill(0)).values()],
            backgroundColor: ['rgba(255, 99, 132, 0.5)', ],
            borderColor: ['rgba(255, 99, 132, 1)', ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
}
var ctx = document.getElementById('myChart').getContext('2d');
window.myLine = new Chart(ctx, dataObj);
