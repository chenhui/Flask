# from flask import Flask ,url_for,escape
from app import app

# app=Flask(__name__)
app.run(debug=True)

# @app.route("/hello")
# def hello_world():
#     return "Hello world!!"

# @app.route("/")
# def index():
#     return "Index Page"

# # @app.route('/user/<username>')
# # def show_user_profile(username):
# #     return 'User %s' % (username)

# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile.'.format(escape(username))

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % (post_id)

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return 'Subpath %s' % (subpath)

# @app.route('/projects/')
# def projects():
#     return '哈喽 哈喽'

# @app.route('/about')
# def about():
#     return 'The about page!!!'

# @app.route('/login')
# def login():
#     return 'login'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login',next='/'))
    

