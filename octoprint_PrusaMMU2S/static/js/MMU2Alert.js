/*
 * View model for OctoPrint-Print-Queue
 *
 * Author: Michael New
 * License: AGPLv3
 */

$(function() {
	function MMU2AlertViewModel() {
		var self = this;
		self.params = parameters;
		self.settings = parameters[0];

		self.onDataUpdaterPluginMessage = function(plugin, data) {
			if (plugin != "continuousprint") return;

			var theme = 'info';
			switch(data["type"]) {
				case "popup":
					theme = "info";
					break;
				case "error":
					theme = 'danger';
					self.loadQueue();
					break;
				case "success":
					theme = 'success';
					self.loadQueue();
					break;
			
			if (data.msg != "") {
				new PNotify({
					title: 'MMU2 Alert!',
					text: data.msg,
					type: theme,
					hide: true,
					buttons: {
						closer: true,
						sticker: false
					}
				});
			}
		}
	}

	// This is how our plugin registers itself with the application, by adding some configuration
	// information to the global variable OCTOPRINT_VIEWMODELS
	OCTOPRINT_VIEWMODELS.push([
		// This is the constructor to call for instantiating the plugin
		MMU2AlertViewModel,
    [],
    []
	]);
});
