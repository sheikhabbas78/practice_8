from flask import request, redirect, render_template, Blueprint, flash, url_for, session, send_file
import os

from models.model import Model
from models.post.post import PostModel
import models.post.error as PostErrors
from models.user.user import UserModel
from models.blog.blog import BlogModel
from common.database import Database
from common import image_helper
from models.comment import CommentModel



post_blueprint = Blueprint('post', __name__)

@post_blueprint.route('/index/<string:blog_id>')
def post_index(blog_id):
    posts = PostModel.find_by_blog_id(blog_id)

    return render_template('posts/post_index.html',blog_id=blog_id, posts=posts)


@post_blueprint.route('/my_post_index/<string:blog_id>')
def my_post_index(blog_id):
    posts = PostModel.find_by_blog_id(blog_id)
    return render_template('posts/my_post_index.html', posts=posts, blog_id=blog_id)







@post_blueprint.route('/create_post/<string:blog_id>', methods=['GET', 'POST'])
def create_post(blog_id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        file = request.files['file1']
        try:
            if PostModel.find_by_title(title):
                flash('post with this title alredy exit', 'danger')
                return redirect(url_for('.create_post'), blog_id=blog_id)
        except PostErrors.PostNotFound:
            image_helper.save_image(file)
            PostModel(title, content, blog_id, file.filename).save_to_mongo()



            return redirect(url_for('.my_post_index', blog_id=blog_id))
    return render_template('posts/create_post.html')


@post_blueprint.route('/<string:blog_id>/edit_post/<string:post_id>', methods=['GET', 'POST'])
def edit_post(blog_id,post_id):
    post = PostModel.find_one_by_id(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post.title = title
        post.content = content
        post.save_to_mongo()
        return redirect(url_for('.my_post_index', blog_id=blog_id))
    return render_template('posts/edit_post.html', post=post)

@post_blueprint.route('<string:blog_id>/delete/<string:post_id>')
def delete_post(blog_id, post_id):
    post = PostModel.find_one_by_id(post_id)
    post.remove_from_mongo()
    return redirect(url_for('.my_post_index', blog_id=blog_id))

@post_blueprint.route('/<string:blog_id>/<string:post_id>/like')
def like_count(blog_id,post_id):
    post = PostModel.find_one_by_id(post_id)
    post.like = post.like + 1
    post.save_to_mongo()
    return redirect(url_for('.post_index', blog_id=blog_id))

@post_blueprint.route('/<string:blog_id>/<string:post_id>/dislike')
def dislike_count(blog_id, post_id):
    post = PostModel.find_one_by_id(post_id)
    post.dislike = post.dislike + 1
    post.save_to_mongo()
    return redirect(url_for('.post_index', blog_id=blog_id))

















