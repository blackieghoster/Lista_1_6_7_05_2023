from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """
    Index

    :return: return index site code.
    rtype: string

    """
    website = "<h1>Hello WSB! Greetings from Flask!</h1>"

    return website


if __name__ == "__main__":
    app.run(debug=True)
