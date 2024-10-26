#!/usr/bin/python3 
#shebang . interpreter directive

#pip install pyyaml

import yaml
from pathlib import Path

  
OpenAPI_KEY = "Secret"
 


def get_settings():
    full_file_path = Path(__file__).parent.joinpath('settings.yaml')
    with open(full_file_path) as settings:
        settings_data = yaml.load(settings, Loader=yaml.Loader)
    return settings_data

try:
    settingsDict=get_settings()
    OPENIDKEY_KEY=settingsDict["OpenAPI_KEY"]
    print("open id  key" +OPENIDKEY_KEY)


except Exception as error:
    print("An exception occurred",error)
