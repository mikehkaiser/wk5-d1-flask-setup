# Controller page for bikes_inv

from flask import Blueprint, render_template
from flask_login import login_required

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')

def home(): #this function tells what webpage is being displayed
    return render_template('index.html') 

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

