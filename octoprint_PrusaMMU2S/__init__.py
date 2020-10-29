# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
from past import basestring
class HelloWorldPlugin(octoprint.plugin.StartupPlugin,octoprint.plugin.TemplatePlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!")
        hooks = self._plugin_manager.get_hooks("octoprint.comm.transport.serial.factory")
        
