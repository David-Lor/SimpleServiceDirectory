
#Installed libraries
from flask import Flask, render_template
#Own files
from helpers import CONFIG, get_sections


app = Flask(__name__)

@app.route(CONFIG["route"])
def index():
    return render_template(
        "index.html",
        sections=get_sections(),
        pageTitle=CONFIG["pageTitle"]
    )

def run():
    app.run(
        host=CONFIG["host"],
        port=CONFIG["port"],
        debug=bool(CONFIG["debug"])
    )
