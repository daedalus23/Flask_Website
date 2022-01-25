from flask import Blueprint, render_template, request
import requests

home_Blueprint = Blueprint('home_blueprint', __name__)


def is_url_ok(url):
    return 200 == requests.head(url).status_code


def get_html(htmlFile):
    with open(f"./templates/{htmlFile}", "r") as file:
        temp = file.read()
    return temp


def save_html(htmlFile, newFile):
    with open(f"./templates/{htmlFile}", "w") as file:
        file.write(newFile)


@home_Blueprint.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html')


@home_Blueprint.route('/one.html', methods=["GET", "POST"])
def one():
    return render_template('one.html')


@home_Blueprint.route('/videos', methods=["GET", "POST"])
def videos(vid):
    youtube_url = 'https://www.youtube.com/watch?v=' + vid
    HTML_TEMPLATE = get_html("index.html")
    if is_url_ok(youtube_url):
        headline_html = """<a href="{url}">YouTube video: {id}</a>""".format(url=youtube_url, id=vid)
        all_html = HTML_TEMPLATE.substitute(headline=headline_html, youtube_id=vid)
    else:
        headline_html = """YouTube video <u>{id}</u> does not exist""".format(id=vid)
        all_html = HTML_TEMPLATE.substitute(headline=headline_html, youtube_id='dQw4w9WgXcQ')
    return all_html
