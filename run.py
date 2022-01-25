from flask_website import app


def read_video():
    with open(f'flask_website/static/assets/videos', 'r') as file:
        temp = file.read()
        return temp


if __name__ == "__main__":
    app.run()
