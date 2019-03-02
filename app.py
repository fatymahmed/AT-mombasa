from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/bamburi')
def bamburi():
	return '<h1>We are now in Bamburi!!</h1>'

@app.route('/town/<name>')
def town(name):
	return f'<h1>I am in {name} </h1>'

@app.route('/latin/<name>')
def latin(name):
	if name[-1]=="y":
		return f'<h1>your latin name is {name[:-1]}iful </h1>'	
	else:
		return f'<h1>your latin name is {name}y </h1>'	


if __name__ == '__main__':
	app.run(debug=True)
