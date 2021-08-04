
let socket = new WebSocket(
    (window.location.protocol == 'https:' ? 'wss://' : 'wss://')
        + 'iee2913-g10-project.southcentralus.cloudapp.azure.com/wss/sender/ecg/');

socket.onopen = function(e){
    alert('Conectado Exitosamente');
};

ecg_val = {
    valueInternal: -1,
    valueListener: function(val) {},
    set value(val) {
      this.pastValue = this.valueInternal;
      this.valueInternal = val;
      this.valueListener(val);
    },
    get value() {
      return this.valueInternal;
    },
    onchange: function(listener) {
      this.valueListener = listener;
    }
  };

var isTabActive;

  window.onfocus = function () { 
    isTabActive = true; 
  }; 
  
  window.onblur = function () { 
    isTabActive = false; 
}; 

ecg_val.onchange(function(val){
    var status_ecg = document.getElementById("status-ecg")
    if (val >= 0 && ecg_val.pastValue < 0){
        status_ecg.className = "text-success fw-bold";
        status_ecg.textContent = "Monitoreando";
    }
    else if (val < 0){
        status_ecg.className = "text-danger fw-bold";
        status_ecg.textContent = "Esperando";
    }
});

socket.onmessage = function(e){
    // console.log(e.data);
    var recData = JSON.parse(e.data);
    ecg_val.value = recData.value;
    if (ecg_val.value >= 0 && isTabActive){
        dataObjNew = dataObj['data']['datasets'][0]['data'];
        dataObjNew.shift();
        dataObjNew.push(recData.value);
        dataObj['data']['datasets'][0]['data'] = dataObjNew;
        window.myLine.update();
    }
};

socket.onclose = function(e){
    alert("Desconectado");
};

var dataObj = {
    type: 'line',
    data: {
        labels: [...(Array(100).fill('')).values()],
        datasets: [{
            label: 'ECG 2 canales',
            data: [...(Array(100).fill(0)).values()],
            backgroundColor: ['rgba(255, 99, 132, 0.5)', ],
            borderColor: ['rgba(255, 99, 132, 1)', ],
            borderWidth: 1
        }]
    },
    options: {
        animation: false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
}
var ctx = document.getElementById('myChart').getContext('2d');
window.myLine = new Chart(ctx, dataObj);
