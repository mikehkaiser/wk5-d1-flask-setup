from flask import Blueprint, render_template, request
from bikes_inventory.forms import UserLoginForm

#UserLoginForm has been created and imported to routes page.
#routes page will not direct the traffict

#variable auth takes class Blueprint, label 'auth' in Flask app(__name__)
# and gets the templates from auth_templates'
auth = Blueprint('auth', __name__, template_folder='auth_templates')
#registers variable 'auth' with module route, which will be given to 
#__init__ to display page 
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print([email, password])
    return render_template('signup.html', form=form)

@auth.route('/signin')
def signin():
    return render_template('signin.html')