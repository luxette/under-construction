import os
from flask import Flask, flash, render_template, session, url_for, redirect



app = Flask(__name__)

app.config['SECRET_KEY'] = 'ItsMeHoudini'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
