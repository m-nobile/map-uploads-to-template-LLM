
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY")
username = "martinanobile"
host = "www.pythonanywhere.com"
path = "/tmp/fileA.txt"

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']

        response = requests.post(
            'https://{host}/api/v0/user/{username}/files/path{path}'.format(
            host=host, username=username, path=path),
            files={"content": f},
            headers={'Authorization': 'Token {SECRET_KEY}'.format(SECRET_KEY=SECRET_KEY)}
        )

        return render_template("acknowledgement.html", name = SECRET_KEY, resp = response.content)






