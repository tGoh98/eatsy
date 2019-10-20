import json, createpeople, modeleval
from flask import Flask, render_template, request
from os import path

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    did_update = False
    errorMessage = ""
    if request.method == 'POST':
        if len(request.form) <= 1:
            errorMessage = "Please select two or more users!"
            did_update = True
        else:
            json.dump(request.form, open('selectedUsers.json', 'w'))
            return render_template("loading.html", selectedUsers=request.form)

    if not path.exists('idtonameandattr.txt'):
        createpeople.getsamplepeople()
    users = json.load(open('idtonameandattr.txt'))
    return render_template("index.html", users=users, did_update=did_update, errorMessage=errorMessage)


@app.route('/loading')
def loading():
    modeleval.createmodel()
    return render_template('loading.html')


@app.route('/results')
def results():
    restaurants = json.load(open('busselections.txt'))

    group_preferences = json.load(open('grouppreferences.txt'))
    data = []
    labels = []
    for rest in group_preferences:
        print(rest)
        labels.append(rest.replace('&', 'and'))
        data.append(group_preferences[rest])
    return render_template('results.html', restaurants=restaurants, data=data, labels=labels)


@app.route('/elements')
def elements():
    return render_template("elements.html")


if __name__ == '__main__':
    app.run(debug=True)
