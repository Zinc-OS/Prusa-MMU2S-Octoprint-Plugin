# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
from past import basestring
class HelloWorldPlugin(octoprint.plugin.StartupPlugin,octoprint.plugin.TemplatePlugin):
    def on_after_startup(self):
        self.potentialError=False
        self.Error=False
        self._logger.info("Plugin Started!")
        hooks = self._plugin_manager.get_hooks("octoprint.comm.transport.serial.factory")
    def findMMUerror(self, comm, line, action, *args, **kwargs):
        
        if line == "mmu_get_response - begin move: load":
            self._plugin_manager.send_plugin_message(self._identifier, dict(type="complete", msg="MMU Is loading"))
        else if line =="Recv: mmu_get_response() returning: 0":
            self.potentialError=True
            self._plugin_manager.send_plugin_message(self._identifier, dict(type="error", msg="Something may be wrong with the MMU"))
        else if line=="Recv: MMU not responding":
            if !self.potentialError:
                self.potentialError=True
                self._plugin_manager.send_plugin_message(self._identifier, dict(type="error", msg="Something may be wrong with the MMU"))
            
        else if line =="Recv: echo:busy: paused for user":
            if potentialError:
                self.error= True
                self._plugin_manager.send_plugin_message(self._identifier, dict(type="error", msg="MMU needs user attention"))
            else:
                self._plugin_manager.send_plugin_message(self._identifier, dict(type="error", msg="The printer needs user attention"))
        else:
            return
 

        self._logger.info("Received \"custom\" action from printer")

__plugin_name__ = "MMU2S Announcement Plugin"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    plugin = CustomActionCommandPlugin()

    global __plugin_implementation__
    __plugin_implementation__ = plugin

    global __plugin_hooks__
    __plugin_hooks__ = {"octoprint.comm.protocol.gcode.received": plugin.findMMUerror}
