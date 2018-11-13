function trigger_audio() {
	// for legacy browsers
	const AudioContext = window.AudioContext || window.webkitAudioContext;
	const audioCtx = new AudioContext();

	var pan_vals = [];
	var panner = null;

	bufferLoader = new BufferLoader(
		audioCtx,
		$.map($('audio source'), function(x) { 

			// extract the class from x [value to pan audio]
			var read_in = x.outerHTML;
			var str1 = read_in.substring(read_in.indexOf('class')+7);
			this.pan_value = str1.substring(0, str1.indexOf('"'));
			pan_vals.push(this.pan_value); 		//append position to a list

			//return the src [audio to be triggered]
			return x.src; }),

		function(bufferList) {
			for(i=0; i<bufferList.length; i++){

				panner = audioCtx.createPanner();
				panner.panningModel = 'HRTF';
				panner.distanceModel = 'inverse';
				panner.refDistance = 1;
				panner.maxDistance = 10000;
				panner.rolloffFactor = 1;
				panner.coneInnerAngle = 360;
				panner.coneOuterAngle = 0;
				panner.coneOuterGain = 0;

				var sound_effect = audioCtx.createBufferSource();
				sound_effect.buffer = bufferList[i];
				panner.positionX.value = pan_vals[i];
				sound_effect.connect(panner).connect(audioCtx.destination);
				sound_effect.start(i*2); // 2 second delay between sounds
			}
		}
	);
	
    bufferLoader.load();
}