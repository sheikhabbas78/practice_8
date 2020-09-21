from flask import Blueprint, render_template, request, session, redirect, url_for

from models.blog.blog import BlogModel
import models.blog.error as BlogErrors
from models.user.user import UserModel
from models.user.decorators import require_login

blog_blueprint = Blueprint('blog', __name__)

@blog_blueprint.route('/index')
def blogs_index():
    blogs = BlogModel.find_all()
    return render_template('blogs/blog_index.html', blogs=blogs)

@blog_blueprint.route('/create', methods=['GET','POST'])
@require_login
def create_blog():
    if request.method == 'POST':
        try:
            title = request.form['blogname']
            description = request.form['description']
            user = UserModel.find_by_email(session['email'])
            author_id = user._id
            if BlogModel.save_blog(title, description, author_id):
                return redirect(url_for('blog.my_blogs'))
        except BlogErrors.BlogError as e:
            return render_template('errors.html', e=e)
    return render_template('blogs/blog_create.html')

@blog_blueprint.route('/myblogs')
@require_login
def my_blogs():
    user = UserModel.find_by_email(session['email'])
    blogs = BlogModel.find_by_author_id(user._id)
    return render_template('blogs/my_blog_index.html', blogs=blogs)

@blog_blueprint.route('/delete/<string:blog_id>')
@require_login
def delete_my_blog(blog_id):
    blog = BlogModel.find_by_id(blog_id)
    blog.remove_from_mongo()
    return redirect(url_for('blog.my_blogs'))

@blog_blueprint.route('/edit/<string:blog_id>', methods=['GET', 'POST'])
@require_login
def edit_my_blog(blog_id):
    if request.method == 'POST':
        title = request.form['blogname']
        description = request.form['description']
        blog = BlogModel.find_by_id(blog_id)
        blog.title = title
        blog.description = description
        blog.save_to_mongo()
        return redirect(url_for('blog.my_blogs'))
    return render_template('blogs/edit_my_blog.html', blog=BlogModel.find_by_id(blog_id))








