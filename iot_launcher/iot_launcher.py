""" 
gw4xxx-launcher - IoTmaxx Gateway Application Launcher
Copyright (C) 2021-2022 IoTmaxx GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import subprocess
import json
from pathlib import Path
import sys, os

import iot_launcher.default_config as defCfg

def launchApplication():
    configFiles = Path(defCfg.jsonConfigDir).glob("*.json")

    theServices = {}

    for file in configFiles:
        with open(file, "r") as jfile:
            theServices.update(json.load(jfile))

    with open(defCfg.jsonConfigFile, "r") as jfile:
        launcherConfig = json.load(jfile)

    if launcherConfig["launch"] != None:
        retVal = subprocess.run(theServices[launcherConfig["launch"]]["application"])
    else:
        retVal = os.EX_OK
    return retVal

