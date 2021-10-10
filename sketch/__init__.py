from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '6342426eb1d32483002eebceedaa0938'

from sketch import routes