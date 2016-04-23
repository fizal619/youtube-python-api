#!/usr/bin/python
#query = 'Fist Fight'
#print(youtubeSearch(query))

from flask.ext.api import FlaskAPI
from flask import jsonify, request
from ytsearch import youtubeSearch


#initialize server
app = FlaskAPI(__name__)


@app.route('/')
def index():
    all_args = request.args.lists()
    query = request.args['q']
    video = youtubeSearch(query)
    return jsonify(video)

app.run('0.0.0.0', 5000)