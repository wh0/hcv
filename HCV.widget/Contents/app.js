include('Framework/kontx/1.5/src/all.js');

var LauncherView = new KONtx.Class({
	ClassName: 'LauncherView',
	Extends: KONtx.system.AnchorSnippetView,
	createView: function () {
		this.controls.label = new KONtx.element.Text({
			label: 'Hardcoded Video',
			styles: {
				color: '#ffffff',
				fontSize: KONtx.utility.scale(20),
				hOffset: KONtx.utility.scale(18),
				vOffset: KONtx.utility.scale(22),
			},
		}).appendTo(this);
	},
});

var PlayerView = new KONtx.Class({
	ClassName: 'PlayerView',
	Extends: KONtx.system.FullscreenView,
	createView: function () {
		this.controls.controls = new KONtx.control.MediaTransportOverlay({
			rewindButton: true,
			fastforwardButton: true,
			stopButton: false,
		}).appendTo(this);
	},
	updateView: function () {
		KONtx.mediaplayer.initialize();
		var bounds = KONtx.mediaplayer.getDefaultViewportBounds();
		KONtx.mediaplayer.setViewportBounds(bounds);
		var playlist = new KONtx.media.Playlist();
		playlist.addEntryByURL('http://hcv-setup.herokuapp.com/dispatch');
		KONtx.mediaplayer.playlist.set(playlist);
		KONtx.mediaplayer.playlist.start();
	},
});

KONtx.application.init({
	views: [
		{id: 'launcher', viewClass: LauncherView},
		{id: 'player', viewClass: PlayerView},
	],
	defaultViewId: 'player',
});

