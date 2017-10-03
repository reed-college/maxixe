"""
These are all based on an old version of the tango rest api found here:
https://github.com/autolab/Tango/wiki/Tango-REST-API/570622659163e8f7dfd032808a57a18f48006667
I wanted to use the old version of the api docs since our server is running
an old version of tango
You can find the new docs here:
https://autolab.github.io/docs/tango-rest/
"""
from flask import Flask
from json import dumps
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/open/<key>/<courselab>/')
def open(key, courselab):
    """
    This is the function that creates a new courselabs directory in Tango
    <key> is of course the Tango key and <courselab> is the name of the new
    directory
    """
    response = {
        "statusMsg": "Created directory",
        "statusId": 0,
        "files": {},
    }
    return dumps(response)
