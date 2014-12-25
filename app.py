import os

import flask
import youtube_dl

app = flask.Flask(__name__)

ydl = youtube_dl.YoutubeDL()
destination = 'http://zippy.gfycat.com/HalfSmugAmericancicada.mp4'

@app.route('/')
def index():
	return flask.render_template('index.html', destination=destination)

@app.route('/dispatch')
def dispatch():
	return flask.redirect(destination)

@app.route('/assign', methods=['POST'])
def assign():
	location = flask.request.form['location']
	if not location or ':' not in location:
		flask.abort(400)
	destination = location
	return flask.render_template('assigned.html', location=location)

@app.route('/extract')
def extract():
	location = flask.request.args['location']
	if not location or ':' not in location:
		flask.abort(400)
	result = ydl.extract_info(location, download=False)
	return flask.render_template('extracted.html', result=result)

port = int(os.environ.get('PORT', '5000'))
app.run(host='0.0.0.0', port=port, debug=True)
