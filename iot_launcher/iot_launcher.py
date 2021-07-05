import subprocess
import json
from pathlib import Path
import sys, os

jsonConfigDir = "/config/iot_launcher.d"
jsonConfigFile = "/config/iot_launcher.json"

anyviz = {
    "anyviz": {
        "application": ["/usr/bin/anyvizcloudadapter"],
        "description": "Anyviz Cloud Adapter",
        "type": "cloudadapter",
        "publisher": {
            "name": "Mirasoft GmbH",
            "URL": "www.anyviz.de"
        }
    }
}

test1 = {
    "test1": {
        "application": ["/usr/bin/anyvizcloudadapter"],
        "description": "Anyviz Cloud Adapter",
        "type": "cloudadapter",
        "publisher": {
            "name": "Mirasoft GmbH",
            "URL": "www.anyviz.de"
        }
    }
}

test2 = {
    "test2": {
        "application": ["/usr/bin/anyvizcloudadapter"],
        "description": "Anyviz Cloud Adapter",
        "type": "cloudadapter",
        "publisher": {
            "name": "Mirasoft GmbH",
            "URL": "www.anyviz.de"
        }
    }
}

launcher_default = {
    "launch": "anyviz"
}

#set up default (start anyviz) in case this is an update from an older version without iot_launcher
# try:
#     Path(jsonConfigDir).mkdir()
#     with open("/config/iot_launcher.d/anyviz.json", "x") as jfile:
#         json.dump(anyviz, jfile)
#     with open("/config/iot_launcher.d/test1.json", "x") as jfile:
#         json.dump(test1, jfile)
#     with open("/config/iot_launcher.d/test2.json", "x") as jfile:
#         json.dump(test2, jfile)
#     with open(jsonConfigFile, "x") as jfile:
#         json.dump(launcher_default, jfile)
# except FileExistsError:
#     pass

configFiles = Path(jsonConfigDir).glob("*.json")

theServices = {}

for file in configFiles:
    with open(file, "r") as jfile:
        theServices.update(json.load(jfile))

with open(jsonConfigFile, "r") as jfile:
    launcherConfig = json.load(jfile)

if theServices[launcherConfig["launch"]]["application"] != "None":
    retVal = subprocess.run(theServices[launcherConfig["launch"]]["application"])
else:
    retVal = os.EX_OK

sys.exit(retVal)

#for service in theServices:
 #   print(service)

