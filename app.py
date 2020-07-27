import os

from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

from helpers import benford, files
from blueprints.home import home_bp
from blueprints.results import result_bp

ALLOWED_EXTENSIONS = {'txt'}
UPLOAD_FOLDER = './uploads'

app = Flask(__name__, instance_relative_config=True)

# create and configure the app
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

test_config = None

if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.register_blueprint(home_bp)
app.register_blueprint(result_bp)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')