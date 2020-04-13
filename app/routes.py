# This file includes the different URLs that the application will implement

from app import myApp
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User


@myApp.route('/')
@myApp.route('/index')
def index():
	user = {'username': 'Albert'}
	posts = [
        {	'date': '15-oct-2019',
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
	        'date': '15-feb-2020',
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
	return render_template('index.html', title='Home', user=user, posts=posts)


@myApp.route('/about')
def about():
	return render_template('about.html', title='About')


@myApp.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	myForm = LoginForm()

	#when browser sends the GET request (receive the form), validate_on_submit() returns False
	#when browser sends POST request (submit data), validate and return True
	if myForm.validate_on_submit():
		user = User.query.filter_by(username=myForm.username.data).first()
		if user is None or not user.check_password(myForm.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))

		#if both username and password are correct, then register user as logged-in
		login_user(user, remember=myForm.remember_me.data)
		return redirect(url_for('index'))
		
	return render_template('login.html', title='Sign in', form=myForm)



