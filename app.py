import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        json.dump(request.form, open('selectedUsers.json', 'w'))
        return render_template("loading.html")

    users = json.load(open('dummyUsers.json'))
    return render_template("index.html", users=users)


@app.route('/loading')
def loading():
    return render_template('loading.html')


@app.route('/results')
def results():
    return render_template('results.html')


@app.route('/elements')
def elements():
    return render_template("elements.html")


if __name__ == '__main__':
    app.run(debug=True)
