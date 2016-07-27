from flask import Flask
from flask import request
from flask import render_template

app = Flask("MyApp")


@app.route("/contact")
def contact():
	return render_template("index.html")


@app.route("/contact", methods=['POST'])
def sign_up():
	form_data = request.form
	print form_data['name']
	print form_data['email']
	print form_data['message']
	print form_data['url']
	return "Merci!"
	
app.run()