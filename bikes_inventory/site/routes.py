# Controller page for bikes_inv

from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')

def home(): #this function tells what webpage is being displayed
    return render_template('index.html') #function returns the entire index.html file