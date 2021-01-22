# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
from past import basestring
class MMU2Alerts(octoprint.plugin.StartupPlugin,octoprint.plugin.TemplatePlugin):
    def on_after_startup(self):
        self.potentialError=False
        self.Error=False
        self._logger.info("Plugin Started!")
        hooks = self._plugin_manager.get_hooks("octoprint.comm.transport.serial.factory")
    def findMMUerror(self, comm, line, action, *args, **kwargs):
        
        if "mmu_get_response - begin move: load"in line:
            self._plugin_manager.send_plugin_message(self._identifier, dict(type="complete", msg="MMU Is loading"))
        else if "Recv: mmu_get_response() returning: 0"in line:
            self.potentialError=True
            self._plugin_manager.send_plugin_message(self._identifier, dict(type="error", msg="Something may be wrong with the MMU"))
        else if "Recv: MMU not responding" in line:
            if !self.potentialError:
                self.potentialError=True
                self._plugin_manager.send_plugin_message(self._identifier, dict(type="error", msg="Something may be wrong with the MMU"))
            
        else if "Recv: echo:busy: paused for user"in line:
            if potentialError:
                self.error= True
                self._plugin_manager.send_plugin_message(self._identifier, dict(type="error", msg="MMU needs user attention"))
            else:
                self._plugin_manager.send_plugin_message(self._identifier, dict(type="error", msg="The printer needs user attention"))
        else:
            return
 

        self._logger.info("Received \"custom\" action from printer")
        ##~~ Softwareupdate hook
        def get_update_information(self):
            # Define the configuration for your plugin to use with the Software Update
            # Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
            # for details.
            return dict(
                MMU2Alert=dict(
                    displayName="MMU2 Alert Plugin",
                    displayVersion=self._plugin_version,

                    # version check: github repository
                    type="github_release",
                    user="Zinc-OS",
                    repo="Prusa-MMU2S-Octoprint-Plugin",
                    current=self._plugin_version,
                    stable_branch=dict(
                        name="Stable", branch="master", comittish=["master"]
                    ),
                    # update method: pip
                    pip="https://github.com/Zinc-OS/Prusa-MMU2S-Octoprint-Plugin/archive/{target_version}.zip"
                )
            )
__plugin_name__ = "MMU2S Announcement Plugin"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    plugin = CustomActionCommandPlugin()

    global __plugin_implementation__
    __plugin_implementation__ = plugin

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.received": __plugin_implementation__.findMMUerror,
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
