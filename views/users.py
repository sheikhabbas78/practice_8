from flask import Blueprint, request, render_template, session, redirect, url_for

from models.user.user import UserModel
import models.user.error as UserErrors
from common import image_helper

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        file = request.files['file2']

        try:
            if UserModel.register_user(username, email, password, file.filename):
                image_helper.save_image(file)
                session['email'] = email
                session['username'] = UserModel.find_by_email(email).username
                session['image_name'] = UserModel.find_by_email(email).image_name

                return redirect(url_for('home'))
        except UserErrors.UserError as e:
            return render_template('errors.html', e=e)
    return render_template('users/user_register.html')

@user_blueprint.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if UserModel.login_user(email, password):
                session['email'] = email
                session['username']= UserModel.find_by_email(email).username
                session['image_name']= UserModel.find_by_email(email).image_name
                return redirect(url_for('blog.my_blogs'))
        except UserErrors.UserError as e:
            return render_template('errors.html', e=e)
    return render_template('users/user_login.html')

@user_blueprint.route('signup')
def user_logout():
    session['email'] = None
    session['username']= None
    return redirect(url_for('home'))




