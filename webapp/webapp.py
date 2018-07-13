from flask import Flask

app = Flask(__name__)

@app.route('/phil')
def index():
	return  "Hey there"

@app.route()

if  __name__ == '__main__':
	app.run(debug=True, host = '0.0.0.0')

