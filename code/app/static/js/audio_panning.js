$('document').ready(function(){
	// for legacy browsers
	const AudioContext = window.AudioContext || window.webkitAudioContext;
	const audioCtx = new AudioContext();

	const pannerOptions = {pan: 1};
	const panner = new StereoPannerNode(audioCtx, pannerOptions);

	const pannerControl = document.querySelector('#panner');
	pannerControl.addEventListener('input', function() {
	    panner.pan.value = this.value;
	}, false);

		$('.audio').each(function(){

			// get the audio element
			// 'this' is the audio element
			const audioElement = this;

			// pass it into the audio context
			const track = audioCtx.createMediaElementSource(audioElement);

			// track.connect(audioCtx.destination); 				//without panning
			track.connect(panner).connect(audioCtx.destination);  	// with panning

			audioElement.play();
			
		});
});