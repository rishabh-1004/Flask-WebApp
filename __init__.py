from flask import Flask, render_template, flash,request,url_for,redirect
from content_management import Content
from dbconnect import connection
from wtforms import Form

TOPIC_DICT=Content()

app=Flask(__name__)

@app.route('/')
def homepage():
	return render_template('main.html')

@app.route('/dashboard/')
def dashboard():
	return render_template('dashboard.html',TOPIC_DICT = TOPIC_DICT)

@app.route('/login/' , methods=['GET','POST'])
def login_page():
	error=None
	try:
		if request.method == "POST":
			attempted_username = request.form.get('username')
			attempted_password = request.form.get('password')
			flash(attempted_username)
			flash(attempted_password)
			if attempted_username=="admin" and attempted_password == "password":
				return redirect (url_for ('dashboard'))
			else:
				error="Invalid Credentials"

		return render_template('login.html',error=error) 
	except Exception as e:
		return render_template('login.html',error=e)

class RegistrationForm(Form):
	username=TextField('Username', [validators.Length(min=4,max=20)])
	email=TextField('Email Address', [validators.Length(min=6,max=50)])
	password=PasswordField('Password',[validator.Required(),validators.EqualTo('confirm',message="Passwords must match")])
	confirm=PasswordField('Repeat Password')
	accept_tons= BooleanField('I accept the <a href="#">Terms of Service</a>')


@app.route('/register/',methods=['GET','POST'])
def register_page():
	try:
		c,conn = connection()
		return ("okay")
	except Exception as e:
		return (str(e))

@app.errorhandler(404)
def page_not_found(e):
	return ("Page not Found")

if __name__=='__main__':
	app.secret_key = 'some secret key'
	app.run()
