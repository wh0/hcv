import json
import os

import flask
import youtube_dl
import youtube_dl.version

ydl_ver = youtube_dl.version.__version__
app = flask.Flask(__name__)

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
	global destination
	destination = location
	return flask.render_template('assigned.html', location=location)

@app.route('/extract')
def extract():
	location = flask.request.args['location']
	if not location or ':' not in location:
		flask.abort(400)
	try:
		ydl = youtube_dl.YoutubeDL(params={'no_color': True})
		result = ydl.extract_info(location, download=False)
	except Exception, e:
		app.log_exception(e)
		return flask.render_template('not-extracted.html', version=ydl_ver, formatted_exc=str(e)), 500
	return flask.render_template('extracted.html', version=ydl_ver, result=result, formatted_result=json.dumps(result, indent=2))

@app.route('/up')
def up():
	flask.request.environ.get('werkzeug.server.shutdown')()
	return 'restarting'

port = int(os.environ.get('PORT', '5000'))
app.run(host='0.0.0.0', port=port)
