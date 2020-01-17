import os
import secrets
from flask import json, url_for, redirect, Markup, Response, render_template, flash, g, session, jsonify, request, send_from_directory, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from app         import bcrypt, login_manager, db
from app.models    import User
from app.users.forms     import LoginForm, RegisterForm
import os, shutil, re, cgi, json

users = Blueprint('users', __name__)

# provide login manager with load_user callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# authenticate user
@users.route('/logout.html')
def logout():
    logout_user()
    return redirect(url_for('users.login'))


# register user
@users.route('/register.html', methods=['GET', 'POST'])
def register():
    
    # define login form here
    form = RegisterForm(request.form)

    msg = None

    # custommize your pate title / description here
    title       = 'Register an account - ipNX vCPE'
    description = 'Online ipNX virtual Customer Premises Equipment.'

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 
        name     = request.form.get('name'    , '', type=str) 
        email    = request.form.get('email'   , '', type=str) 

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()

        # filter User out of database through username
        user_by_email = User.query.filter_by(email=email).first()

        if user:
            msg = 'Username exists!'
        
        elif user_by_email:
            msg = 'The emaill entered already has an account. Choose another one.'
        
        else:                    
            pw_hash = bcrypt.generate_password_hash(password)

            user = User(username, pw_hash, name, email)

            user.save()

            msg = flash('Your account has been created. You can now login.', 'success')
            return redirect(url_for('users.login'))

    # try to match the pages defined in -> themes/light-bootstrap/pages/
    return render_template('layouts/default.html',
                            title=title,
                            content=render_template( 'pages/register.html', 
                                                     form=form,
                                                     msg=msg))


# App main route + generic routing
@users.route('/', methods=['GET', 'POST'], defaults={'path': 'login.html'})
@users.route('/<path>')
def login(path):
    # define login form here
    form = LoginForm(request.form)
    # Flask message injected into the page, in case of any errors
    msg = None
    # custommize your page title / description here
    page_title = 'Login - ipNX vCPE'
    page_description = 'Online ipNX virtual Customer Premises Equipment.'
    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():
        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        # filter User out of database through username
        user = User.query.filter_by(user=username).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('main.index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user. Check again and re-enter."
    # try to match the pages defined in -> themes/light-bootstrap/pages/
    return render_template( 'layouts/logindefault.html',
                            title=page_title,
                            content=render_template( 'pages/'+path, form=form,
                                                    msg=msg) )


