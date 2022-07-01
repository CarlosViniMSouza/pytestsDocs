from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)


@app.route("/project")
def project():
    return "<h1> The Project Page </h1>"


@app.route("/about")
def about():
    return "<h1> About Projects </h1>"


@app.route("/team")
def team():
    return {
        "Component01": "subject01",
        "Component02": "subject02",
        "Component03": "subject03",
        "Component04": "subject04"
    }


@app.route('/post/<int:post_id>')
def showPost(post_id):
    # show the post with the given id, the id is an integer
    return f'Post N°{post_id}'


@app.route('/path/<path:subpath>')
def showSubpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


with app.test_request_context():
    print(url_for('project'))
    print(url_for('about'))
    print(url_for('showPost', post_id=1))
