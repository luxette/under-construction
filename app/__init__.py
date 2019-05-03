import os
from flask import Flask, flash, render_template, session, url_for, redirect



app = Flask(__name__)

app.config['SECRET_KEY'] = 'ItsMeHoudini'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 
# DEBUG = True
# DB_USERNAME = 'bwl1289'
# DB_PASSWORD = ''
# BLOG_DATABASE_NAME = 'blog'
# DB_HOST = os.getenv('IP', '0.0.0.0')
# DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
# SQLALCHEMY_DATABASE_URI = DB_URI
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# UPLOADED_IMAGES_DEST = '/home/ubuntu/workspace/flask_blog/static/images'
# UPLOADED_IMAGES_URL = '/static/images/'
