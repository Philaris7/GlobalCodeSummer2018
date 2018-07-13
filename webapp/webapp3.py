from flask import Flask, render_template, Markup
import Twipz as twit

app = Flask(__name__)

@app.route('/')
def index():
	return   render_template('index.html')

@app.route('/tfr')
def freinds():
	f = twit.get_friends()
	s = ''
	for i in range(len(f)):
		s = s +  Markup('<b> <h2>') + str(i+1) + " : " +  f[i] + Markup('</h2> </b>') 
	return render_template('friends.html',to = s )


@app.route('/tff')
def followers():
	f = twit.get_followers()
	s = ''
	for i in range(len(f)):
		s = s +  Markup('<b> <h2>') + str(i+1) + " : " +  f[i] + Markup('</h2> </b>') 
	return render_template('index.html',to = s)

if __name__ == '__main__':
	app.run(debug=True, host = '0.0.0.0')

