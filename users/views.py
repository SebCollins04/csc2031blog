from flask import Blueprint, render_template, redirect, url_for
from users.forms import RegisterForm

users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register',  methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(form.data.get('username'))
        print(form.data.get('password'))
        return redirect(url_for('users.login'))

    return render_template('users/register.html', form=form)

@users_blueprint.route('/')
def login():
    return render_template('users/login.html')

@users_blueprint.route('/')
def account():
    return render_template('users/account.html')