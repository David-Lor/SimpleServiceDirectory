
#Native libraries
import os
import json


#Get absolute path of the SimpleServiceDirectory folder
DIR = os.path.dirname(os.path.abspath(__file__))

#Load settings from settings.json into the CONFIG variable
with open(DIR+"/settings.json") as f:
    CONFIG = json.load(f)

def get_sections():
    with open(DIR+"/sections.json") as f:
        return json.load(f)
