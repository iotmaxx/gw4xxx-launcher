import subprocess
import json
from pathlib import Path

anyviz = {
    "application": ["/usr/bin/anyvizcloudadapter"],
    "description": "Anyviz Cloud Adapter",
    "type": "cloudadapter",
    "publisher": {
        "name": "Mirasoft GmbH",
        "URL": "www.anyviz.de"
    }
}

launcher_default = {
    "launch": "anyviz"
}

#set up default (start anyviz) in case this is an update from an older version without iot_launcher
try:
    Path("/config/iot_launcher.d").mkdir()
    with open("/config/iot_launcher.d/anyviz.json", "x") as jfile:
        json.dump(anyviz, jfile)
    with open("/config/iot_launcher.json", "x") as jfile:
        json.dump(launcher_default, jfile)
except FileExistsError:
    pass


