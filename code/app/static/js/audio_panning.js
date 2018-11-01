function trigger_audio() {
	// for legacy browsers
	const AudioContext = window.AudioContext || window.webkitAudioContext;
	const audioCtx = new AudioContext();

	const pannerOptions = {pan: 0};
	const panner = new StereoPannerNode(audioCtx, pannerOptions);

	const pannerControl = document.querySelector('#panner');
	pannerControl.addEventListener('input', function() {
	    panner.pan.value = this.value;
	}, false);

	bufferLoader = new BufferLoader(
		audioCtx,
		$.map($('audio source'), function(x) { return x.src; }),
		function(bufferList) {
			for(i=0; i<bufferList.length; i++){

				var sound_effect = audioCtx.createBufferSource();
				sound_effect.buffer = bufferList[i];
				sound_effect.connect(panner).connect(audioCtx.destination);
				sound_effect.start(i*2); // 2 second delay between sounds
			}
		}
	);
	
    bufferLoader.load();
}