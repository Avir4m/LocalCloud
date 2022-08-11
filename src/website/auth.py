from flask import Blueprint, render_template, abort, redirect, request, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from itsdangerous import SignatureExpired, URLSafeTimedSerializer

from .models import User
from . import db
from . import SECRET_KEY

auth = Blueprint('auth', __name__)

s = URLSafeTimedSerializer(SECRET_KEY)


@auth.route('login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('No user with that username.', category='error')
        elif len(password) <= 1:
            flash('You must enter your password.', category='error')
        elif not check_password_hash(user.password, password):
            flash('Invalid password or email address, Please try again.', category='error')
        else:
            flash('Logged in successfully!', category='success')
            login_user(user)
            return redirect(url_for('views.index'))
        
    return render_template('login.html', user=current_user)


@auth.route('sign-up/', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        user = User.query.filter_by(username=username).first()

        if user:
            flash('Username is already in use, Try different one.', category='error')
        elif len(username) <= 1:
            flash('You must provide a username.', category='error')
        elif ' ' in username:
            flash('You cannot have spaces in username.', category='error')
        elif ' ' in password1:
            flash('You cannot have spaces in password.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 4:
            flash('Password must be at least 4 characters.', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=False)
            flash('Account created!', category='success')
            return redirect(url_for('views.index'))
        
        
    return render_template('sign-up.html', user=current_user)


@auth.route('logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('forgot_password/', methods=['POST', 'GET'])
def forgot_password():
    if request.method == 'POST':
        
        username = request.form.get('username')
        
        user = User.query.filter_by(username=username).first()
        
        if user:
            token = s.dumps(username, salt='reset-password')
            link = url_for('auth.reset_password', token=token, _external=True)

            print(f'\n\n\n\n\n[PASSWORD RESET LINK]: {link}\n\n\n\n\n')
            flash('Sent a verification link to the server console.', category='success')
        else:
            flash('This username is not connected to any account, please try different username.', category='error')
        
    return render_template('forgot_password.html', user=current_user)


@auth.route('/reset_password/<token>/', methods=['POST', 'GET'])
def reset_password(token):
    try:
        username = s.loads(token, salt='reset-password', max_age=600) # 600 Seconds (10 minutes)
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('Invalid token', category='error')
        else:
            if request.method == 'POST':
                password1 = request.form.get('password1')
                password2 = request.form.get('password1')

                if ' ' in password1:
                    flash('You cannot have spaces in password.', category='error')
                elif password1 != password2:
                    flash('Passwords don\'t match.', category='error')
                elif len(password1) < 4:
                    flash('Password must be at least 4 characters.', category='error')
                else:
                    user.password = generate_password_hash(password1, method='sha256')
                    db.session.commit()
                    flash('Password has been changed!', category='success')
                    return redirect(url_for('views.index'))

            return render_template('reset_password.html', user=current_user)

    except SignatureExpired:
        abort(404)