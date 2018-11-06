from flask import Flask

app = Flask(__name__)

@app.route('/')
def fello_world():
	return "Hello, Tasfin"

if __name__ == '__main__':
	app.run(host='0.0.0.0')