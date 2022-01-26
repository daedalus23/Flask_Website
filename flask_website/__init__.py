from flask import Flask
from .home import home_Blueprint
from .controlpanel import control_panel_Blueprint


app = Flask(__name__)

app.register_blueprint(home_Blueprint)
app.register_blueprint(control_panel_Blueprint)
