"""
These are all based on an old version of the tango rest api found here:
https://github.com/autolab/Tango/wiki/Tango-REST-API/570622659163e8f7dfd032808a57a18f48006667
I wanted to use the old version of the api docs since our server is running
an old version of tango
You can find the new docs here:
https://autolab.github.io/docs/tango-rest/
also I got all of the status responses from here:
https://github.com/autolab/Tango/blob/master/restful-tango/tangoREST.py#L27
since they're not in the docs
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


@app.route('/upload/<key>/<courselab>/', methods=['POST'])
def upload(key, courselab):
    """
    This function would send a file to be stored on the Tango server
    args are the same as above with the open function
    """
    response = {
        "statusMsg": "Uploaded file",
        "statusId": 0,
    }
    return dumps(response)


@app.route('/addJob/<key>/<courselab>/', methods=['POST'])
def addJob(key, courselab):
    """
    This function would run a job on the given courselab. This means it would
    add a job to the job queue and then wen the job got off the queue, Tango
    would make a docker container with the courselab in it and the call "make"
    in the courselab directory.
    This returns the normal status message and id, but also a jobid, which
    would be used to identify the job, but here it is just a unique integer
    that this app does not keep track of
    """
    # This sets a global counter if it doesn't exist
    # increments it if it does exist
    if "jobCounter" not in globals():
        global jobCounter
        jobCounter = 1
    else:
        jobCounter += 1
    response = {
        "statusMsg": "Job added",
        "statusId": 0,
        "jobId": jobCounter,  # here we use the counter
    }
    return dumps(response)
