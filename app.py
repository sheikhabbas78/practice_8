from flask import Flask, render_template
import os
from flask_uploads import configure_uploads

from views.users import user_blueprint
from views.blog import blog_blueprint
from views.posts import post_blueprint
from common.image_helper import IMAGE_SET

app = Flask(__name__)
app.secret_key = 'abbas'
app.config['UPLOADED_IMAGES_DEST'] = os.path.join('static')
configure_uploads(app, IMAGE_SET)

app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(blog_blueprint, url_prefix='/blogs')
app.register_blueprint(post_blueprint, url_prefix='/posts')

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)