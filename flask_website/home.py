from flask import Blueprint, render_template, request

home_Blueprint = Blueprint('home_blueprint', __name__)


@home_Blueprint.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html')


@home_Blueprint.route('/one.html', methods=["GET", "POST"])
def one():
    return render_template('one.html')


@home_Blueprint.route('/star-submit', methods=["GET", "POST"])
def star_submit():
    input_box = request.form['input_box']
    print(input_box)
    return render_template('one.html')

