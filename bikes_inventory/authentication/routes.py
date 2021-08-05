from flask import Blueprint, render_template, request, redirect, url_for, flash 
from flask_login import login_user, logout_user, login_required
from bikes_inventory.forms import UserLoginForm, UserSignupForm #import class UserLoginForm from forms.py
from bikes_inventory.models import User, db, check_password_hash
#import classes User and db from models.py

#UserLoginForm has been created and imported to routes page.
#routes page will not direct the traffict

#variable auth takes class Blueprint, label 'auth' in Flask app(__name__)
# and gets the templates from auth_templates'
auth = Blueprint('auth', __name__, template_folder='auth_templates')
#registers variable 'auth' with module route, which will be given to 
#__init__ to display page 
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserSignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print([email, password])
        #pushing user to the database
        user = User(email, password)
        db.session.add(user)
        db.session.commit()
        flash(f'Sign up successful for {email}.', 'user-created')
        return redirect(url_for('auth.signin'))
    return render_template('signup.html', form=form)


@auth.route('/signin', methods = ['GET','POST'])
def signin():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print([email,password])
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            flash('You were successfully logged in.', 'auth-success')
            return redirect(url_for('site.profile'))
        else:
            flash('Your email/password is incorrect', 'auth-failed')
            return redirect(url_for('auth.signin'))
    return render_template('signin.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))