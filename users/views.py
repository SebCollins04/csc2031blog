from flask import Blueprint, render_template

main_blueprint = Blueprint('users', __name__, template_folder='templates')


@main_blueprint.route('/')
def register():
    return render_template('users/register.html')

@main_blueprint.route('/')
def login():
    return render_template('users/login.html')

@main_blueprint.route('/')
def account():
    return render_template('users/account.html')