from flask import Blueprint, render_template

control_panel_Blueprint = Blueprint('about_blueprint', __name__)


@control_panel_Blueprint.route('/control_panel.html', methods=["GET", "POST"])
def control_panel():
    return render_template('control_panel.html')
