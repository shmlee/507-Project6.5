# Import statements necessary
from flask import Flask, render_template
from flask_script import Manager
import requests
import json

# Set up application
app = Flask(__name__)

manager = Manager(app)

# Routes


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/user/<yourname>')
def hello_name(yourname):
    return '<h1>Hello {}</h1>'.format(yourname)

@app.route('/showvalues/<name>')
def basic_values_list(name):
    lst = ["hello","goodbye","tomorrow","many","words","jabberwocky"]
    if len(name) > 3:
        longname = name
        shortname = None
    else:
        longname = None
        shortname = name
    return render_template('values.html',word_list=lst,long_name=longname,short_name=shortname)


## PART 1: Add another route /word/<new_word> as the instructions describe.
@app.route('/word/<new_word>')
def word(new_word):
    baseurl = 'https://api.datamuse.com/words'
    params = {}
    params["rel_rhy"] = new_word# fill in params
    result = json.loads(requests.get(baseurl, params=params).text)
    result_word = result[0]['word']

    print(result_word)
    return '<h1>The word is {}</h1>'.format((result_word))

    





if __name__ == '__main__':
    manager.run() # Runs the flask server in a special way that makes it nice to debug
