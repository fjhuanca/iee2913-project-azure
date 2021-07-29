var wavesurfer = WaveSurfer.create({
    container: '#waveform',
    // Here you can use wavesurfer docs on configuration
    // to customize your player!
  })
  // We play, pause and stop our audio file with instanciated wavesurfer.js
function startRecording() {
    wavesurfer.play()
  }
  function pauseRecording() {
    wavesurfer.pause()
  }
  function stopRecording() {
    wavesurfer.stop()
  }