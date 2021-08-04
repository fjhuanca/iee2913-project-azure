let socket_signs = new WebSocket(
    (window.location.protocol == 'https:' ? 'wss://' : 'wss://')
    + 'iee2913-g10-project.southcentralus.cloudapp.azure.com/wss/sender/signs/');

// socket.onopen = function(e){
//     alert('Conectado Exitosamente');
// };

bpm = {
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

bpm.onchange(function(val){
    var status_bpm = document.getElementById("status-bpm")
    if (val >= 0 && bpm.pastValue < 0){
        status_bpm.className = "text-success fw-bold";
        status_bpm.textContent = "Monitoreando";
    }
    else if (val < 0){
        status_bpm.className = "text-danger fw-bold";
        status_bpm.textContent = "Esperando";
    }
});

bf = {
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

bf.onchange(function(val){
    var status_bf = document.getElementById("status-bf")
    if (val >= 0 && bf.pastValue < 0){
        status_bf.className = "text-success fw-bold";
        status_bf.textContent = "Monitoreando";
    }
    else if (val < 0){
        status_bf.className = "text-danger fw-bold";
        status_bf.textContent = "Esperando";
    }
});


temp = {
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

temp.onchange(function(val){
    var status_temp = document.getElementById("status-temp")
    if (val >= 0 && temp.pastValue < 0){
        status_temp.className = "text-success fw-bold";
        status_temp.textContent = "Monitoreando";
    }
    else if (val < 0){
        status_temp.className = "text-danger fw-bold";
        status_temp.textContent = "Esperando";
    }
});

spo = {
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

spo.onchange(function(val){
    var status_spo = document.getElementById("status-spo")
    if (val >= 0 && spo.pastValue < 0){
        status_spo.className = "text-success fw-bold";
        status_spo.textContent = "Monitoreando";
    }
    else if (val < 0){
        status_spo.className = "text-danger fw-bold";
        status_spo.textContent = "Esperando";
    }
});

// NAME.className="mynewclass"
socket_signs.onmessage = function(e){
    // console.log(e.data);
    var recData = JSON.parse(e.data);
    bpm.value = recData.bpm;
    temp.value = recData.temp
    spo.value = recData.spo;
    bf.value = recData.bf
    if (bpm.value >= 0){
        document.getElementById("bpm_inst").innerHTML = bpm.value + "(LPM)";
    }
    else if (bpm.value < 0){
        document.getElementById("bpm_inst").innerHTML = "-" + "(LPM)";
    }

    if (temp.value >= 0){
        document.getElementById("temp_inst").innerHTML = roundToTwo(recData.temp) + "°C";
    }
    else if (temp.value < 0){
        document.getElementById("temp_inst").innerHTML = "-" + "°C";
    }

    if (spo.value >= 0){
        document.getElementById("spo_inst").innerHTML = spo.value + "°%";
    }
    else if (spo.value < 0){
        document.getElementById("spo_inst").innerHTML = "-" + "%";
    }

    if (bf.value >= 0){
        document.getElementById("bf_inst").innerHTML = bf.value + "BPM";
    }
    else if (bf.value < 0){
        document.getElementById("bf_inst").innerHTML = "-" + "BPM";
    }


};

function roundToTwo(num) {    
    return +(Math.round(num + "e+2")  + "e-2");
}
// socket.onclose = function(e){
//     alert("Desconectado");
// };