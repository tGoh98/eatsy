import json
from flask import Flask, render_template, request

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
            # json.dump(request.form, open('selectedUsers.json', 'w'))
            return render_template("loading.html", selectedUsers=request.form)

    users = json.load(open('dummyUsers.json'))
    return render_template("index.html", users=users, did_update=did_update, errorMessage=errorMessage)


@app.route('/loading')
def loading():
    return render_template('loading.html')


@app.route('/results')
def results():
    restaurants = json.load(open('dummyRestaurants.json'))
    return render_template('results.html', restaurants=restaurants)


@app.route('/elements')
def elements():
    return render_template("elements.html")


if __name__ == '__main__':
    app.run(debug=True)
